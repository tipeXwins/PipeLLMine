--- qsharp-runtime/qsharp-runtime#349/after/src>Simulation>Simulators>ToffoliSimulator>Y.cs	2022-01-10 16:02:54.000000000 +0000
+++ qsharp-runtime/qsharp-runtime#349/before/src>Simulation>Simulators>ToffoliSimulator>Y.cs	2022-01-10 16:02:54.000000000 +0000
@@ -25,7 +25,7 @@
             /// The implementation of the operation.
             /// For the Toffoli simulator, the implementation throws a run-time error.
             /// </summary>
-            public override Func<Qubit, QVoid> __Body__ => (q1) =>
+            public override Func<Qubit, QVoid> Body => (q1) =>
             {
                 throw new NotImplementedException();
             };
