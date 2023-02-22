--- strawberryfields/strawberryfields#507/after/ops.py	2022-01-10 16:02:54.000000000 +0000
+++ strawberryfields/strawberryfields#507/before/ops.py	2022-01-10 16:02:54.000000000 +0000
@@ -594,10 +594,9 @@
         r = par_evaluate(self.p[0])
         phi = par_evaluate(self.p[1])
 
-        np_args = [arg.numpy() if hasattr(arg, "numpy") else arg for arg in [r, phi]]
-        is_complex = any([np.iscomplexobj(np.real_if_close(arg)) for arg in np_args])
+        tf_complex = any(hasattr(arg, "numpy") and np.iscomplex(arg.numpy()) for arg in [r, phi])
 
-        if is_complex:
+        if (np.iscomplex([r, phi])).any() or tf_complex:
             raise ValueError("The arguments of Coherent(r, phi) cannot be complex")
 
         backend.prepare_coherent_state(r, phi, *reg)
@@ -723,10 +722,11 @@
     def _apply(self, reg, backend, **kwargs):
         p = par_evaluate(self.p)
 
-        np_args = [arg.numpy() if hasattr(arg, "numpy") else arg for arg in p]
-        is_complex = any([np.iscomplexobj(np.real_if_close(arg)) for arg in np_args])
+        tf_complex = any(
+            hasattr(arg, "numpy") and np.iscomplex(arg.numpy()) for arg in [p[0], p[1], p[2], p[3]]
+        )
 
-        if is_complex:
+        if (np.iscomplex([p[0], p[1], p[2], p[3]])).any() or tf_complex:
             raise ValueError(
                 "The arguments of DisplacedSqueezed(r_d, phi_d, r_s, phi_s) cannot be complex"
             )
@@ -1337,10 +1337,9 @@
     def _apply(self, reg, backend, **kwargs):
         r, phi = par_evaluate(self.p)
 
-        np_args = [arg.numpy() if hasattr(arg, "numpy") else arg for arg in [r, phi]]
-        is_complex = any([np.iscomplexobj(np.real_if_close(arg)) for arg in np_args])
+        tf_complex = any(hasattr(arg, "numpy") and np.iscomplex(arg.numpy()) for arg in [r, phi])
 
-        if is_complex:
+        if (np.iscomplex([r, phi])).any() or tf_complex:
             raise ValueError("The arguments of Dgate(r, phi) cannot be complex")
 
         backend.displacement(r, phi, *reg)
