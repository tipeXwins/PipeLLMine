0a1
> 
3c4
<         return []
---
>         return [[]]
12,30d12
< 
< 
< """
< Subsequences
< 
< 
< Input:
<     a: An int
<     b: An int
<     k: A positive int
< 
< Output:
<     A list of all length-k ascending sequences of ints in range(a, b)
< 
< Example:
<     >>> subsequences(a=1, b=5, k=3)
<     [[1, 2, 3], [1, 2, 4], [1, 3, 4], [2, 3, 4]]
< """
< 
