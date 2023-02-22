--- qsharp-runtime/qsharp-runtime#349/after/src>Simulation>Simulators>QuantumSimulator>Exp.cs	2022-01-10 16:02:54.000000000 +0000
+++ qsharp-runtime/qsharp-runtime#349/before/src>Simulation>Simulators>QuantumSimulator>Exp.cs	2022-01-10 16:02:54.000000000 +0000
@@ -26,7 +26,7 @@
                 this.Simulator = m;
             }
 
-            public override Func<(IQArray<Pauli>, double, IQArray<Qubit>), QVoid> __Body__ => (_args) =>
+            public override Func<(IQArray<Pauli>, double, IQArray<Qubit>), QVoid> Body => (_args) =>
             {
                 var (paulis, theta, qubits) = _args;
 
@@ -43,14 +43,14 @@
                 return QVoid.Instance;
             };
 
-            public override Func<(IQArray<Pauli>, double, IQArray<Qubit>), QVoid> __AdjointBody__ => (_args) =>
+            public override Func<(IQArray<Pauli>, double, IQArray<Qubit>), QVoid> AdjointBody => (_args) =>
             {
                 var (paulis, angle, qubits) = _args;
 
-                return this.__Body__.Invoke((paulis, -angle, qubits));
+                return this.Body.Invoke((paulis, -angle, qubits));
             };
 
-            public override Func<(IQArray<Qubit>, (IQArray<Pauli>, double, IQArray<Qubit>)), QVoid> __ControlledBody__ => (_args) =>
+            public override Func<(IQArray<Qubit>, (IQArray<Pauli>, double, IQArray<Qubit>)), QVoid> ControlledBody => (_args) =>
             {
                 var (ctrls, (paulis, angle, qubits)) = _args;
 
@@ -63,17 +63,17 @@
                 }
 
                 SafeControlled(ctrls,
-                    () => this.__Body__.Invoke((paulis, angle, qubits)),
+                    () => this.Body.Invoke((paulis, angle, qubits)),
                     (count, ids) => MCExp(Simulator.Id, (uint)paulis.Length, paulis.ToArray(), angle, count, ids, qubits.GetIds()));
 
                 return QVoid.Instance;
             };
 
-            public override Func<(IQArray<Qubit>, (IQArray<Pauli>, double, IQArray<Qubit>)), QVoid> __ControlledAdjointBody__ => (_args) =>
+            public override Func<(IQArray<Qubit>, (IQArray<Pauli>, double, IQArray<Qubit>)), QVoid> ControlledAdjointBody => (_args) =>
             {
                 var (ctrls, (paulis, angle, qubits)) = _args;
 
-                return this.__ControlledBody__.Invoke((ctrls, (paulis, -angle, qubits)));
+                return this.ControlledBody.Invoke((ctrls, (paulis, -angle, qubits)));
             };
         }
     }
