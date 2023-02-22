--- qsharp-runtime/qsharp-runtime#349/after/src>Simulation>Simulators>ToffoliSimulator>R.cs	2022-01-10 16:02:54.000000000 +0000
+++ qsharp-runtime/qsharp-runtime#349/before/src>Simulation>Simulators>ToffoliSimulator>R.cs	2022-01-10 16:02:54.000000000 +0000
@@ -29,7 +29,7 @@
             /// For the Toffoli simulator, the implementation flips the target qubit
             /// if the rotation is effectively an X gate.
             /// </summary>
-            public override Func<(Pauli, double, Qubit), QVoid> __Body__ => (_args) =>
+            public override Func<(Pauli, double, Qubit), QVoid> Body => (_args) =>
             {
                 var (basis, angle, q1) = _args;
 
@@ -50,7 +50,7 @@
             /// The implementation of the adjoint specialization of the operation.
             /// For the Toffoli simulator *only*, this operation is self-adjoint.
             /// </summary>
-            public override Func<(Pauli, double, Qubit), QVoid> __AdjointBody__ => __Body__;
+            public override Func<(Pauli, double, Qubit), QVoid> AdjointBody => Body;
 
             /// <summary>
             /// The implementation of the controlled specialization of the operation.
@@ -58,7 +58,7 @@
             /// if the rotation is effectively an X gate and all of the control qubits
             /// are in the One state.
             /// </summary>
-            public override Func<(IQArray<Qubit>, (Pauli, double, Qubit)), QVoid> __ControlledBody__ => (_args) =>
+            public override Func<(IQArray<Qubit>, (Pauli, double, Qubit)), QVoid> ControlledBody => (_args) =>
             {
                 var (ctrls, (basis, angle, q1)) = _args;
 
@@ -80,7 +80,7 @@
             /// The implementation of the controlled adjoint specialization of the operation.
             /// For the Toffoli simulator *only*, the controlled specialization is self-adjoint.
             /// </summary>
-            public override Func<(IQArray<Qubit>, (Pauli, double, Qubit)), QVoid> __ControlledAdjointBody__ => __ControlledBody__;
+            public override Func<(IQArray<Qubit>, (Pauli, double, Qubit)), QVoid> ControlledAdjointBody => ControlledBody;
         }
     }
 }
