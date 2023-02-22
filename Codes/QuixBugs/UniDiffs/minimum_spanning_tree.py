--- BuggyCodes/minimum_spanning_tree.py	2022-08-29 18:38:22.000000000 +0100
+++ CorrectCodes/minimum_spanning_tree.py	2022-08-29 18:38:22.000000000 +0100
@@ -9,34 +9,7 @@
             mst_edges.add(edge)
             group_by_node[u].update(group_by_node[v])
             for node in group_by_node[v]:
-                group_by_node[node].update(group_by_node[u])
+                group_by_node[node] = group_by_node[u]
 
     return mst_edges
 
-
-
-
-"""
-Minimum Spanning Tree
-
-
-Kruskal's algorithm implementation.
-
-Input:
-    weight_by_edge: A dict of the form {(u, v): weight} for every undirected graph edge {u, v}
-
-Precondition:
-    The input graph is connected
-
-Output:
-    A set of edges that connects all the vertices of the input graph and has the least possible total weight.
-
-Example:
-    >>> minimum_spanning_tree({
-    ...     (1, 2): 10,
-    ...     (2, 3): 15,
-    ...     (3, 4): 10,
-    ...     (1, 4): 10
-    ... })
-    {(1, 2), (3, 4), (1, 4)}
-"""
