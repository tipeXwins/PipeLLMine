--- BuggyCodes/next_permutation.py	2022-08-29 18:38:22.000000000 +0100
+++ CorrectCodes/next_permutation.py	2022-08-29 18:38:22.000000000 +0100
@@ -3,29 +3,20 @@
     for i in range(len(perm) - 2, -1, -1):
         if perm[i] < perm[i + 1]:
             for j in range(len(perm) - 1, i, -1):
-                if perm[j] < perm[i]:
+                if perm[i] < perm[j]:
                     next_perm = list(perm)
                     next_perm[i], next_perm[j] = perm[j], perm[i]
                     next_perm[i + 1:] = reversed(next_perm[i + 1:])
                     return next_perm
 
-
-
 """
-Next Permutation
-next-perm
-
-
-Input:
-    perm: A list of unique ints
-
-Precondition:
-    perm is not sorted in reverse order
-
-Output:
-    The lexicographically next permutation of the elements of perm
-
-Example:
-    >>> next_permutation([3, 2, 4, 1])
-    [3, 4, 1, 2]
+def next_permutation(perm):
+    for i in range(len(perm) - 2, -1, -1):
+        if perm[i] < perm[i + 1]:
+            for j in range(len(perm) - 1, i, -1):
+                if perm[j] > perm[i]:
+                    next_perm = list(perm)
+                    next_perm[i], next_perm[j] = perm[j], perm[i]
+                    next_perm[i + 1:] = reversed(next_perm[i + 1:])
+                    return next_perm
 """
