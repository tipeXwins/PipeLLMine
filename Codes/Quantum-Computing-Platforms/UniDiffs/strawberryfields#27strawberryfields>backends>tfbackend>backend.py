--- strawberryfields/strawberryfields#27/after/strawberryfields>backends>tfbackend>backend.py	2022-01-10 16:02:54.000000000 +0000
+++ strawberryfields/strawberryfields#27/before/strawberryfields>backends>tfbackend>backend.py	2022-01-10 16:02:54.000000000 +0000
@@ -293,11 +293,6 @@
 
     def beamsplitter(self, t, r, mode1, mode2):
         with tf.name_scope('Beamsplitter'):
-            if isinstance(t, complex):
-                raise ValueError("Beamsplitter transmittivity t must be a float.")
-            if isinstance(t, tf.Tensor):
-                if t.dtype.is_complex:
-                    raise ValueError("Beamsplitter transmittivity t must be a float.")
             remapped_modes = self._remap_modes([mode1, mode2])
             self.circuit.beamsplitter(t, r, remapped_modes[0], remapped_modes[1])
 
