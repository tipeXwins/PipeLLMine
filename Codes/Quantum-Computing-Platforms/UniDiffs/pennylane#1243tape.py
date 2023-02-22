--- pennylane/pennylane#1243/after/tape.py	2022-01-10 16:02:54.000000000 +0000
+++ pennylane/pennylane#1243/before/tape.py	2022-01-10 16:02:54.000000000 +0000
@@ -648,26 +648,11 @@
         self.trainable_params = {parameter_mapping[i] for i in self.trainable_params}
         self._par_info = {parameter_mapping[k]: v for k, v in self._par_info.items()}
 
-        for idx, op in enumerate(self._ops):
-            try:
-                self._ops[idx] = op.adjoint()
-            except NotImplementedError:
-                op.inverse = not op.inverse
+        for op in self._ops:
+            op.inverse = not op.inverse
 
         self._ops = list(reversed(self._ops))
 
-    def adjoint(self):
-        new_tape = self.copy(copy_operations=True)
-        qml.transforms.invisible(new_tape.inv)()
-        QuantumTape._lock.acquire()
-        try:
-            QueuingContext.append(new_tape)
-        except Exception as _:
-            QuantumTape._lock.release()
-            raise
-        QuantumTape._lock.release()
-        return new_tape
-
     # ========================================================
     # Parameter handling
     # ========================================================
