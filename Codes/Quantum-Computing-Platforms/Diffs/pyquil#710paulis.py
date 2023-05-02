28c28
< from .gates import I, H, RZ, RX, CNOT, X, PHASE, QUANTUM_GATES
---
> from .gates import H, RZ, RX, CNOT, X, PHASE, QUANTUM_GATES
715,721c715
<     if isinstance(term, PauliTerm):
<         return (len(term) == 0) and (not np.isclose(term.coefficient, 0))
<     elif isinstance(term, PauliSum):
<         return (len(term.terms) == 1) and (len(term.terms[0]) == 0) and \
<                (not np.isclose(term.terms[0].coefficient, 0))
<     else:
<         raise TypeError("is_identity only checks PauliTerms and PauliSum objects!")
---
>     return len(term) == 0
756,757d749
<         elif is_zero(term):
<             pass
881c873,876
<         return np.isclose(pauli_object.coefficient, 0)
---
>         if pauli_object.id() == '':
>             return True
>         else:
>             return False
883c878,881
<         return len(pauli_object.terms) == 1 and np.isclose(pauli_object.terms[0].coefficient, 0)
---
>         if len(pauli_object.terms) == 1 and pauli_object.terms[0].id() == '':
>             return True
>         else:
>             return False
