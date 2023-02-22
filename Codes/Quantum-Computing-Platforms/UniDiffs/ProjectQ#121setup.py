--- ProjectQ/ProjectQ#121/after/setup.py	2022-01-10 16:02:54.000000000 +0000
+++ ProjectQ/ProjectQ#121/before/setup.py	2022-01-10 16:02:54.000000000 +0000
@@ -113,8 +113,8 @@
         openmp = ''
         if has_flag(self.compiler, '-fopenmp'):
             openmp = '-fopenmp'
-        elif has_flag(self.compiler, '-qopenmp'):
-            openmp = '-qopenmp'
+        elif has_flag(self.compiler, '-openmp'):
+            openmp = '-openmp'
         if ct == 'msvc':
             openmp = ''  # supports only OpenMP 2.0
 
