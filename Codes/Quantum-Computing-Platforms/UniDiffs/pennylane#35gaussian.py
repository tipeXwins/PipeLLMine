--- pennylane/pennylane#35/after/gaussian.py	2022-01-10 16:02:54.000000000 +0000
+++ pennylane/pennylane#35/before/gaussian.py	2022-01-10 16:02:54.000000000 +0000
@@ -35,7 +35,7 @@
 
 operator_map = {
     'CoherentState': Coherent,
-    'DisplacedSqueezedState': DisplacedSqueezed,
+    'DisplacedSqueezed': DisplacedSqueezed,
     'SqueezedState': Squeezed,
     'ThermalState': Thermal,
     'GaussianState': Gaussian,
