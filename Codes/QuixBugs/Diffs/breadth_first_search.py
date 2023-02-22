11c11
<     while True:
---
>     while queue:
23d22
< 
25c24,31
< Breadth-First Search
---
> from collections import deque as Queue
> 
> def breadth_first_search(startnode, goalnode):
>     queue = Queue()
>     queue.append(startnode)
> 
>     nodesseen = set()
>     nodesseen.add(startnode)
26a33,34
>     while len(queue):
>         node = queue.popleft()
28,30c36,86
< Input:
<     startnode: A digraph node
<     goalnode: A digraph node
---
>         if node is goalnode:
>             return True
>         else:
>             queue.extend(node for node in node.successors if node not in nodesseen)
>             nodesseen.update(node.successors)
> 
>     return False
> 
> 
> 
> from collections import deque as Queue
> 
> def breadth_first_search(startnode, goalnode):
>     queue = Queue()
>     queue.append(startnode)
> 
>     nodesseen = set()
>     nodesseen.add(startnode)
> 
>     while len(queue) > 0:
>         node = queue.popleft()
> 
>         if node is goalnode:
>             return True
>         else:
>             queue.extend(node for node in node.successors if node not in nodesseen)
>             nodesseen.update(node.successors)
> 
>     return False
> 
> 
> 
> from collections import deque as Queue
> 
> def breadth_first_search(startnode, goalnode):
>     queue = Queue()
>     queue.append(startnode)
> 
>     nodesseen = set()
>     nodesseen.add(startnode)
> 
>     while len(queue) != 0:
>         node = queue.popleft()
> 
>         if node is goalnode:
>             return True
>         else:
>             queue.extend(node for node in node.successors if node not in nodesseen)
>             nodesseen.update(node.successors)
> 
>     return False
32,33d87
< Output:
<     Whether goalnode is reachable from startnode
