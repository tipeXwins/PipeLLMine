--- BuggyCodes/subsequences.py	2022-08-29 18:38:22.000000000 +0100
+++ CorrectCodes/subsequences.py	2022-08-29 18:38:22.000000000 +0100
@@ -1,6 +1,7 @@
+
 def subsequences(a, b, k):
     if k == 0:
-        return []
+        return [[]]
 
     ret = []
     for i in range(a, b + 1 - k):
@@ -10,22 +11,3 @@
 
     return ret
 
-
-"""
-Subsequences
-
-
-Input:
-    a: An int
-    b: An int
-    k: A positive int
-
-Output:
-    A list of all length-k ascending sequences of ints in range(a, b)
-
-Example:
-    >>> subsequences(a=1, b=5, k=3)
-    [[1, 2, 3], [1, 2, 4], [1, 3, 4], [2, 3, 4]]
-"""
-
-
