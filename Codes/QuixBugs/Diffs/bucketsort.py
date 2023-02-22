0a1
> 
7c8
<     for i, count in enumerate(arr):
---
>     for i, count in enumerate(counts):
12,13d12
< 
< 
15,20c14,17
< Bucket Sort
< 
< 
< Input:
<     arr: A list of small ints
<     k: Upper bound of the size of the ints in arr (not inclusive)
---
> def bucketsort(arr, k):
>     counts = [0] * k
>     for x in arr:
>         counts[x] += 1
22,23c19,21
< Precondition:
<     all(isinstance(x, int) and 0 <= x < k for x in arr)
---
>     sorted_arr = []
>     for i, count in enumerate(arr):
>         sorted_arr.extend([i] * counts[i])
25,26c23
< Output:
<     The elements of arr in sorted order
---
>     return sorted_arr
