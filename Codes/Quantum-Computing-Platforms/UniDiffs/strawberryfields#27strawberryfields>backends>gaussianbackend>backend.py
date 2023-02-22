--- strawberryfields/strawberryfields#27/after/strawberryfields>backends>gaussianbackend>backend.py	2022-01-10 16:02:54.000000000 +0000
+++ strawberryfields/strawberryfields#27/before/strawberryfields>backends>gaussianbackend>backend.py	2022-01-10 16:02:54.000000000 +0000
@@ -181,8 +181,6 @@
         self.circuit.displace(alpha, mode)
 
     def beamsplitter(self, t, r, mode1, mode2):
-        if isinstance(t, complex):
-            raise ValueError("Beamsplitter transmittivity t must be a float.")
         theta = arctan2(abs(r), t)
         phi = angle(r)
         self.circuit.beamsplitter(-theta, -phi, mode1, mode2)
