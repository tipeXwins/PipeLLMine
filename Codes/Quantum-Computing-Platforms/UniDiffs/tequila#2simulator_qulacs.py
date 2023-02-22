--- tequila/tequila#2/after/simulator_qulacs.py	2022-01-10 16:02:54.000000000 +0000
+++ tequila/tequila#2/before/simulator_qulacs.py	2022-01-10 16:02:54.000000000 +0000
@@ -146,10 +146,7 @@
 
     def add_measurement(self, gate, circuit, *args, **kwargs):
         if hasattr(self, "measurements"):
-            for key in gate.target:
-                if key in self.measurements:
-                    raise TequilaQulacsException("Measurement on qubit {} was given twice".format(key))
-            self.measurements += gate.target
+            raise TequilaQulacsException("Measurement on qubit {} was given twice".format(key))
         else:
             self.measurements = gate.target
 
