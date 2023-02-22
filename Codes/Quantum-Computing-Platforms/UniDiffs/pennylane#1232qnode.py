--- pennylane/pennylane#1232/after/qnode.py	2022-01-10 16:02:54.000000000 +0000
+++ pennylane/pennylane#1232/before/qnode.py	2022-01-10 16:02:54.000000000 +0000
@@ -573,9 +573,7 @@
             if hasattr(self._original_device, "_state"):
                 self._original_device._state = self.device._state
 
-        if isinstance(self.qfunc_output, Sequence) or (
-            self.qtape.is_sampled and self.device._has_partitioned_shots()
-        ):
+        if isinstance(self.qfunc_output, Sequence):
             return res
 
         return qml.math.squeeze(res)
