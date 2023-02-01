14c14
<             longest = length + 1
---
>             longest = max(longest, length + 1)
18,19d17
< 
< 
21,22c19,21
< Longest Increasing Subsequence
< longest-increasing-subsequence
---
> def lis(arr):
>     ends = {}
>     longest = 0
23a23
>     for i, val in enumerate(arr):
25,26c25
< Input:
<     arr: A sequence of ints
---
>         prefix_lengths = [j for j in range(1, longest + 1) if arr[ends[j]] < val]
28,29c27
< Precondition:
<     The ints in arr are unique
---
>         length = max(prefix_lengths) if prefix_lengths else 0
31,32c29,31
< Output:
<     The length of the longest monotonically increasing subsequence of arr
---
>         if length == longest or val < arr[ends[length + 1]]:
>             ends[length + 1] = i
>             longest = max(length + 1, longest)
34,36c33
< Example:
<     >>> lis([4, 1, 5, 3, 7, 6, 2])
<     3
---
>     return longest
