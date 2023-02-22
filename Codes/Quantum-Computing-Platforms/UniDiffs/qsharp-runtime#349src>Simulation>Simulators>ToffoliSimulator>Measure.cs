--- qsharp-runtime/qsharp-runtime#349/after/src>Simulation>Simulators>ToffoliSimulator>Measure.cs	2022-01-10 16:02:54.000000000 +0000
+++ qsharp-runtime/qsharp-runtime#349/before/src>Simulation>Simulators>ToffoliSimulator>Measure.cs	2022-01-10 16:02:54.000000000 +0000
@@ -32,7 +32,7 @@
             /// That is, Result.One is returned if an odd number of the measured qubits are
             /// in the One state.
             /// </summary>
-            public override Func<(IQArray<Pauli>, IQArray<Qubit>), Result> __Body__ => (_args) =>
+            public override Func<(IQArray<Pauli>, IQArray<Qubit>), Result> Body => (_args) =>
             {
                 Qubit? f(Pauli p, Qubit q) =>
                     p switch {
