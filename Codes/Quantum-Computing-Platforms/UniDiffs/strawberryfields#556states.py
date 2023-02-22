--- strawberryfields/strawberryfields#556/after/states.py	2022-01-10 16:02:54.000000000 +0000
+++ strawberryfields/strawberryfields#556/before/states.py	2022-01-10 16:02:54.000000000 +0000
@@ -305,8 +305,8 @@
 
     # coherent states
     k = np.arange(fock_dim)
-    c1 = ((1.0 * a) ** k) / np.sqrt(fac(k))
-    c2 = ((-1.0 * a) ** k) / np.sqrt(fac(k))
+    c1 = (a ** k) / np.sqrt(fac(k))
+    c2 = ((-a) ** k) / np.sqrt(fac(k))
 
     # add them up with a relative phase
     ket = (c1 + np.exp(1j * phi) * c2) * N
