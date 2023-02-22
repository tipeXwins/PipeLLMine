--- BuggyCodes/longest_common_subsequence.py	2022-08-29 18:38:22.000000000 +0100
+++ CorrectCodes/longest_common_subsequence.py	2022-08-29 18:38:22.000000000 +0100
@@ -1,9 +1,10 @@
+
 def longest_common_subsequence(a, b):
     if not a or not b:
         return ''
 
     elif a[0] == b[0]:
-        return a[0] + longest_common_subsequence(a[1:], b)
+        return a[0] + longest_common_subsequence(a[1:], b[1:])
 
     else:
         return max(
@@ -12,23 +13,3 @@
             key=len
         )
 
-
-
-"""
-Longest Common Subsequence
-
-
-Calculates the longest subsequence common to the two input strings. (A subsequence is any sequence of letters in the same order
-they appear in the string, possibly skipping letters in between.)
-
-Input:
-    a: The first string to consider.
-    b: The second string to consider.
-
-Output:
-    The longest string which is a subsequence of both strings. (If multiple subsequences of equal length exist, either is OK.)
-
-Example:
-    >>> longest_common_subsequence('headache', 'pentadactyl')
-    'eadac'
-"""
