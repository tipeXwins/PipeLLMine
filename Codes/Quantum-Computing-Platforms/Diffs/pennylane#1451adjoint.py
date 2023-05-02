118,120c118
<         if not tape.operations:
<             tape = fn(*args, **kwargs)
<         for op in reversed(tape.operations):
---
>         for op in reversed(tape.queue):
