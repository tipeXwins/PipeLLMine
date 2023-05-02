72,74c72
<     def copy(
<         self, target_mapping: Dict[QubitInput, QubitInput] = None, target: QubitSetInput = None
<     ):
---
>     def copy(self, target_mapping: Dict[QubitInput, QubitInput] = {}, target: QubitSetInput = None):
113,114c111,113
<         elif hasattr(copy, "target"):
<             copy.target = self._target.map(target_mapping or {})
---
>         else:
>             if hasattr(copy, "target"):
>                 copy.target = self._target.map(target_mapping)
