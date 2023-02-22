--- BuggyCodes/sieve.py	2022-08-29 18:38:22.000000000 +0100
+++ CorrectCodes/sieve.py	2022-08-29 18:38:22.000000000 +0100
@@ -1,17 +1,31 @@
+
 def sieve(max):
     primes = []
     for n in range(2, max + 1):
-        if any(n % p > 0 for p in primes):
+        if all(n % p > 0 for p in primes):
             primes.append(n)
     return primes
 
 """
-Sieve of Eratosthenes
-prime-sieve
+def sieve(max):
+    primes = []
+    for n in range(2, max + 1):
+        if not any(n % p == 0 for p in primes):
+            primes.append(n)
+    return primes
 
-Input:
-    max: A positive int representing an upper bound.
+def sieve(max):
+    primes = []
+    for n in range(2, max + 1):
+        if all(n % p for p in primes):
+            primes.append(n)
+    return primes
+
+def sieve(max):
+    primes = []
+    for n in range(2, max + 1):
+        if not any(n % p for p in primes):
+            primes.append(n)
+    return primes
 
-Output:
-    A list containing all primes up to and including max
 """
