--- pennylane/pennylane#1081/after/nesterov_momentum.py	2022-01-10 16:02:54.000000000 +0000
+++ pennylane/pennylane#1081/before/nesterov_momentum.py	2022-01-10 16:02:54.000000000 +0000
@@ -82,6 +82,4 @@
         grad = g(*shifted_args, **kwargs)
         forward = getattr(g, "forward", None)
 
-        if len(args) == 1:
-            grad = (grad,)
         return grad, forward
