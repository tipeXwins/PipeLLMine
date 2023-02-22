--- qiskit-aer/qiskit-aer#167/after/aerbackend.py	2022-01-10 16:02:54.000000000 +0000
+++ qiskit-aer/qiskit-aer#167/before/aerbackend.py	2022-01-10 16:02:54.000000000 +0000
@@ -156,7 +156,7 @@
         if not output.get("success", False):
             logger.error("%s: simulation failed", self.name())
             # Check for error message in the failed circuit
-            for res in output.get('results', []):
+            for res in output.get('results'):
                 if not res.get('success', False):
                     raise AerError(res.get("status", None))
             # If no error was found check for error message at qobj level
