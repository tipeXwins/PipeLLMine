--- dwave-system/dwave-system#276/after/warnings.py	2022-01-10 16:02:54.000000000 +0000
+++ dwave-system/dwave-system#276/before/warnings.py	2022-01-10 16:02:54.000000000 +0000
@@ -174,14 +174,11 @@
                                      sample_index=row),
                            )
 
-    def chain_strength(self, bqm, chain_strength, embedding=None):
+    def chain_strength(self, bqm, chain_strength):
         """Issues a warning when any quadratic biases are greater than the given
         chain strength."""
         if as_action(self.action) is IGNORE:
             return
-        if embedding is not None:
-            if not embedding or all(len(chain) <= 1 for chain in embedding.values()):
-                return
 
         interactions = [uv for uv, bias in bqm.quadratic.items()
                         if abs(bias) >= chain_strength]
