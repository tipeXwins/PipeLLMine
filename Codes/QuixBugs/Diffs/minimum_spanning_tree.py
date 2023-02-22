12c12
<                 group_by_node[node].update(group_by_node[u])
---
>                 group_by_node[node] = group_by_node[u]
16,42d15
< 
< 
< 
< """
< Minimum Spanning Tree
< 
< 
< Kruskal's algorithm implementation.
< 
< Input:
<     weight_by_edge: A dict of the form {(u, v): weight} for every undirected graph edge {u, v}
< 
< Precondition:
<     The input graph is connected
< 
< Output:
<     A set of edges that connects all the vertices of the input graph and has the least possible total weight.
< 
< Example:
<     >>> minimum_spanning_tree({
<     ...     (1, 2): 10,
<     ...     (2, 3): 15,
<     ...     (3, 4): 10,
<     ...     (1, 4): 10
<     ... })
<     {(1, 2), (3, 4), (1, 4)}
< """
