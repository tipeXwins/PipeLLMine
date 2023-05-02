137,138c137,138
<         coeff_groupings = [
<             qml.math.stack([hamiltonian.data[i] for i in indices])
---
>         coeffs = [
>             qml.math.squeeze(qml.math.take(hamiltonian.coeffs, indices, axis=0))
156a157,158
>     else:
>         coeffs = hamiltonian.coeffs
158,174c160,167
<         def processing_fn(res_groupings):
<             dot_products = [
<                 qml.math.dot(r_group, c_group)
<                 for c_group, r_group in zip(coeff_groupings, res_groupings)
<             ]
<             return qml.math.sum(qml.math.stack(dot_products), axis=0)
< 
<         return tapes, processing_fn
< 
<     coeffs = hamiltonian.data
<     tapes = []
<     for o in hamiltonian.ops:
<         with tape.__class__() as new_tape:
<             for op in tape.operations:
<                 op.queue()
<             qml.expval(o)
<         tapes.append(new_tape)
---
>         tapes = []
>         for o in hamiltonian.ops:
>             with tape.__class__() as new_tape:
>                 for op in tape.operations:
>                     op.queue()
>                 qml.expval(o)
> 
>             tapes.append(new_tape)
176a170
> 
