--- pyquil/pyquil#174/after/parser.py	2022-01-10 16:02:54.000000000 +0000
+++ pyquil/pyquil#174/before/parser.py	2022-01-10 16:02:54.000000000 +0000
@@ -38,4 +38,4 @@
     :param str quil: a single or multiline Quil program
     :return: list of instructions
     """
-    return run_parser(quil.strip())
+    return run_parser(quil)
