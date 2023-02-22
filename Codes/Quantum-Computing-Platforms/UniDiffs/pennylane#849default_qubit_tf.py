--- pennylane/pennylane#849/after/default_qubit_tf.py	2022-01-10 16:02:54.000000000 +0000
+++ pennylane/pennylane#849/before/default_qubit_tf.py	2022-01-10 16:02:54.000000000 +0000
@@ -166,7 +166,7 @@
         # raise an error when calculating the gradient. For versions of TF after 2.3.0,
         # special apply methods are also not supported when using more than 8 wires due to
         # limitations with TF slicing.
-        if not SUPPORTS_APPLY_OPS or self.num_wires > 8:
+        if not SUPPORTS_APPLY_OPS or wires > 8:
             self._apply_ops = {}
 
     @classmethod
