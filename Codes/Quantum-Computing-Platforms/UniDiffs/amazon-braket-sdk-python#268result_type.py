--- amazon-braket-sdk-python/amazon-braket-sdk-python#268/after/result_type.py	2022-01-10 16:02:54.000000000 +0000
+++ amazon-braket-sdk-python/amazon-braket-sdk-python#268/before/result_type.py	2022-01-10 16:02:54.000000000 +0000
@@ -69,9 +69,7 @@
         """
         raise NotImplementedError("to_ir has not been implemented yet.")
 
-    def copy(
-        self, target_mapping: Dict[QubitInput, QubitInput] = None, target: QubitSetInput = None
-    ):
+    def copy(self, target_mapping: Dict[QubitInput, QubitInput] = {}, target: QubitSetInput = None):
         """
         Return a shallow copy of the result type.
 
@@ -110,8 +108,9 @@
         elif target is not None:
             if hasattr(copy, "target"):
                 copy.target = target
-        elif hasattr(copy, "target"):
-            copy.target = self._target.map(target_mapping or {})
+        else:
+            if hasattr(copy, "target"):
+                copy.target = self._target.map(target_mapping)
         return copy
 
     @classmethod
