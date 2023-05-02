65,66c65
<             fixed_qubit_count = g.fixed_qubit_count()
<             if fixed_qubit_count is NotImplemented:
---
>             if g != Gate.Unitary and g().qubit_count != noise.qubit_count:
68,74c67,68
<                     f"Target gate {g} can be instantiated on a variable number of qubits,"
<                     " but noise can only target gates with fixed qubit counts."
<                 )
<             if fixed_qubit_count != noise.qubit_count:
<                 raise ValueError(
<                     f"Target gate {g} acts on {fixed_qubit_count} qubits,"
<                     f" but {noise} acts on {noise.qubit_count} qubits."
---
>                     "The target_targets must be gates that have the same number of \
> qubits as defined by the multi-qubit noise channel."
