0a1
> 
9c10
<                 dp[i, j] = dp[i - 1, j] + 1
---
>                 dp[i, j] = dp[i - 1, j - 1] + 1
12,31d12
< 
< 
< 
< """
< Longest Common Substring
< longest-common-substring
< 
< Input:
<     s: a string
<     t: a string
< 
< Output:
<     Length of the longest substring common to s and t
< 
< Example:
<     >>> lcs_length('witch', 'sandwich')
<     2
<     >>> lcs_length('meow', 'homeowner')
<     4
< """
