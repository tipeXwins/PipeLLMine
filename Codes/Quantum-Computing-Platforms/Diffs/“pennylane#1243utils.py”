308,309c308,309
<         new_tape = operation_list.adjoint()
<         return new_tape
---
>         operation_list.inv()
>         return operation_list
337c337
<     def qfunc():
---
>     with qml.tape.QuantumTape() as tape:
339a340,341
>             if o.inverse:
>                 o.inv()
341,342c343
<     with qml.tape.QuantumTape() as tape:
<         qml.adjoint(qfunc)()
---
>     tape.inv()
