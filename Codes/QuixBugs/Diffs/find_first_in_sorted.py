0a1
> 
5c6
<     while lo <= hi:
---
>     while lo < hi:
19d19
< 
21,22c21,35
< Fancy Binary Search
< fancy-binsearch
---
> def find_first_in_sorted(arr, x):
>     lo = 0
>     hi = len(arr)
> 
>     while lo <= hi - 1:
>         mid = (lo + hi) // 2
> 
>         if x == arr[mid] and (mid == 0 or x != arr[mid - 1]):
>             return mid
> 
>         elif x <= arr[mid]:
>             hi = mid
> 
>         else:
>             lo = mid + 1
23a37,50
>     return -1
> 
> def find_first_in_sorted(arr, x):
>     lo = 0
>     hi = len(arr)
> 
>     while lo + 1 <= hi:
>         mid = (lo + hi) // 2
> 
>         if x == arr[mid] and (mid == 0 or x != arr[mid - 1]):
>             return mid
> 
>         elif x <= arr[mid]:
>             hi = mid
25,27c52,53
< Input:
<     arr: A sorted list of ints
<     x: A value to find
---
>         else:
>             lo = mid + 1
29,30c55
< Output:
<     The lowest index i such that arr[i] == x, or -1 if x not in arr
---
>     return -1
32,34d56
< Example:
<     >>> find_first_in_sorted([3, 4, 5, 5, 5, 5, 6], 5)
<     2
