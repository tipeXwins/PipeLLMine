--- dwave-system/dwave-system#422/after/leap_hybrid_sampler.py	2022-01-10 16:02:54.000000000 +0000
+++ dwave-system/dwave-system#422/before/leap_hybrid_sampler.py	2022-01-10 16:02:54.000000000 +0000
@@ -32,30 +32,28 @@
 __all__ = ['LeapHybridSampler', 'LeapHybridDQMSampler']
 
 
-class classproperty(property):
-    def __get__(self, obj, objtype=None):
-        return super(classproperty, self).__get__(objtype)
 class LeapHybridSampler(dimod.Sampler):
     
 
     _INTEGER_BQM_SIZE_THRESHOLD = 10000
 
-    @classproperty
-    def default_solver(cls):
-        return dict(supported_problem_types__contains='bqm',
-                    order_by='-properties.version')
+    def __init__(self, solver=None, connection_close=True, **config):
 
-    def __init__(self, **config):
+        # we want a Hybrid solver by default, but allow override
         config.setdefault('client', 'hybrid')
 
-        config.setdefault('connection_close', True)
+        if solver is None:
+            solver = {}
 
-        defaults = config.setdefault('defaults', {})
-        if not isinstance(defaults, abc.Mapping):
-            raise TypeError("mapping expected for 'defaults'")
-        defaults.update(solver=self.default_solver)
-
-        self.client = Client.from_config(**config)
+        if isinstance(solver, abc.Mapping):
+            if solver.setdefault('category', 'hybrid') != 'hybrid':
+                raise ValueError("the only 'category' this sampler supports is 'hybrid'")
+            if solver.setdefault('supported_problem_types__contains', 'bqm') != 'bqm':
+                raise ValueError("the only problem type this sampler supports is 'bqm'")
+
+            solver.setdefault('order_by', '-properties.version')
+        self.client = Client.from_config(
+            solver=solver, connection_close=connection_close, **config)
         self.solver = self.client.get_solver()
 
         if self.properties.get('category') != 'hybrid':
@@ -195,23 +193,25 @@
 class LeapHybridDQMSampler:
     
 
-    @classproperty
-    def default_solver(self):
-        return dict(supported_problem_types__contains='dqm',
-                    order_by='-properties.version')
-
-    def __init__(self, **config):
+    def __init__(self, solver=None, connection_close=True, **config):
 
         config.setdefault('client', 'hybrid')
 
-        config.setdefault('connection_close', True)
+        if solver is None:
+            solver = {}
+
+        if isinstance(solver, abc.Mapping):
+            if solver.setdefault('category', 'hybrid') != 'hybrid':
+                raise ValueError("the only 'category' this sampler supports is 'hybrid'")
+            if solver.setdefault('supported_problem_types__contains', 'dqm') != 'dqm':
+                raise ValueError("the only problem type this sampler supports is 'dqm'")
+
+            # prefer the latest version, but allow kwarg override
+            solver.setdefault('order_by', '-properties.version')
 
-        defaults = config.setdefault('defaults', {})
-        if not isinstance(defaults, abc.Mapping):
-            raise TypeError("mapping expected for 'defaults'")
-        defaults.update(solver=self.default_solver)
+        self.client = Client.from_config(
+            solver=solver, connection_close=connection_close, **config)
 
-        self.client = Client.from_config(**config)
         self.solver = self.client.get_solver()
 
         if self.properties.get('category') != 'hybrid':
