--- pennylane/pennylane#709/after/pennylane>qnn>torch.py	2022-01-10 16:02:54.000000000 +0000
+++ pennylane/pennylane#709/before/pennylane>qnn>torch.py	2022-01-10 16:02:54.000000000 +0000
@@ -330,7 +330,7 @@
 
         for arg in self.sig:
             if arg is not self.input_arg:  # Non-input arguments must always be positional
-                w = self.qnode_weights[arg].to(x)
+                w = self.qnode_weights[arg]
 
                 qnode = functools.partial(qnode, w)
             else:
@@ -349,10 +349,7 @@
         Returns:
             tensor: output datapoint
         """
-        kwargs = {
-            **{self.input_arg: x},
-            **{arg: weight.to(x) for arg, weight in self.qnode_weights.items()},
-        }
+        kwargs = {**{self.input_arg: x}, **self.qnode_weights}
         return self.qnode(**kwargs).type(x.dtype)
 
     def __str__(self):
