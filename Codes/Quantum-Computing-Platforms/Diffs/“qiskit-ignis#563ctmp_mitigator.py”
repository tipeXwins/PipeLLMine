114a115,116
>         if qubits is None:
>             qubits = list(range(self._num_qubits))
117,120c119,120
<             counts, clbits=clbits, qubits=qubits, return_shots=True)
<         num_qubits = int(np.log2(probs.shape[0]))
<         if qubits is None:
<             qubits = list(range(num_qubits))
---
>             counts, clbits=clbits, qubits=qubits,
>             num_qubits=len(qubits), return_shots=True)
