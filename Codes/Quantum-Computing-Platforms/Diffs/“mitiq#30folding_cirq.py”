103,104d102
< def _get_num_to_fold(stretch: float, ngates: int) -> int:
<     return round(ngates * (stretch - 1.0) / 2.0)
128,130c126
<     num_to_fold = _get_num_to_fold(stretch, ngates)
<     if num_to_fold == 0:
<         return folded
---
>     num_to_fold = int(ngates * (stretch - 1.0) / 2.0)
220c216
<     num_to_fold = _get_num_to_fold(stretch, ngates)
---
>     num_to_fold = int(ngates * (stretch - 1.0) / 2.0)
317c313
<     return circuit + eye
---
>     return circuit + eye
\ No newline at end of file
