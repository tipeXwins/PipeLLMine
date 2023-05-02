739,741c739,740
<         if not (isinstance(right, MemoryReference) or isinstance(right, int)
<                 or isinstance(right, float)):
<             raise TypeError("right operand should be an MemoryReference or an int or float.")
---
>         if not isinstance(right, MemoryReference):
>             raise TypeError("right operand should be an MemoryReference")
