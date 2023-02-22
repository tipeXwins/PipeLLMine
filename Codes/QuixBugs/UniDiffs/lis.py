--- BuggyCodes/lis.py	2022-08-29 18:38:22.000000000 +0100
+++ CorrectCodes/lis.py	2022-08-29 18:38:22.000000000 +0100
@@ -11,27 +11,24 @@
 
         if length == longest or val < arr[ends[length + 1]]:
             ends[length + 1] = i
-            longest = length + 1
+            longest = max(longest, length + 1)
 
     return longest
 
-
-
 """
-Longest Increasing Subsequence
-longest-increasing-subsequence
+def lis(arr):
+    ends = {}
+    longest = 0
 
+    for i, val in enumerate(arr):
 
-Input:
-    arr: A sequence of ints
+        prefix_lengths = [j for j in range(1, longest + 1) if arr[ends[j]] < val]
 
-Precondition:
-    The ints in arr are unique
+        length = max(prefix_lengths) if prefix_lengths else 0
 
-Output:
-    The length of the longest monotonically increasing subsequence of arr
+        if length == longest or val < arr[ends[length + 1]]:
+            ends[length + 1] = i
+            longest = max(length + 1, longest)
 
-Example:
-    >>> lis([4, 1, 5, 3, 7, 6, 2])
-    3
+    return longest
 """
