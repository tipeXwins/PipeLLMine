105,108c105,108
<         # Get qubit mitigation matrix and mitigate probs
<         if qubits is None:
<             qubits = range(num_qubits)
<         ainvs = self._mitigation_mats[list(qubits)]
---
>         if qubits is not None:
>             ainvs = self._mitigation_mats[list(qubits)]
>         else:
>             ainvs = self._mitigation_mats
