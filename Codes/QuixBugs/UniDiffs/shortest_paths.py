--- BuggyCodes/shortest_paths.py	2022-08-29 18:38:22.000000000 +0100
+++ CorrectCodes/shortest_paths.py	2022-08-29 18:38:22.000000000 +0100
@@ -7,42 +7,10 @@
 
     for i in range(len(weight_by_node) - 1):
         for (u, v), weight in weight_by_edge.items():
-            weight_by_edge[u, v] = min(
+            weight_by_node[v] = min(
                 weight_by_node[u] + weight,
                 weight_by_node[v]
             )
 
     return weight_by_node
 
-
-"""
-Minimum-Weight Paths
-bellman-ford
-
-Bellman-Ford algorithm implementation
-
-Given a directed graph that may contain negative edges (as long as there are no negative-weight cycles), efficiently calculates the minimum path weights from a source node to every other node in the graph.
-
-Input:
-    source: A node id
-    weight_by_edge: A dict containing edge weights keyed by an ordered pair of node ids
-
-Precondition:
-    The input graph contains no negative-weight cycles
-
-Output:
-   A dict mapping each node id to the minimum weight of a path from the source node to that node
-
-Example:
-    >>> shortest_paths('A', {
-        ('A', 'B'): 3,
-        ('A', 'C'): 3,
-        ('A', 'F'): 5,
-        ('C', 'B'): -2,
-        ('C', 'D'): 7,
-        ('C', 'E'): 4,
-        ('D', 'E'): -5,
-        ('E', 'F'): -1
-    })
-    {'A': 0, 'C': 3, 'B': 1, 'E': 5, 'D': 10, 'F': 4}
-"""
