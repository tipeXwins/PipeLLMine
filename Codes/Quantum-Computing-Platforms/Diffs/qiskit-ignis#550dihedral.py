404c404,405
<         super().__init__(num_qubits=self._num_qubits)
---
>         dims = self._num_qubits * (2,)
>         super().__init__(dims, dims)
593c594
<         elem = CNOTDihedral(self._num_qubits)
---
>         elem = CNOTDihedral(self.num_qubits)
