--- dwave-system/dwave-system#373/after/leap_hybrid_sampler.py	2022-01-10 16:02:54.000000000 +0000
+++ dwave-system/dwave-system#373/before/leap_hybrid_sampler.py	2022-01-10 16:02:54.000000000 +0000
@@ -93,7 +93,7 @@
                 raise ValueError("the only problem type this sampler supports is 'bqm'")
 
             # prefer the latest version, but allow kwarg override
-            solver.setdefault('order_by', '-properties.version')
+            solver.setdefault('order_by', '-version')
 
         self.client = Client.from_config(
             solver=solver, connection_close=connection_close, **config)
@@ -331,7 +331,7 @@
                 raise ValueError("the only problem type this sampler supports is 'dqm'")
 
             # prefer the latest version, but allow kwarg override
-            solver.setdefault('order_by', '-properties.version')
+            solver.setdefault('order_by', '-version')
 
         self.client = Client.from_config(
             solver=solver, connection_close=connection_close, **config)
