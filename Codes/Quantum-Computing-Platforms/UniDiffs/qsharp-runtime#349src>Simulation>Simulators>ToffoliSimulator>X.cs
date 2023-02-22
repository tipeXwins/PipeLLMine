--- qsharp-runtime/qsharp-runtime#349/after/src>Simulation>Simulators>ToffoliSimulator>X.cs	2022-01-10 16:02:54.000000000 +0000
+++ qsharp-runtime/qsharp-runtime#349/before/src>Simulation>Simulators>ToffoliSimulator>X.cs	2022-01-10 16:02:54.000000000 +0000
@@ -28,7 +28,7 @@
             /// The implementation of the operation.
             /// For the Toffoli simulator, the implementation flips the target qubit.
             /// </summary>
-            public override Func<Qubit, QVoid> __Body__ => (q1) =>
+            public override Func<Qubit, QVoid> Body => (q1) =>
             {
                 if (q1 == null) return QVoid.Instance;
 
@@ -44,7 +44,7 @@
             /// For the Toffoli simulator, the implementation flips the target qubit 
             /// if all of the control qubits are 1.
             /// </summary>
-            public override Func<(IQArray<Qubit>, Qubit), QVoid> __ControlledBody__ => (args) =>
+            public override Func<(IQArray<Qubit>, Qubit), QVoid> ControlledBody => (args) =>
             {
                 var (ctrls, q) = args;
                 if (q == null) return QVoid.Instance;
