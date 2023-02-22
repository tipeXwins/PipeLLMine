--- pennylane/pennylane#1081/after/_grad.py	2022-01-10 16:02:54.000000000 +0000
+++ pennylane/pennylane#1081/before/_grad.py	2022-01-10 16:02:54.000000000 +0000
@@ -85,8 +85,6 @@
             if getattr(arg, "requires_grad", True):
                 argnum.append(idx)
 
-        if len(argnum) == 1:
-            argnum = argnum[0]
         return self._grad_with_forward(
             self._fun,
             argnum=argnum,
