--- mitiq/mitiq#425/after/guide-getting-started.rst	2022-01-10 16:02:54.000000000 +0000
+++ mitiq/mitiq#425/before/guide-getting-started.rst	2022-01-10 16:02:54.000000000 +0000
@@ -221,8 +221,6 @@
             optimization_level=0,
             noise_model=noise_model,
             shots=shots,
-            seed_transpiler=1,
-            seed_simulator=1
         )
         results = job.result()
         counts = results.get_counts()
@@ -246,7 +244,8 @@
     exact = 1
     print(abs(exact - mitigated) < abs(exact - unmitigated))
 
-    assert abs(exact - mitigated) < abs(exact - unmitigated)
+.. testoutput::
+    True
 
 Note that we don't need to even redefine factories for different stacks. Once
 you have a ``Factory`` it can be used with different front and backends.
