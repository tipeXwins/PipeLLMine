--- BuggyCodes/shortest_path_lengths.py	2022-08-29 18:38:22.000000000 +0100
+++ CorrectCodes/shortest_path_lengths.py	2022-08-29 18:38:22.000000000 +0100
@@ -1,3 +1,4 @@
+
 from collections import defaultdict
 
 def shortest_path_lengths(n, length_by_edge):
@@ -10,29 +11,8 @@
             for j in range(n):
                 length_by_path[i, j] = min(
                     length_by_path[i, j],
-                    length_by_path[i, k] + length_by_path[j, k]
+                    length_by_path[i, k] + length_by_path[k, j]
                 )
 
     return length_by_path
 
-
-"""
-All Shortest Paths
-floyd-warshall
-
-Floyd-Warshall algorithm implementation.
-
-Calculates the length of the shortest path connecting every ordered pair of nodes in a directed graph.
-
-
-
-Input:
-    n: The number of nodes in the graph. The nodes are assumed to have ids 0..n-1
-    length_by_edge: A dict containing edge length keyed by an ordered pair of node ids
-
-Precondition:
-    There are no negative-length cycles in the input graph
-
-Output:
-    A dict containing shortest path length keyed by an ordered pair of node ids
-"""
