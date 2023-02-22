--- strawberryfields/strawberryfields#27/after/ops.py	2022-01-10 16:02:54.000000000 +0000
+++ strawberryfields/strawberryfields#27/before/ops.py	2022-01-10 16:02:54.000000000 +0000
@@ -293,7 +293,7 @@
         r = tf.expand_dims(r, -1)
     t = tf.cast(tf.reshape(t, [-1, 1, 1, 1, 1, 1]), def_type)
     r = tf.cast(tf.reshape(r, [-1, 1, 1, 1, 1, 1]), def_type)
-    mag_t = tf.cast(t, tf.float32)
+    mag_t = tf.abs(t)
     mag_r = tf.abs(r)
     phase_r = tf.atan2(tf.imag(r), tf.real(r))
 
