--- tequila/tequila#47/after/qc_base.py	2022-01-10 16:02:54.000000000 +0000
+++ tequila/tequila#47/before/qc_base.py	2022-01-10 16:02:54.000000000 +0000
@@ -458,17 +458,13 @@
             self._kwargs = kwargs
 
         def __call__(self, op):
-            errlog = ""
             try:
                 try:
                     return self._trafo(op, **self._kwargs)
-                except TypeError as E:
-                    print("converting to interaction operator")
-                    errlog += "\n" + str(E)
+                except TypeError:
                     return self._trafo(openfermion.get_interaction_operator(op), **self._kwargs)
-            except Exception as E:
-                errlog += "\n" + str(E)
-                raise TequilaException("Error in QubitEncoding " + str(self) + errlog)
+            except:
+                raise TequilaException("Error in QubitEncoding " + str(self))
 
         def __repr__(self):
             if len(self._kwargs) > 0:
@@ -496,25 +492,11 @@
                  **kwargs):
 
         self.parameters = parameters
-        if "molecule" in kwargs:
-            self.molecule = kwargs["molecule"]
-        else:
-            self.molecule = self.make_molecule(*args, **kwargs)
-        assert (parameters.basis_set.lower() == self.molecule.basis.lower())
-        assert (parameters.multiplicity == self.molecule.multiplicity)
-        assert (parameters.charge == self.molecule.charge)
-        self.active_space = None
-        if active_orbitals is not None:
-            self.active_space = self._make_active_space_data(active_orbitals=active_orbitals, reference=reference)
-        if reference is None:
-            self.reference = [i for i in range(self.n_electrons // 2)]
-        else:
-            self.reference = reference
 
         # filter out arguments to the transformation
         trafo_args = {k.split("__")[1]: v for k, v in kwargs.items() if
                       (hasattr(k, "lower") and "transformation__" in k.lower())}
-
+        trafo = None
         if transformation is None:
             trafo = openfermion.jordan_wigner
         elif hasattr(transformation, "lower") and transformation.lower() in ["jordan-wigner", "jw", "j-w",
@@ -536,13 +518,6 @@
         elif hasattr(transformation, "lower") and transformation.lower() in ["bravyi-kitaev-tree", "bkt",
                                                                              "bravykitaevtree", "b-k-t"]:
             trafo = openfermion.bravyi_kitaev_tree
-        elif hasattr(transformation, "lower") and transformation.lower() in ["tapered_bravyi_kitaev", "tbk", "t-b-k",
-                                                                             "symmetry_conserving_bravyi_kitaev"]:
-            if "active_orbitals" not in trafo_args:
-                trafo_args["active_orbitals"] = self.n_orbitals * 2
-            if "active_fermions" not in trafo_args:
-                trafo_args["active_fermions"] = self.n_electrons
-            trafo = openfermion.symmetry_conserving_bravyi_kitaev
         elif hasattr(transformation, "lower"):
             trafo = getattr(openfermion, transformation.lower())
         else:
@@ -560,6 +535,16 @@
             trafo = transformation
 
         self.transformation = self._QubitEncoding(transformation=trafo, **trafo_args)
+        if "molecule" in kwargs:
+            self.molecule = kwargs["molecule"]
+        else:
+            self.molecule = self.make_molecule(*args, **kwargs)
+        assert (parameters.basis_set.lower() == self.molecule.basis.lower())
+        assert (parameters.multiplicity == self.molecule.multiplicity)
+        assert (parameters.charge == self.molecule.charge)
+        self.active_space = None
+        if active_orbitals is not None:
+            self.active_space = self._make_active_space_data(active_orbitals=active_orbitals, reference=reference)
 
         self._rdm1 = None
         self._rdm2 = None
@@ -736,41 +721,27 @@
         Returns
         -------
         """
+        if reference_orbitals is None:
+            reference_orbitals = [i for i in range(self.n_electrons // 2)]
+        spin_orbitals = sorted([2 * i for i in reference_orbitals] + [2 * i + 1 for i in reference_orbitals])
 
         if n_qubits is None:
             n_qubits = 2 * self.n_orbitals
 
-        if self.transformation._trafo == openfermion.symmetry_conserving_bravyi_kitaev:
-            def tapering(fop):
-                fermion_hamiltonian_reorder = openfermion.utils.reorder(fop, openfermion.utils.up_then_down,
-                                                                        num_modes=n_qubits)
-                qubit_hamiltonian = openfermion.bravyi_kitaev_tree(fermion_hamiltonian_reorder, n_qubits=n_qubits)
-                qubit_hamiltonian.compress()
-                return qubit_hamiltonian
+        string = ""
 
-            transformation = tapering
-        else:
-            transformation = self.transformation
-        if reference_orbitals is None:
-            reference_orbitals = self.reference
-        spin_orbitals = sorted([2 * i for i in reference_orbitals] + [2 * i + 1 for i in reference_orbitals])
-        string = "1.0 ["
         for i in spin_orbitals:
             string += str(i) + "^ "
-        string += "]"
 
         fop = openfermion.FermionOperator(string, 1.0)
-        op = QubitHamiltonian(qubit_hamiltonian=transformation(fop))
+
+        op = QubitHamiltonian(qubit_hamiltonian=self.transformation(fop))
         from tequila.wavefunction.qubit_wavefunction import QubitWaveFunction
         wfn = QubitWaveFunction.from_int(0, n_qubits=n_qubits)
         wfn = wfn.apply_qubitoperator(operator=op)
         assert (len(wfn.keys()) == 1)
-        key = list(wfn.keys())[0]
-        if self.transformation._trafo == openfermion.symmetry_conserving_bravyi_kitaev:
-            active_qubits = [i for i in range(n_qubits) if i not in [n_qubits - 1, n_qubits // 2 - 1]]
-            array = [key.array[i] for i in active_qubits]
-            key = BitString.from_array(array=array)
-        return key
+        keys = [k for k in wfn.keys()]
+        return keys[-1]
 
     def make_molecule(self, *args, **kwargs) -> MolecularData:
         """Creates a molecule in openfermion format by running psi4 and extracting the data
@@ -882,28 +853,6 @@
         """
 
         return prepare_product_state(self.reference_state(*args, **kwargs))
-    def make_upgccsd_ansatz(self,
-                            include_singles:bool=True,
-                            include_reference:bool=True,
-                            indices:list=None,
-                            order:int =1,
-                            *args, **kwargs):
-        if indices is None:
-            indices = []
-            for i in range(self.n_orbitals):
-                for a in range(i + 1, self.n_orbitals):
-                    indices.append(((2 * i, 2 * a), (2 * i + 1, 2 * a + 1)))
-                    if include_singles:
-                        indices.append(((2 * i, 2 * a)))
-                        indices.append(((2 * i + 1, 2 * a + 1)))
-        U = QCircuit()
-        if include_reference:
-            U = self.prepare_reference()
-        generators = [self.make_excitation_generator(i, *args, **kwargs) for i in indices]
-        for k in range(order):
-            idx = [(k,i) for i in indices]
-            U += gates.Trotterized(generators=generators, angles=idx, steps=1)
-        return U
 
     def make_uccsd_ansatz(self, trotter_steps: int,
                           initial_amplitudes: typing.Union[str, Amplitudes, ClosedShellAmplitudes] = "mp2",
@@ -992,7 +941,9 @@
                             spin_indices.append([2 * key[0], 2 * key[1], 2 * key[2], 2 * key[3]])
                             spin_indices.append([2 * key[0] + 1, 2 * key[1] + 1, 2 * key[2] + 1, 2 * key[3] + 1])
                         partner = tuple([key[2], key[1], key[0], key[3]])  # taibj -> tbiaj
+                    print("sp = ", spin_indices)
                     for idx in spin_indices:
+                        print("idx = ", idx)
                         idx = [(idx[2 * i], idx[2 * i + 1]) for i in range(len(idx) // 2)]
                         generators.append(self.make_excitation_generator(indices=idx))
 
