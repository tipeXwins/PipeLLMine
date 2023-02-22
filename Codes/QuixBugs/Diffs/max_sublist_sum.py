7c7
<         max_ending_here = max_ending_here + x
---
>         max_ending_here = max(0, max_ending_here + x)
12d11
< 
14,15c13,19
< Max Sublist Sum
< max-sublist-sum
---
> def max_sublist_sum(arr):
>     max_ending_here = 0
>     max_so_far = 0
> 
>     for x in arr:
>         max_ending_here = max(max_ending_here + x, 0)
>         max_so_far = max(max_so_far, max_ending_here)
17c21
< Efficient equivalent to max(sum(arr[i:j]) for 0 <= i <= j <= len(arr))
---
>     return max_so_far
19c23,25
< Algorithm source: WordAligned.org by Thomas Guest
---
> def max_sublist_sum(arr):
>     max_ending_here = 0
>     max_so_far = 0
20a27,29
>     for x in arr:
>         max_ending_here = max(x, max_ending_here + x)
>         max_so_far = max(max_so_far, max_ending_here)
22,23c31
< Input:
<     arr: A list of ints
---
>     return max_so_far
25,26d32
< Output:
<     The maximum sublist sum
28,30c34,43
< Example:
<     >>> max_sublist_sum([4, -5, 2, 1, -1, 3])
<     5
---
> def max_sublist_sum(arr):
>     max_ending_here = 0
>     max_so_far = 0
> 
>     for x in arr:
>         max_ending_here = max(max_ending_here + x, x)
>         max_so_far = max(max_so_far, max_ending_here)
> 
>     return max_so_far
> 
