--- qsharp-runtime/qsharp-runtime#349/after/QCTraceSimulator.Interface.ForceMeasure.cs	2022-01-10 16:02:54.000000000 +0000
+++ qsharp-runtime/qsharp-runtime#349/before/QCTraceSimulator.Interface.ForceMeasure.cs	2022-01-10 16:02:54.000000000 +0000
@@ -15,7 +15,7 @@
                 tracerCore = m;
             }
 
-            public override Func<(IQArray<Pauli>, IQArray<Qubit>, Result), QVoid> __Body__
+            public override Func<(IQArray<Pauli>, IQArray<Qubit>, Result), QVoid> Body
                 => (arg) =>
                 {
                     (IQArray<Pauli> observable, IQArray<Qubit> target, Result result) = arg;
@@ -24,4 +24,4 @@
                 };
         }
     }
-}
+}
\ No newline at end of file
