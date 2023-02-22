--- strawberryfields/strawberryfields#556/after/ops.py	2022-01-10 16:02:54.000000000 +0000
+++ strawberryfields/strawberryfields#556/before/ops.py	2022-01-10 16:02:54.000000000 +0000
@@ -867,8 +867,8 @@
         N = temp / pf.sqrt(2 * (1 + pf.cos(phi) * temp ** 4))
 
         # coherent states
-        c1 = ((1.0 * alpha) ** l) / np.sqrt(ssp.factorial(l))
-        c2 = ((-1.0 * alpha) ** l) / np.sqrt(ssp.factorial(l))
+        c1 = (alpha ** l) / np.sqrt(ssp.factorial(l))
+        c2 = ((-alpha) ** l) / np.sqrt(ssp.factorial(l))
         # add them up with a relative phase
         ket = (c1 + pf.exp(1j * phi) * c2) * N
 
