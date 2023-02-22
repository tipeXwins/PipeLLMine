--- tequila/tequila#55/after/simulator_base.py	2022-01-10 16:02:54.000000000 +0000
+++ tequila/tequila#55/before/simulator_base.py	2022-01-10 16:02:54.000000000 +0000
@@ -355,7 +355,7 @@
 
     def sample_all_z_hamiltonian(self, samples: int, hamiltonian, *args, **kwargs):
         # make measurement instruction
-        qubits = [q for q in self.abstract_qubit_map]
+        qubits = [q for q in hamiltonian.qubits if q in self.abstract_qubit_map]
         if len(qubits) == 0:
             return sum([ps.coeff for ps in hamiltonian.paulistrings])
         measure = Measurement(target=qubits)
@@ -369,12 +369,11 @@
             n_samples = 0
             Etmp = 0.0
             for key, count in counts.items():
-                ps_support = [self.abstract_qubit_map[i] for i in paulistring._data.keys() if i in self.abstract_qubit_map]
-                parity = [k for i, k in enumerate(key.array) if i in ps_support].count(1)
+                parity = [k for i,k in enumerate(key.array) if i in paulistring._data].count(1)
                 sign = (-1) ** parity
                 Etmp += sign * count
                 n_samples += count
-            E += (Etmp /samples) * paulistring.coeff
+            E += Etmp / samples * paulistring.coeff
         return E
 
     def sample_paulistring(self, samples: int, paulistring, *args,
@@ -707,7 +706,7 @@
         for H in self._abstract_hamiltonians:
             E = 0.0
             if H.is_all_z():
-               E = self.U.sample_all_z_hamiltonian(samples=samples, hamiltonian=H, *args, **kwargs)
+                E = self.U.sample_all_z_hamiltonian(samples=samples, hamiltonian=H, *args, **kwargs)
             else:
                 for ps in H.paulistrings:
                     E += self.sample_paulistring(samples=samples, paulistring=ps, *args, **kwargs)
