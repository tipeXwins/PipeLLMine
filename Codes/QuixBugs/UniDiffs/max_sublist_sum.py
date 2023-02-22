--- BuggyCodes/max_sublist_sum.py	2022-08-29 18:38:22.000000000 +0100
+++ CorrectCodes/max_sublist_sum.py	2022-08-29 18:38:22.000000000 +0100
@@ -4,28 +4,41 @@
     max_so_far = 0
 
     for x in arr:
-        max_ending_here = max_ending_here + x
+        max_ending_here = max(0, max_ending_here + x)
         max_so_far = max(max_so_far, max_ending_here)
 
     return max_so_far
 
-
 """
-Max Sublist Sum
-max-sublist-sum
+def max_sublist_sum(arr):
+    max_ending_here = 0
+    max_so_far = 0
 
-Efficient equivalent to max(sum(arr[i:j]) for 0 <= i <= j <= len(arr))
+    for x in arr:
+        max_ending_here = max(max_ending_here + x, 0)
+        max_so_far = max(max_so_far, max_ending_here)
 
-Algorithm source: WordAligned.org by Thomas Guest
+    return max_so_far
 
+def max_sublist_sum(arr):
+    max_ending_here = 0
+    max_so_far = 0
 
-Input:
-    arr: A list of ints
+    for x in arr:
+        max_ending_here = max(x, max_ending_here + x)
+        max_so_far = max(max_so_far, max_ending_here)
 
-Output:
-    The maximum sublist sum
+    return max_so_far
+
+
+def max_sublist_sum(arr):
+    max_ending_here = 0
+    max_so_far = 0
+
+    for x in arr:
+        max_ending_here = max(max_ending_here + x, x)
+        max_so_far = max(max_so_far, max_ending_here)
+
+    return max_so_far
 
-Example:
-    >>> max_sublist_sum([4, -5, 2, 1, -1, 3])
-    5
 """
