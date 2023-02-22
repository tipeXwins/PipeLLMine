--- pennylane/pennylane#1451/after/adjoint.py	2022-01-10 16:02:54.000000000 +0000
+++ pennylane/pennylane#1451/before/adjoint.py	2022-01-10 16:02:54.000000000 +0000
@@ -115,9 +115,7 @@
     def wrapper(*args, **kwargs):
         with get_active_tape().stop_recording(), QuantumTape() as tape:
             fn(*args, **kwargs)
-        if not tape.operations:
-            tape = fn(*args, **kwargs)
-        for op in reversed(tape.operations):
+        for op in reversed(tape.queue):
             try:
                 op.adjoint()
             except NotImplementedError:
