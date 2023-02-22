--- BuggyCodes/find_first_in_sorted.py	2022-08-29 18:38:22.000000000 +0100
+++ CorrectCodes/find_first_in_sorted.py	2022-08-29 18:38:22.000000000 +0100
@@ -1,8 +1,9 @@
+
 def find_first_in_sorted(arr, x):
     lo = 0
     hi = len(arr)
 
-    while lo <= hi:
+    while lo < hi:
         mid = (lo + hi) // 2
 
         if x == arr[mid] and (mid == 0 or x != arr[mid - 1]):
@@ -16,20 +17,41 @@
 
     return -1
 
-
 """
-Fancy Binary Search
-fancy-binsearch
+def find_first_in_sorted(arr, x):
+    lo = 0
+    hi = len(arr)
+
+    while lo <= hi - 1:
+        mid = (lo + hi) // 2
+
+        if x == arr[mid] and (mid == 0 or x != arr[mid - 1]):
+            return mid
+
+        elif x <= arr[mid]:
+            hi = mid
+
+        else:
+            lo = mid + 1
 
+    return -1
+
+def find_first_in_sorted(arr, x):
+    lo = 0
+    hi = len(arr)
+
+    while lo + 1 <= hi:
+        mid = (lo + hi) // 2
+
+        if x == arr[mid] and (mid == 0 or x != arr[mid - 1]):
+            return mid
+
+        elif x <= arr[mid]:
+            hi = mid
 
-Input:
-    arr: A sorted list of ints
-    x: A value to find
+        else:
+            lo = mid + 1
 
-Output:
-    The lowest index i such that arr[i] == x, or -1 if x not in arr
+    return -1
 
-Example:
-    >>> find_first_in_sorted([3, 4, 5, 5, 5, 5, 6], 5)
-    2
 """
