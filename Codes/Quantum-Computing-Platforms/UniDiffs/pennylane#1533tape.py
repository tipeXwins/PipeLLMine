--- pennylane/pennylane#1533/after/tape.py	2022-01-10 16:02:54.000000000 +0000
+++ pennylane/pennylane#1533/before/tape.py	2022-01-10 16:02:54.000000000 +0000
@@ -977,10 +977,7 @@
         rotation_gates = []
 
         for observable in self.observables:
-            try:
-                rotation_gates.extend(observable.diagonalizing_gates())
-            except NotImplementedError:
-                pass
+            rotation_gates.extend(observable.diagonalizing_gates())
 
         return rotation_gates
 
