--- QuantumLibraries/QuantumLibraries#48/after/Random.qs	2022-01-10 16:02:54.000000000 +0000
+++ QuantumLibraries/QuantumLibraries#48/before/Random.qs	2022-01-10 16:02:54.000000000 +0000
@@ -110,7 +110,7 @@
             fail $"Number of random bits must be greater than 0.";
         }
         
-        return ToDouble(RandomIntPow2(bitsRandom)) / PowD(2.0, ToDouble(bitsRandom));
+        return ToDouble(RandomIntPow2(bitsRandom)) / ToDouble(2 ^ bitsRandom + 1);
     }
     
 }
