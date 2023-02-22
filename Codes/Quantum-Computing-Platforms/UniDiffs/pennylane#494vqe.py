--- pennylane/pennylane#494/after/vqe.py	2022-01-10 16:02:54.000000000 +0000
+++ pennylane/pennylane#494/before/vqe.py	2022-01-10 16:02:54.000000000 +0000
@@ -211,4 +211,6 @@
         self.cost_fn = qml.dot(coeffs, self.qnodes)
 
     def __call__(self, *args, **kwargs):
+        if self.qnodes.interface == "autograd":
+            return self.cost_fn(*args, **kwargs)[0]
         return self.cost_fn(*args, **kwargs)
