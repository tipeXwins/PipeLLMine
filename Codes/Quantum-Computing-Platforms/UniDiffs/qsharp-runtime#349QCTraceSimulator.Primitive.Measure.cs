--- qsharp-runtime/qsharp-runtime#349/after/QCTraceSimulator.Primitive.Measure.cs	2022-01-10 16:02:54.000000000 +0000
+++ qsharp-runtime/qsharp-runtime#349/before/QCTraceSimulator.Primitive.Measure.cs	2022-01-10 16:02:54.000000000 +0000
@@ -16,7 +16,7 @@
             }
 
             public override Func<(IQArray<Pauli>, IQArray<Qubit>), Result>
-                __Body__ => (args) =>
+                Body => (args) =>
                 {
                     (IQArray<Pauli> observable, IQArray<Qubit> target) = args;
                     return core.Measure(observable, target);
@@ -25,4 +25,4 @@
 
 
     }
-}
+}
\ No newline at end of file
