--- qsharp-runtime/qsharp-runtime#349/after/src>Simulation>Simulators>QuantumSimulator>ExpFrac.cs	2022-01-10 16:02:54.000000000 +0000
+++ qsharp-runtime/qsharp-runtime#349/before/src>Simulation>Simulators>QuantumSimulator>ExpFrac.cs	2022-01-10 16:02:54.000000000 +0000
@@ -19,32 +19,32 @@
             public static double Angle(long numerator, long power) =>
                 (System.Math.PI * numerator) / (1 << (int)power);
 
-            public override Func<(IQArray<Pauli>, long, long, IQArray<Qubit>), QVoid> __Body__ => (args) =>
+            public override Func<(IQArray<Pauli>, long, long, IQArray<Qubit>), QVoid> Body => (args) =>
             {
                 var (paulis, numerator, power, qubits) = args;
                 var angle = Angle(numerator, power);
-                return Exp__.Apply((paulis, angle, qubits));
+                return Exp.Apply((paulis, angle, qubits));
             };
 
-            public override Func<(IQArray<Pauli>, long, long, IQArray<Qubit>), QVoid> __AdjointBody__ => (args) =>
+            public override Func<(IQArray<Pauli>, long, long, IQArray<Qubit>), QVoid> AdjointBody => (args) =>
             {
                 var (paulis, numerator, power, qubits) = args;
                 var angle = Angle(numerator, power);
-                return Exp__.Adjoint.Apply((paulis, angle, qubits));
+                return Exp.Adjoint.Apply((paulis, angle, qubits));
             };
 
-            public override Func<(IQArray<Qubit>, (IQArray<Pauli>, long, long, IQArray<Qubit>)), QVoid> __ControlledBody__ => (args) =>
+            public override Func<(IQArray<Qubit>, (IQArray<Pauli>, long, long, IQArray<Qubit>)), QVoid> ControlledBody => (args) =>
             {
                 var (ctrls, (paulis, numerator, power, qubits)) = args;
                 var angle = Angle(numerator, power);
-                return Exp__.Controlled.Apply((ctrls, (paulis, angle, qubits)));
+                return Exp.Controlled.Apply((ctrls, (paulis, angle, qubits)));
             };
 
-            public override Func<(IQArray<Qubit>, (IQArray<Pauli>, long, long, IQArray<Qubit>)), QVoid> __ControlledAdjointBody__ => (args) =>
+            public override Func<(IQArray<Qubit>, (IQArray<Pauli>, long, long, IQArray<Qubit>)), QVoid> ControlledAdjointBody => (args) =>
             {
                 var (ctrls, (paulis, numerator, power, qubits)) = args;
                 var angle = Angle(numerator, power);
-                return Exp__.Adjoint.Controlled.Apply((ctrls, (paulis, angle, qubits)));
+                return Exp.Adjoint.Controlled.Apply((ctrls, (paulis, angle, qubits)));
             };
         }
     }
