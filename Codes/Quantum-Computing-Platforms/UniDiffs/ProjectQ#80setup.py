--- ProjectQ/ProjectQ#80/after/setup.py	2022-01-10 16:02:54.000000000 +0000
+++ ProjectQ/ProjectQ#80/before/setup.py	2022-01-10 16:02:54.000000000 +0000
@@ -143,7 +143,7 @@
             self.warning("")
 
     def warning(self, warning_text):
-        raise Exception(warning_text + "\nCould not install the C++-Simulator.\n"
+        Exception(warning_text + "\nCould not install the C++-Simulator.\n"
                   "ProjectQ will default to the (slow) Python simulator.\n"
                   "Use --without-cppsimulator to skip building the (faster) "
                   "C++ version of the simulator.")
