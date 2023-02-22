--- qsharp-runtime/qsharp-runtime#349/after/src>Simulation>Simulators>ToffoliSimulator>SWAP.cs	2022-01-10 16:02:54.000000000 +0000
+++ qsharp-runtime/qsharp-runtime#349/before/src>Simulation>Simulators>ToffoliSimulator>SWAP.cs	2022-01-10 16:02:54.000000000 +0000
@@ -29,7 +29,7 @@
             /// The implementation of the operation.
             /// For the Toffoli simulator, the implementation swaps the states of the two qubits.
             /// </summary>
-            public override Func<(Qubit, Qubit), QVoid> __Body__ => (args) =>
+            public override Func<(Qubit, Qubit), QVoid> Body => (args) =>
             {
                 var (q1, q2) = args;
 
@@ -53,7 +53,7 @@
             /// For the Toffoli simulator, the implementation swaps the states of the
             /// target qubits if all of the control qubits are 1.
             /// </summary>
-            public override Func<(IQArray<Qubit>, (Qubit, Qubit)), QVoid> __ControlledBody__ => (args) =>
+            public override Func<(IQArray<Qubit>, (Qubit, Qubit)), QVoid> ControlledBody => (args) =>
             {
                 var (ctrls, (q1, q2)) = args;
 
