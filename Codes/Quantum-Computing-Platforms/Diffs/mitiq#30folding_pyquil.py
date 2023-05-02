5c5
< from mitiq.folding_cirq import _get_num_to_fold
---
> 
31c31
<     num_to_fold = _get_num_to_fold(stretch, ngates)
---
>     num_to_fold = int(ngates * (stretch - 1) / 2)
54c54
<     num_to_fold = _get_num_to_fold(stretch, ngates)
---
>     num_to_fold = int(ngates * (stretch - 1) / 2)
128c128
<     num_to_fold = _get_num_to_fold(stretch, ngates)
---
>     num_to_fold = int(ngates * fractional_stretch / 2)
