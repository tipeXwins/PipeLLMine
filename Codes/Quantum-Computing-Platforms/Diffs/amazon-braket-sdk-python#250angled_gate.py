15c15
< from typing import Optional, Sequence
---
> from typing import Sequence
25c25
<     def __init__(self, angle: float, qubit_count: Optional[int], ascii_symbols: Sequence[str]):
---
>     def __init__(self, angle: float, qubit_count: int, ascii_symbols: Sequence[str]):
