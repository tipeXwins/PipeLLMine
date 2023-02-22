5c5
<         if hare.successor is None:
---
>         if hare is None or hare.successor is None:
15d14
< 
17,18c16,17
< Linked List Cycle Detection
< tortoise-hare
---
> def detect_cycle(node):
>     hare = tortoise = node
20c19,21
< Implements the tortoise-and-hare method of cycle detection.
---
>     while True:
>         if hare.successor is None or hare.successor.successor is None:
>             return False
22,23c23,24
< Input:
<     node: The head node of a linked list
---
>         tortoise = tortoise.successor
>         hare = hare.successor.successor
25,26c26,27
< Output:
<     Whether the linked list is cyclic
---
>         if hare is tortoise:
>             return True
