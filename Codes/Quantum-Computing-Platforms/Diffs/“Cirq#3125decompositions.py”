503,515d502
<     def _decompose_(self, qubits):
<         from cirq import ops
<         a, b = qubits
<         return [
<             ops.GlobalPhaseOperation(self.global_phase),
<             ops.MatrixGate(self.single_qubit_operations_before[0]).on(a),
<             ops.MatrixGate(self.single_qubit_operations_before[1]).on(b),
<             np.exp(1j * ops.X(a) * ops.X(b) * self.interaction_coefficients[0]),
<             np.exp(1j * ops.Y(a) * ops.Y(b) * self.interaction_coefficients[1]),
<             np.exp(1j * ops.Z(a) * ops.Z(b) * self.interaction_coefficients[2]),
<             ops.MatrixGate(self.single_qubit_operations_after[0]).on(a),
<             ops.MatrixGate(self.single_qubit_operations_after[1]).on(b),
<         ]
