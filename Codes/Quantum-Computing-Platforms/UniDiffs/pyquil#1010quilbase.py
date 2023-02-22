--- pyquil/pyquil#1010/after/quilbase.py	2022-01-10 16:02:54.000000000 +0000
+++ pyquil/pyquil#1010/before/quilbase.py	2022-01-10 16:02:54.000000000 +0000
@@ -736,9 +736,8 @@
     def __init__(self, target, left, right):
         if not isinstance(left, MemoryReference):
             raise TypeError("left operand should be an MemoryReference")
-        if not (isinstance(right, MemoryReference) or isinstance(right, int)
-                or isinstance(right, float)):
-            raise TypeError("right operand should be an MemoryReference or an int or float.")
+        if not isinstance(right, MemoryReference):
+            raise TypeError("right operand should be an MemoryReference")
         self.target = target
         self.left = left
         self.right = right
