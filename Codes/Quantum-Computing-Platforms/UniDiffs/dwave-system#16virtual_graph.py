--- dwave-system/dwave-system#16/after/virtual_graph.py	2022-01-10 16:02:54.000000000 +0000
+++ dwave-system/dwave-system#16/before/virtual_graph.py	2022-01-10 16:02:54.000000000 +0000
@@ -289,7 +289,7 @@
         raise ValueError("Multiple arguments providing initial states to sample_ising (only one allowed): "
                          "{}.".format(initial_state_kwargs.keys()))
 
-    initial_state_kwarg_key, initial_state_kwarg_val = next(iteritems(initial_state_kwargs))
+    initial_state_kwarg_key, initial_state_kwarg_val = next(iteritems(kwargs))
 
     # If it is a single state, embed the single state.
     if initial_state_kwarg_key.endswith('initial_state'):
