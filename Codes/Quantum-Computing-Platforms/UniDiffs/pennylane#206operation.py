--- pennylane/pennylane#206/after/operation.py	2022-01-10 16:02:54.000000000 +0000
+++ pennylane/pennylane#206/before/operation.py	2022-01-10 16:02:54.000000000 +0000
@@ -373,7 +373,7 @@
         """
         w = [i.val if isinstance(i, Variable) else i for i in self._wires]
         self.check_wires(w)
-        return [int(i) for i in w]
+        return w
 
     @property
     def parameters(self):
