--- Cirq/Cirq#3125/after/decompositions.py	2022-01-10 16:02:54.000000000 +0000
+++ Cirq/Cirq#3125/before/decompositions.py	2022-01-10 16:02:54.000000000 +0000
@@ -500,19 +500,6 @@
             interaction_matrix(x_mat, x),
             before)
 
-    def _decompose_(self, qubits):
-        from cirq import ops
-        a, b = qubits
-        return [
-            ops.GlobalPhaseOperation(self.global_phase),
-            ops.MatrixGate(self.single_qubit_operations_before[0]).on(a),
-            ops.MatrixGate(self.single_qubit_operations_before[1]).on(b),
-            np.exp(1j * ops.X(a) * ops.X(b) * self.interaction_coefficients[0]),
-            np.exp(1j * ops.Y(a) * ops.Y(b) * self.interaction_coefficients[1]),
-            np.exp(1j * ops.Z(a) * ops.Z(b) * self.interaction_coefficients[2]),
-            ops.MatrixGate(self.single_qubit_operations_after[0]).on(a),
-            ops.MatrixGate(self.single_qubit_operations_after[1]).on(b),
-        ]
 
 def scatter_plot_normalized_kak_interaction_coefficients(
         interactions: Iterable[
