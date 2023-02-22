17c17
<     if len(arr) == 0:
---
>     if len(arr) <= 1:
24a25,39
> """
> def mergesort(arr):
>     def merge(left, right):
>         result = []
>         i = 0
>         j = 0
>         while i < len(left) and j < len(right):
>             if left[i] <= right[j]:
>                 result.append(left[i])
>                 i += 1
>             else:
>                 result.append(right[j])
>                 j += 1
>         result.extend(left[i:] or right[j:])
>         return result
25a41,47
>     if len(arr) == 0 or len(arr) == 1:
>         return arr
>     else:
>         middle = len(arr) // 2
>         left = mergesort(arr[:middle])
>         right = mergesort(arr[middle:])
>         return merge(left, right)
27,28c49,62
< """
< Merge Sort
---
> def mergesort(arr):
>     def merge(left, right):
>         result = []
>         i = 0
>         j = 0
>         while i < len(left) and j < len(right):
>             if left[i] <= right[j]:
>                 result.append(left[i])
>                 i += 1
>             else:
>                 result.append(right[j])
>                 j += 1
>         result.extend(left[i:] or right[j:])
>         return result
29a64,70
>     if len(arr) == 1 or len(arr) == 0:
>         return arr
>     else:
>         middle = len(arr) // 2
>         left = mergesort(arr[:middle])
>         right = mergesort(arr[middle:])
>         return merge(left, right)
31,32c72,85
< Input:
<     arr: A list of ints
---
> def mergesort(arr):
>     def merge(left, right):
>         result = []
>         i = 0
>         j = 0
>         while i < len(left) and j < len(right):
>             if left[i] <= right[j]:
>                 result.append(left[i])
>                 i += 1
>             else:
>                 result.append(right[j])
>                 j += 1
>         result.extend(left[i:] or right[j:])
>         return result
34,35c87,93
< Output:
<     The elements of arr in sorted order
---
>     if len(arr) < 2:
>         return arr
>     else:
>         middle = len(arr) // 2
>         left = mergesort(arr[:middle])
>         right = mergesort(arr[middle:])
>         return merge(left, right)
