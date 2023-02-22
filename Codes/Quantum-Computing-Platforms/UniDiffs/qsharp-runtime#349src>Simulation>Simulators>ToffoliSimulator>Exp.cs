--- qsharp-runtime/qsharp-runtime#349/after/src>Simulation>Simulators>ToffoliSimulator>Exp.cs	2022-01-10 16:02:54.000000000 +0000
+++ qsharp-runtime/qsharp-runtime#349/before/src>Simulation>Simulators>ToffoliSimulator>Exp.cs	2022-01-10 16:02:54.000000000 +0000
@@ -29,7 +29,7 @@
             /// For the Toffoli simulator, the implementation flips a target qubit
             /// if the respective rotation is effectively an X gate.
             /// </summary>
-            public override Func<(IQArray<Pauli>, double, IQArray<Qubit>), QVoid> __Body__ => (_args) =>
+            public override Func<(IQArray<Pauli>, double, IQArray<Qubit>), QVoid> Body => (_args) =>
             {
                 var (bases, angle, qubits) = _args;
 
@@ -58,7 +58,7 @@
             /// The implementation of the adjoint specialization of the operation.
             /// For the Toffoli simulator *only*, this operation is self-adjoint.
             /// </summary>
-            public override Func<(IQArray<Pauli>, double, IQArray<Qubit>), QVoid> __AdjointBody__ => __Body__;
+            public override Func<(IQArray<Pauli>, double, IQArray<Qubit>), QVoid> AdjointBody => Body;
 
             /// <summary>
             /// The implementation of the controlled specialization of the operation.
@@ -66,7 +66,7 @@
             /// if the rotation is effectively an X gate and all of the control qubits
             /// are in the One state.
             /// </summary>
-            public override Func<(IQArray<Qubit>, (IQArray<Pauli>, double, IQArray<Qubit>)), QVoid> __ControlledBody__ => (_args) =>
+            public override Func<(IQArray<Qubit>, (IQArray<Pauli>, double, IQArray<Qubit>)), QVoid> ControlledBody => (_args) =>
             {
                 var (ctrls, (bases, angle, qubits)) = _args;
 
@@ -96,7 +96,7 @@
             /// The implementation of the controlled adjoint specialization of the operation.
             /// For the Toffoli simulator *only*, the controlled specialization is self-adjoint.
             /// </summary>
-            public override Func<(IQArray<Qubit>, (IQArray<Pauli>, double, IQArray<Qubit>)), QVoid> __ControlledAdjointBody__ => __ControlledBody__;
+            public override Func<(IQArray<Qubit>, (IQArray<Pauli>, double, IQArray<Qubit>)), QVoid> ControlledAdjointBody => ControlledBody;
         }
     }
 }
