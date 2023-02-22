--- qiskit-ignis/qiskit-ignis#567/after/fitters.py	2022-01-10 16:02:54.000000000 +0000
+++ qiskit-ignis/qiskit-ignis#567/before/fitters.py	2022-01-10 16:02:54.000000000 +0000
@@ -159,48 +159,35 @@
 
         return S
 
-    def get_error_probs(self, results):
+    def weight_syndrome_graph(self, results):
 
         results = results['0']
-        shots = sum(results.values())
 
-        error_probs = {}
-        for edge in self.S.edge_list():
+        count = {element: {edge: 0 for edge in self.S.edges}
+                 for element in ['00', '01', '10', '11']}
 
-            av_vv = 0  # v_ij
-            av_v = [0, 0]  # [v_,v_j]
-            av_xor = 0  # v_{i xor j}
-
-            for string in results:
-
-                error_nodes = self._string2nodes(string)
-                v = [int(self.S[edge[k]] in error_nodes) for k in range(2)]
-                av_vv += v[0]*v[1]*results[string]
-                for k in range(2):
-                    av_v[k] += v[k]*results[string]
-                av_xor += (v[0] != v[1])*results[string]
-            av_vv /= shots
-            av_v[0] /= shots
-            av_v[1] /= shots
-            av_xor /= shots
-            if (1 - 2*av_xor) != 0:
-                x = (av_vv - av_v[0]*av_v[1])/(1 - 2*av_xor)
-            else:
-                x = np.nan
-            error_probs[self.S[edge[0]], self.S[edge[1]]] = max(0, 0.5 - np.sqrt(0.25-x))
-        return error_probs
-    def weight_syndrome_graph(self, results):
-        error_probs = self.get_error_probs(results)
+        for string in results:
+
+            nodes = self._string2nodes(string)
+
+            for edge in self.S.edge_list():
+                element = ''
+                for j in range(2):
+                    if edge[j] in nodes:
+                        element += '1'
+                    else:
+                        element += '0'
+                count[element][edge] += results[string]
 
         for edge in self.S.edge_list():
-            p = error_probs[self.S[edge[0]], self.S[edge[1]]]
-            if p == 0:
-                w = np.inf
-            elif 1-p == 1:
-                w = -np.inf
-            else:
-                w = -np.log(p/(1-p))
-            self.S.update_edge(edge[0], edge[1], w)
+            ratios = []
+            for elements in [('00', '11'), ('11', '00'),
+                             ('01', '10'), ('10', '01')]:
+                if count[elements[1]][edge] > 0:
+                    ratio = count[elements[0]][edge]/count[elements[1]][edge]
+                    ratios.append(ratio)
+            self.S.remove_edge(edge[0], edge[1])
+            self.S.add_edge(edge[0], edge[1], -np.log(min(ratios)))
 
     def make_error_graph(self, string, subgraphs=None):
         """
