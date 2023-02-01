358c358
<         qubits = [q for q in self.abstract_qubit_map]
---
>         qubits = [q for q in hamiltonian.qubits if q in self.abstract_qubit_map]
372,373c372
<                 ps_support = [self.abstract_qubit_map[i] for i in paulistring._data.keys() if i in self.abstract_qubit_map]
<                 parity = [k for i, k in enumerate(key.array) if i in ps_support].count(1)
---
>                 parity = [k for i,k in enumerate(key.array) if i in paulistring._data].count(1)
377c376
<             E += (Etmp /samples) * paulistring.coeff
---
>             E += Etmp / samples * paulistring.coeff
710c709
<                E = self.U.sample_all_z_hamiltonian(samples=samples, hamiltonian=H, *args, **kwargs)
---
>                 E = self.U.sample_all_z_hamiltonian(samples=samples, hamiltonian=H, *args, **kwargs)
