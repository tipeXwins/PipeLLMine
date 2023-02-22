--- QuantumLibraries/QuantumLibraries#303/after/Integer.qs	2022-01-10 16:02:54.000000000 +0000
+++ QuantumLibraries/QuantumLibraries#303/before/Integer.qs	2022-01-10 16:02:54.000000000 +0000
@@ -228,8 +228,8 @@
                 ApplyOuterCDKMAdder(xs, ys, auxiliary);
             } apply {
                 CarryOutCoreCDKM(xs, ys, auxiliary, carry);
+                ApplyToEachCA(X, Most(Rest(ys!)));
             }
-            ApplyToEachCA(X, Most(Rest(ys!)));
             CNOT(xs![0], ys![0]);
         }
     }
