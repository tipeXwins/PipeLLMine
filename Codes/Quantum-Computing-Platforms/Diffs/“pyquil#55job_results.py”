103c103
<     num_memory_octets = _round_to_next_multiple(num_addresses, 8) // 8
---
>     num_memory_octets = int(_round_to_next_multiple(num_addresses, 8) / 8)
115c115
<     wf = np.zeros(num_wavefunction_octets // OCTETS_PER_COMPLEX_DOUBLE, dtype=np.cfloat)
---
>     wf = np.zeros(int(num_wavefunction_octets / OCTETS_PER_COMPLEX_DOUBLE), dtype=np.cfloat)
