61c61
<     if not isinstance(classical_reg3, int) and not isinstance(classical_reg3, float):
---
>     if not isinstance(classical_reg3, int):
642,643d641
<     if not isinstance(source, int) and not isinstance(source, float):
<         source = unpack_classical_reg(source)
648,649c646
<     return ClassicalConvert(unpack_classical_reg(classical_reg1),
<                             unpack_classical_reg(classical_reg2))
---
>     return ClassicalConvert(classical_reg1, classical_reg2)
