0a1
> 
6c7
<         return a[0] + longest_common_subsequence(a[1:], b)
---
>         return a[0] + longest_common_subsequence(a[1:], b[1:])
15,34d15
< 
< 
< """
< Longest Common Subsequence
< 
< 
< Calculates the longest subsequence common to the two input strings. (A subsequence is any sequence of letters in the same order
< they appear in the string, possibly skipping letters in between.)
< 
< Input:
<     a: The first string to consider.
<     b: The second string to consider.
< 
< Output:
<     The longest string which is a subsequence of both strings. (If multiple subsequences of equal length exist, either is OK.)
< 
< Example:
<     >>> longest_common_subsequence('headache', 'pentadactyl')
<     'eadac'
< """
