461d460
<             errlog = ""
465,467c464
<                 except TypeError as E:
<                     print("converting to interaction operator")
<                     errlog += "\n" + str(E)
---
>                 except TypeError:
469,471c466,467
<             except Exception as E:
<                 errlog += "\n" + str(E)
<                 raise TequilaException("Error in QubitEncoding " + str(self) + errlog)
---
>             except:
>                 raise TequilaException("Error in QubitEncoding " + str(self))
499,512d494
<         if "molecule" in kwargs:
<             self.molecule = kwargs["molecule"]
<         else:
<             self.molecule = self.make_molecule(*args, **kwargs)
<         assert (parameters.basis_set.lower() == self.molecule.basis.lower())
<         assert (parameters.multiplicity == self.molecule.multiplicity)
<         assert (parameters.charge == self.molecule.charge)
<         self.active_space = None
<         if active_orbitals is not None:
<             self.active_space = self._make_active_space_data(active_orbitals=active_orbitals, reference=reference)
<         if reference is None:
<             self.reference = [i for i in range(self.n_electrons // 2)]
<         else:
<             self.reference = reference
517c499
< 
---
>         trafo = None
539,545d520
<         elif hasattr(transformation, "lower") and transformation.lower() in ["tapered_bravyi_kitaev", "tbk", "t-b-k",
<                                                                              "symmetry_conserving_bravyi_kitaev"]:
<             if "active_orbitals" not in trafo_args:
<                 trafo_args["active_orbitals"] = self.n_orbitals * 2
<             if "active_fermions" not in trafo_args:
<                 trafo_args["active_fermions"] = self.n_electrons
<             trafo = openfermion.symmetry_conserving_bravyi_kitaev
562a538,547
>         if "molecule" in kwargs:
>             self.molecule = kwargs["molecule"]
>         else:
>             self.molecule = self.make_molecule(*args, **kwargs)
>         assert (parameters.basis_set.lower() == self.molecule.basis.lower())
>         assert (parameters.multiplicity == self.molecule.multiplicity)
>         assert (parameters.charge == self.molecule.charge)
>         self.active_space = None
>         if active_orbitals is not None:
>             self.active_space = self._make_active_space_data(active_orbitals=active_orbitals, reference=reference)
738a724,726
>         if reference_orbitals is None:
>             reference_orbitals = [i for i in range(self.n_electrons // 2)]
>         spin_orbitals = sorted([2 * i for i in reference_orbitals] + [2 * i + 1 for i in reference_orbitals])
743,749c731
<         if self.transformation._trafo == openfermion.symmetry_conserving_bravyi_kitaev:
<             def tapering(fop):
<                 fermion_hamiltonian_reorder = openfermion.utils.reorder(fop, openfermion.utils.up_then_down,
<                                                                         num_modes=n_qubits)
<                 qubit_hamiltonian = openfermion.bravyi_kitaev_tree(fermion_hamiltonian_reorder, n_qubits=n_qubits)
<                 qubit_hamiltonian.compress()
<                 return qubit_hamiltonian
---
>         string = ""
751,757d732
<             transformation = tapering
<         else:
<             transformation = self.transformation
<         if reference_orbitals is None:
<             reference_orbitals = self.reference
<         spin_orbitals = sorted([2 * i for i in reference_orbitals] + [2 * i + 1 for i in reference_orbitals])
<         string = "1.0 ["
760d734
<         string += "]"
763c737,738
<         op = QubitHamiltonian(qubit_hamiltonian=transformation(fop))
---
> 
>         op = QubitHamiltonian(qubit_hamiltonian=self.transformation(fop))
768,773c743,744
<         key = list(wfn.keys())[0]
<         if self.transformation._trafo == openfermion.symmetry_conserving_bravyi_kitaev:
<             active_qubits = [i for i in range(n_qubits) if i not in [n_qubits - 1, n_qubits // 2 - 1]]
<             array = [key.array[i] for i in active_qubits]
<             key = BitString.from_array(array=array)
<         return key
---
>         keys = [k for k in wfn.keys()]
>         return keys[-1]
885,906d855
<     def make_upgccsd_ansatz(self,
<                             include_singles:bool=True,
<                             include_reference:bool=True,
<                             indices:list=None,
<                             order:int =1,
<                             *args, **kwargs):
<         if indices is None:
<             indices = []
<             for i in range(self.n_orbitals):
<                 for a in range(i + 1, self.n_orbitals):
<                     indices.append(((2 * i, 2 * a), (2 * i + 1, 2 * a + 1)))
<                     if include_singles:
<                         indices.append(((2 * i, 2 * a)))
<                         indices.append(((2 * i + 1, 2 * a + 1)))
<         U = QCircuit()
<         if include_reference:
<             U = self.prepare_reference()
<         generators = [self.make_excitation_generator(i, *args, **kwargs) for i in indices]
<         for k in range(order):
<             idx = [(k,i) for i in indices]
<             U += gates.Trotterized(generators=generators, angles=idx, steps=1)
<         return U
994a944
>                     print("sp = ", spin_indices)
995a946
>                         print("idx = ", idx)
