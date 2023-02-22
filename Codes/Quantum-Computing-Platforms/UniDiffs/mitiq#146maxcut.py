--- mitiq/mitiq#146/after/maxcut.py	2022-01-10 16:02:54.000000000 +0000
+++ mitiq/mitiq#146/before/maxcut.py	2022-01-10 16:02:54.000000000 +0000
@@ -79,7 +79,7 @@
         return init_state_prog + qaoa_steps
 
     # make the cost observable
-    identity = np.eye(2 ** len(nodes))
+    identity = np.eye(len(nodes) ** 2)
     cost_mat = -0.5 * sum(identity - Circuit(
                     [id(*qreg), ZZ(qreg[i], qreg[j])]).unitary()
                 for i, j in graph)
