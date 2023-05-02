83c83
<         self.mat = self._make_state_tomography_matrix(qubits)
---
>         self.mat = self._make_state_tomography_matrix()
85,88c85
<     def _make_state_tomography_matrix(
<             self,
<             qubits: Sequence['cirq.Qid'],
<     ) -> np.ndarray:
---
>     def _make_state_tomography_matrix(self) -> np.ndarray:
102,103c99,100
<             protocols.resolve_parameters(self.rot_circuit,
<                                          rots).unitary(qubit_order=qubits)
---
>             protocols.unitary(
>                 protocols.resolve_parameters(self.rot_circuit, rots))
