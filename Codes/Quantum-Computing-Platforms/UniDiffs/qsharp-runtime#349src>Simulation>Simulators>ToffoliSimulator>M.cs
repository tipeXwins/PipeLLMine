--- qsharp-runtime/qsharp-runtime#349/after/src>Simulation>Simulators>ToffoliSimulator>M.cs	2022-01-10 16:02:54.000000000 +0000
+++ qsharp-runtime/qsharp-runtime#349/before/src>Simulation>Simulators>ToffoliSimulator>M.cs	2022-01-10 16:02:54.000000000 +0000
@@ -29,7 +29,7 @@
             /// For the Toffoli simulator, the implementation returns the state of the measured qubit.
             /// That is, Result.One is returned if the measured qubit is in the One state.
             /// </summary>
-            public override Func<Qubit, Result> __Body__ => (q1) =>
+            public override Func<Qubit, Result> Body => (q1) =>
             {
                 if (q1 == null) return Result.Zero;
 
