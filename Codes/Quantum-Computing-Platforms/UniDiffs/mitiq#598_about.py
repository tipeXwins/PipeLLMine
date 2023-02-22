--- mitiq/mitiq#598/after/_about.py	2022-01-10 16:02:54.000000000 +0000
+++ mitiq/mitiq#598/before/_about.py	2022-01-10 16:02:54.000000000 +0000
@@ -41,8 +41,7 @@
     except ImportError:
         pyquil_version = "Not installed"
     try:
-        from qiskit import __qiskit_version__
-        qiskit_version = __qiskit_version__["qiskit"]
+        from qiskit import __version__ as qiskit_version
     except ImportError:
         qiskit_version = "Not installed"
 
