576,578c576
<         if isinstance(self.qfunc_output, Sequence) or (
<             self.qtape.is_sampled and self.device._has_partitioned_shots()
<         ):
---
>         if isinstance(self.qfunc_output, Sequence):
