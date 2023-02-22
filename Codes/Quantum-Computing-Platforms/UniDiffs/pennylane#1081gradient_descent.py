--- pennylane/pennylane#1081/after/gradient_descent.py	2022-01-10 16:02:54.000000000 +0000
+++ pennylane/pennylane#1081/before/gradient_descent.py	2022-01-10 16:02:54.000000000 +0000
@@ -127,8 +127,6 @@
         grad = g(*args, **kwargs)
         forward = getattr(g, "forward", None)
 
-        if len(args) == 1:
-            grad = (grad,)
         return grad, forward
 
     def apply_grad(self, grad, args):
