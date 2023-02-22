--- Cirq/Cirq#2739/after/n_qubit_tomography.py	2022-01-10 16:02:54.000000000 +0000
+++ Cirq/Cirq#2739/before/n_qubit_tomography.py	2022-01-10 16:02:54.000000000 +0000
@@ -80,12 +80,9 @@
 
         self.rot_circuit = circuits.Circuit(operations)
         self.rot_sweep = study.Product(*sweeps)
-        self.mat = self._make_state_tomography_matrix(qubits)
+        self.mat = self._make_state_tomography_matrix()
 
-    def _make_state_tomography_matrix(
-            self,
-            qubits: Sequence['cirq.Qid'],
-    ) -> np.ndarray:
+    def _make_state_tomography_matrix(self) -> np.ndarray:
         """Gets the matrix used for solving the linear system of the tomography.
 
         Returns:
@@ -99,8 +96,8 @@
 
         # Unitary matrices of each rotation circuit.
         unitaries = np.array([
-            protocols.resolve_parameters(self.rot_circuit,
-                                         rots).unitary(qubit_order=qubits)
+            protocols.unitary(
+                protocols.resolve_parameters(self.rot_circuit, rots))
             for rots in self.rot_sweep
         ])
         mat = np.einsum('jkm,jkn->jkmn', unitaries, unitaries.conj())
