--- BuggyCodes/shortest_path_length.py	2022-08-29 18:38:22.000000000 +0100
+++ CorrectCodes/shortest_path_length.py	2022-08-29 18:38:22.000000000 +0100
@@ -19,7 +19,7 @@
             insert_or_update(unvisited_nodes,
                 (min(
                     get(unvisited_nodes, nextnode) or float('inf'),
-                    get(unvisited_nodes, nextnode) + length_by_edge[node, nextnode]
+                    distance + length_by_edge[node, nextnode]
                 ),
                 nextnode)
             )
