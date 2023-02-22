--- pennylane/pennylane#946/after/default_qubit_tf.py	2022-01-10 16:02:54.000000000 +0000
+++ pennylane/pennylane#946/before/default_qubit_tf.py	2022-01-10 16:02:54.000000000 +0000
@@ -156,7 +156,7 @@
     _transpose = staticmethod(tf.transpose)
     _tensordot = staticmethod(tf.tensordot)
     _conj = staticmethod(tf.math.conj)
-    _imag = staticmethod(tf.math.imag)
+    _imag = staticmethod(tf.math.conj)
     _roll = staticmethod(tf.roll)
     _stack = staticmethod(tf.stack)
 
