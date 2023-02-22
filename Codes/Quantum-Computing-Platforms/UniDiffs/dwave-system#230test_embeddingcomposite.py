--- dwave-system/dwave-system#230/after/test_embeddingcomposite.py	2022-01-10 16:02:54.000000000 +0000
+++ dwave-system/dwave-system#230/before/test_embeddingcomposite.py	2022-01-10 16:02:54.000000000 +0000
@@ -27,8 +27,7 @@
     @classmethod
     def setUpClass(cls):
         try:
-            cls.qpu = DWaveSampler(solver=dict(
-                qpu=True, initial_state=True, anneal_schedule=True))
+            cls.qpu = DWaveSampler(solver=dict(qpu=True, initial_state=True))
         except (ValueError, ConfigFileError):
             raise unittest.SkipTest("no qpu available")
 
