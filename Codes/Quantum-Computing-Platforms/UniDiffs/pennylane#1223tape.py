--- pennylane/pennylane#1223/after/tape.py	2022-01-10 16:02:54.000000000 +0000
+++ pennylane/pennylane#1223/before/tape.py	2022-01-10 16:02:54.000000000 +0000
@@ -153,7 +153,6 @@
         stop_at = lambda obj: False
 
     new_tape = tape.__class__()
-    new_tape.__bare__ = getattr(tape, "__bare__", tape.__class__)
 
     # Check for observables acting on the same wire. If present, observables must be
     # qubit-wise commuting Pauli words. In this case, the tape is expanded with joint
