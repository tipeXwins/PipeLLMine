651,655c651,652
<         for idx, op in enumerate(self._ops):
<             try:
<                 self._ops[idx] = op.adjoint()
<             except NotImplementedError:
<                 op.inverse = not op.inverse
---
>         for op in self._ops:
>             op.inverse = not op.inverse
658,669d654
< 
<     def adjoint(self):
<         new_tape = self.copy(copy_operations=True)
<         qml.transforms.invisible(new_tape.inv)()
<         QuantumTape._lock.acquire()
<         try:
<             QueuingContext.append(new_tape)
<         except Exception as _:
<             QuantumTape._lock.release()
<             raise
<         QuantumTape._lock.release()
<         return new_tape
