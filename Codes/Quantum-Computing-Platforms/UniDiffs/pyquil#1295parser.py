--- pyquil/pyquil#1295/after/parser.py	2022-01-10 16:02:54.000000000 +0000
+++ pyquil/pyquil#1295/before/parser.py	2022-01-10 16:02:54.000000000 +0000
@@ -121,7 +121,7 @@
         space = " " if qubits else ""
         if variables:
             raw_defcircuit = "DEFCIRCUIT {}({}){}{}:".format(
-                name, ", ".join(map(str, variables)), space, " ".join(map(str, qubits))
+                name, ", ".join(variables), space, " ".join(map(str, qubits))
             )
         else:
             raw_defcircuit = "DEFCIRCUIT {}{}{}:".format(name, space, " ".join(map(str, qubits)))
