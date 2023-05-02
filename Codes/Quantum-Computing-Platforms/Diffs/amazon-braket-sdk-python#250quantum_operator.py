15c15
< from typing import Any, List, Optional, Sequence
---
> from typing import Any, List, Sequence
25c25
<     def __init__(self, qubit_count: Optional[int], ascii_symbols: Sequence[str]):
---
>     def __init__(self, qubit_count: int, ascii_symbols: Sequence[str]):
42,55c42,44
<         fixed_qubit_count = self.fixed_qubit_count()
<         if fixed_qubit_count is NotImplemented:
<             self._qubit_count = qubit_count
<         else:
<             if qubit_count and qubit_count != fixed_qubit_count:
<                 raise ValueError(
<                     f"Provided qubit count {qubit_count}"
<                     "does not equal fixed qubit count {fixed_qubit_count}"
<                 )
<             self._qubit_count = fixed_qubit_count
<         if not isinstance(self._qubit_count, int):
<             raise TypeError(f"qubit_count, {self._qubit_count}, must be an integer")
<         if self._qubit_count < 1:
<             raise ValueError(f"qubit_count, {self._qubit_count}, must be greater than zero")
---
>         if qubit_count < 1:
>             raise ValueError(f"qubit_count, {qubit_count}, must be greater than zero")
>         self._qubit_count = qubit_count
60,64c49,50
<         if len(ascii_symbols) != self._qubit_count:
<             msg = (
<                 f"ascii_symbols, {ascii_symbols},"
<                 f" length must equal qubit_count, {self._qubit_count}"
<             )
---
>         if len(ascii_symbols) != qubit_count:
>             msg = f"ascii_symbols, {ascii_symbols}, length must equal qubit_count, {qubit_count}"
67,70d52
< 
<     @staticmethod
<     def fixed_qubit_count() -> int:
<         return NotImplemented
