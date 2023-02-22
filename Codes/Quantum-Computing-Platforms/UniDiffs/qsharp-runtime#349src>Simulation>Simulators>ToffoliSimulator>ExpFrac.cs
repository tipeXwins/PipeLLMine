--- qsharp-runtime/qsharp-runtime#349/after/src>Simulation>Simulators>ToffoliSimulator>ExpFrac.cs	2022-01-10 16:02:54.000000000 +0000
+++ qsharp-runtime/qsharp-runtime#349/before/src>Simulation>Simulators>ToffoliSimulator>ExpFrac.cs	2022-01-10 16:02:54.000000000 +0000
@@ -30,7 +30,7 @@
             /// For the Toffoli simulator, the implementation flips a target qubit
             /// if the respective rotation is effectively an X gate.
             /// </summary>
-            public override Func<(IQArray<Pauli>, long, long, IQArray<Qubit>), QVoid> __Body__ => (_args) =>
+            public override Func<(IQArray<Pauli>, long, long, IQArray<Qubit>), QVoid> Body => (_args) =>
             {
                 var (bases, num, den, qubits) = _args;
 
@@ -59,7 +59,7 @@
             /// The implementation of the adjoint specialization of the operation.
             /// For the Toffoli simulator *only*, this operation is self-adjoint.
             /// </summary>
-            public override Func<(IQArray<Pauli>, long, long, IQArray<Qubit>), QVoid> __AdjointBody__ => __Body__;
+            public override Func<(IQArray<Pauli>, long, long, IQArray<Qubit>), QVoid> AdjointBody => Body;
 
             /// <summary>
             /// The implementation of the controlled specialization of the operation.
@@ -67,7 +67,7 @@
             /// if the rotation is effectively an X gate and all of the control qubits
             /// are in the One state.
             /// </summary>
-            public override Func<(IQArray<Qubit>, (IQArray<Pauli>, long, long, IQArray<Qubit>)), QVoid> __ControlledBody__ => (_args) =>
+            public override Func<(IQArray<Qubit>, (IQArray<Pauli>, long, long, IQArray<Qubit>)), QVoid> ControlledBody => (_args) =>
             {
                 var (ctrls, (bases, num, den, qubits)) = _args;
 
@@ -97,7 +97,7 @@
             /// The implementation of the controlled adjoint specialization of the operation.
             /// For the Toffoli simulator *only*, the controlled specialization is self-adjoint.
             /// </summary>
-            public override Func<(IQArray<Qubit>, (IQArray<Pauli>, long, long, IQArray<Qubit>)), QVoid> __ControlledAdjointBody__ => __ControlledBody__;
+            public override Func<(IQArray<Qubit>, (IQArray<Pauli>, long, long, IQArray<Qubit>)), QVoid> ControlledAdjointBody => ControlledBody;
         }
     }
 }
