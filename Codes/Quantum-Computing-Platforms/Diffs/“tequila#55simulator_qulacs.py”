418c418
<         qubits = [q for q in self.abstract_qubit_map]
---
>         qubits = [q for q in hamiltonian.qubits if q in self.abstract_qubit_map]
429,430c429
<                 ps_support = [self.abstract_qubit_map[i] for i in paulistring._data.keys() if i in self.abstract_qubit_map]
<                 parity = [k for i, k in enumerate(key.array) if i in ps_support].count(1)
---
>                 parity = [k for i,k in enumerate(key.array) if i in paulistring._data].count(1)
569c568
<             if H.is_all_z() and not self.U.has_noise:
---
>             if H.is_all_z():
