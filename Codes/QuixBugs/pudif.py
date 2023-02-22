--- BuggyCodes/bitcount.py	2022-08-29 18:38:22.000000000 +0100
+++ CorrectCodes/bitcount.py	2023-02-22 11:08:13.472859540 +0000
@@ -5,22 +5,3 @@
         n ^= n - 1
         count += 1
     return count
-
-
-"""
-Bitcount
-bitcount
-
-
-Input:
-    n: a nonnegative int
-
-Output:
-    The number of 1-bits in the binary encoding of n
-
-Examples:
-    >>> bitcount(127)
-    7
-    >>> bitcount(128)
-    1
-"""
