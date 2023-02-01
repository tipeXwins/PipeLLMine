20c20
< from cirq import circuits, ops, extension, value
---
> from cirq import circuits, ops, extension
22a23
> from cirq.value import Symbol
212c213
<                       axis_half_turns=2*a-b).on(op.qubits[0])
---
>                       axis_half_turns=b-2*a).on(op.qubits[0])
304c305
<     if isinstance(h, value.Symbol):
---
>     if isinstance(h, Symbol):
312,313c313,314
<             isinstance(op.gate.half_turns, value.Symbol) or
<             isinstance(op.gate.axis_half_turns, value.Symbol)):
---
>             isinstance(op.gate.half_turns, Symbol) or
>             isinstance(op.gate.axis_half_turns, Symbol)):
323c324
<     if isinstance(h, value.Symbol):
---
>     if isinstance(h, Symbol):
