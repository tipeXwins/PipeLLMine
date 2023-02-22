5c5
<         n ^= n - 1
---
>         n &= n - 1
8,26d7
< 
< 
< """
< Bitcount
< bitcount
< 
< 
< Input:
<     n: a nonnegative int
< 
< Output:
<     The number of 1-bits in the binary encoding of n
< 
< Examples:
<     >>> bitcount(127)
<     7
<     >>> bitcount(128)
<     1
< """
