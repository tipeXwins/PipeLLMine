--- qsharp-runtime/qsharp-runtime#349/after/QCTraceSimulator.Interface.R.cs	2022-01-10 16:02:54.000000000 +0000
+++ qsharp-runtime/qsharp-runtime#349/before/QCTraceSimulator.Interface.R.cs	2022-01-10 16:02:54.000000000 +0000
@@ -17,7 +17,7 @@
             }
 
             public override Func<(Pauli, double, Qubit), QVoid>
-                __Body__ => (arg) =>
+                Body => (arg) =>
                 {
                     (Pauli axis, double angle, Qubit target) = arg;
                     tracerCore.R(axis, angle, target);
@@ -25,4 +25,4 @@
                 };
         }
     }
-}
+}
\ No newline at end of file
