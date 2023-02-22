--- tequila/tequila#176/after/qc_base.py	2022-01-10 16:02:54.000000000 +0000
+++ tequila/tequila#176/before/qc_base.py	2022-01-10 16:02:54.000000000 +0000
@@ -143,11 +143,9 @@
 
         """
         result = []
-        lines = [l for l in geometry.split("\n") if l]
-        for line in lines:
+        for line in geometry.split('\n'):
             words = line.split()
-            if len(words) < 4:
-                words += [0.0] * (4 - len(words))
+            if len(words) != 4:  break
             try:
                 tmp = (ParametersQC.format_element_name(words[0]),
                        (float(words[1]), float(words[2]), float(words[3])))
