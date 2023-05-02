141c141
<         qubit_range = instruction.target
---
>         qubit_range = range(min(instruction.target), max(instruction.target) + 1)
