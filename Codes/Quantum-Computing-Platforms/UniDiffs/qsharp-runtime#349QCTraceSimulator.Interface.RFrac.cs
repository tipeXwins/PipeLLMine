--- qsharp-runtime/qsharp-runtime#349/after/QCTraceSimulator.Interface.RFrac.cs	2022-01-10 16:02:54.000000000 +0000
+++ qsharp-runtime/qsharp-runtime#349/before/QCTraceSimulator.Interface.RFrac.cs	2022-01-10 16:02:54.000000000 +0000
@@ -16,7 +16,7 @@
                 tracerCore = m;
             }
 
-            public override Func<(Pauli, long, long, Qubit), QVoid> __Body__
+            public override Func<(Pauli, long, long, Qubit), QVoid> Body
                 => (arg) =>
                 {
                     (Pauli axis, long numerator, long denomPower, Qubit target) = arg;
@@ -25,4 +25,4 @@
                 };
         }
     }
-}
+}
\ No newline at end of file
