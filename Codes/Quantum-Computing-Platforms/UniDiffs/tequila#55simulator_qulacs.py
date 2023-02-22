--- tequila/tequila#55/after/simulator_qulacs.py	2022-01-10 16:02:54.000000000 +0000
+++ tequila/tequila#55/before/simulator_qulacs.py	2022-01-10 16:02:54.000000000 +0000
@@ -415,7 +415,7 @@
         return circuit
 
     def sample_all_z_hamiltonian(self, samples, hamiltonian, *args, **kwargs):
-        qubits = [q for q in self.abstract_qubit_map]
+        qubits = [q for q in hamiltonian.qubits if q in self.abstract_qubit_map]
         if len(qubits) == 0:
             return sum([ps.coeff for ps in hamiltonian.paulistrings])
 
@@ -426,8 +426,7 @@
             n_samples = 0
             Etmp = 0.0
             for key, count in all_qubit_counts.items():
-                ps_support = [self.abstract_qubit_map[i] for i in paulistring._data.keys() if i in self.abstract_qubit_map]
-                parity = [k for i, k in enumerate(key.array) if i in ps_support].count(1)
+                parity = [k for i,k in enumerate(key.array) if i in paulistring._data].count(1)
                 sign = (-1) ** parity
                 Etmp += sign * count
                 n_samples += count
@@ -566,7 +565,7 @@
         result = []
         for H in self._abstract_hamiltonians:
             E = 0.0
-            if H.is_all_z() and not self.U.has_noise:
+            if H.is_all_z():
                 E = self.U.sample_all_z_hamiltonian(samples=samples, hamiltonian=H, *args, **kwargs)
             else:
                 for ps in H.paulistrings:
