--- ProjectQ/ProjectQ#383/after/setup.py	2022-01-10 16:02:54.000000000 +0000
+++ ProjectQ/ProjectQ#383/before/setup.py	2022-01-10 16:02:54.000000000 +0000
@@ -370,9 +370,10 @@
             cxx_standards = [year for year in cxx_standards if year < 17]
 
         if sys.platform == 'darwin':
-            major_version = int(platform.mac_ver()[0].split('.')[0])
-            minor_version = int(platform.mac_ver()[0].split('.')[1])
-            if major_version <= 10 and minor_version < 14:
+            _, minor_version, _ = [
+                int(i) for i in platform.mac_ver()[0].split('.')
+            ]
+            if minor_version < 14:
                 cxx_standards = [year for year in cxx_standards if year < 17]
 
         for year in cxx_standards:
