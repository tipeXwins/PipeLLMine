14c14
< from typing import Any, Optional, Sequence
---
> from typing import Any, Sequence
29c29,33
<     def __init__(self, qubit_count: Optional[int], ascii_symbols: Sequence[str]):
---
>     def __init__(
>         self,
>         qubit_count: int,
>         ascii_symbols: Sequence[str],
>     ):
32c36
<             qubit_count (int, optional): Number of qubits this noise channel interacts with.
---
>             qubit_count (int): Number of qubits this noise channel interacts with.
42c46,54
<         super().__init__(qubit_count=qubit_count, ascii_symbols=ascii_symbols)
---
>         if qubit_count < 1:
>             raise ValueError(f"qubit_count, {qubit_count}, must be greater than zero")
>         self._qubit_count = qubit_count
>         if ascii_symbols is None:
>             raise ValueError("ascii_symbols must not be None")
>         if len(ascii_symbols) != qubit_count:
>             msg = f"ascii_symbols, {ascii_symbols}, length must equal qubit_count, {qubit_count}"
>             raise ValueError(msg)
>         self._ascii_symbols = tuple(ascii_symbols)
96,98c108
<     def __init__(
<         self, probability: float, qubit_count: Optional[int], ascii_symbols: Sequence[str]
<     ):
---
>     def __init__(self, probability: float, qubit_count: int, ascii_symbols: Sequence[str]):
138,140c148
<     def __init__(
<         self, probability: float, qubit_count: Optional[int], ascii_symbols: Sequence[str]
<     ):
---
>     def __init__(self, probability: float, qubit_count: int, ascii_symbols: Sequence[str]):
180,182c188
<     def __init__(
<         self, probability: float, qubit_count: Optional[int], ascii_symbols: Sequence[str]
<     ):
---
>     def __init__(self, probability: float, qubit_count: int, ascii_symbols: Sequence[str]):
227c233
<         qubit_count: Optional[int],
---
>         qubit_count: int,
301c307
<     def __init__(self, gamma: float, qubit_count: Optional[int], ascii_symbols: Sequence[str]):
---
>     def __init__(self, gamma: float, qubit_count: int, ascii_symbols: Sequence[str]):
342,346c348
<         self,
<         gamma: float,
<         probability: float,
<         qubit_count: Optional[int],
<         ascii_symbols: Sequence[str],
---
>         self, gamma: float, probability: float, qubit_count: int, ascii_symbols: Sequence[str]
