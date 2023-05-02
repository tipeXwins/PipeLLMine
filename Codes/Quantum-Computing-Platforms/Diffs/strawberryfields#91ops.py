1239c1239
< class _Delete(MetaOperation):
---
> class Delete(MetaOperation):
1275c1275
<     Program._current_context.append(_New_modes(n), refs)
---
>     Program._current_context.append(New_modes(n), refs)
1279c1279
< class _New_modes(MetaOperation):
---
> class New_modes(MetaOperation):
1633c1633
< Del = _Delete()
---
> Del = Delete()
