--- qsharp-runtime/qsharp-runtime#349/after/src>Simulation>Simulators>QuantumProcessor>Exp.cs	2022-01-10 16:02:54.000000000 +0000
+++ qsharp-runtime/qsharp-runtime#349/before/src>Simulation>Simulators>QuantumProcessor>Exp.cs	2022-01-10 16:02:54.000000000 +0000
@@ -18,7 +18,7 @@
                 this.Simulator = m;
             }
 
-            public override Func<(IQArray<Pauli>, double, IQArray<Qubit>), QVoid> __Body__ => (_args) =>
+            public override Func<(IQArray<Pauli>, double, IQArray<Qubit>), QVoid> Body => (_args) =>
             {
                 (IQArray<Pauli> paulis, double angle, IQArray<Qubit> qubits) = _args;
 
@@ -35,14 +35,14 @@
                 return QVoid.Instance;
             };
 
-            public override Func<(IQArray<Pauli>, double, IQArray<Qubit>), QVoid> __AdjointBody__ => (_args) =>
+            public override Func<(IQArray<Pauli>, double, IQArray<Qubit>), QVoid> AdjointBody => (_args) =>
             {
                 (IQArray<Pauli> paulis, double angle, IQArray<Qubit> qubits) = _args;
                 
-                return this.__Body__.Invoke((paulis, -angle, qubits));
+                return this.Body.Invoke((paulis, -angle, qubits));
             };
 
-            public override Func<(IQArray<Qubit>, (IQArray<Pauli>, double, IQArray<Qubit>)), QVoid> __ControlledBody__ => (_args) =>
+            public override Func<(IQArray<Qubit>, (IQArray<Pauli>, double, IQArray<Qubit>)), QVoid> ControlledBody => (_args) =>
             {
                 (IQArray<Qubit> ctrls, (IQArray<Pauli> paulis, double angle, IQArray<Qubit> qubits)) = _args;
 
@@ -66,11 +66,11 @@
                 return QVoid.Instance;
             };
 
-            public override Func<(IQArray<Qubit>, (IQArray<Pauli>, double, IQArray<Qubit>)), QVoid> __ControlledAdjointBody__ => (_args) =>
+            public override Func<(IQArray<Qubit>, (IQArray<Pauli>, double, IQArray<Qubit>)), QVoid> ControlledAdjointBody => (_args) =>
             {
                 (IQArray<Qubit> ctrls, (IQArray<Pauli> paulis, double angle, IQArray<Qubit> qubits)) = _args;
 
-                return this.__ControlledBody__.Invoke((ctrls, (paulis, -angle, qubits)));
+                return this.ControlledBody.Invoke((ctrls, (paulis, -angle, qubits)));
             };
         }
     }
