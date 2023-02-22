--- qsharp-runtime/qsharp-runtime#349/after/src>Simulation>Simulators>QuantumProcessor>ExpFrac.cs	2022-01-10 16:02:54.000000000 +0000
+++ qsharp-runtime/qsharp-runtime#349/before/src>Simulation>Simulators>QuantumProcessor>ExpFrac.cs	2022-01-10 16:02:54.000000000 +0000
@@ -15,7 +15,7 @@
 
             public QuantumProcessorDispatcherExpFrac(QuantumProcessorDispatcher m) : base(m) { this.Simulator = m; }
 
-            public override Func<(IQArray<Pauli>, long, long, IQArray<Qubit>), QVoid> __Body__ => (_args) =>
+            public override Func<(IQArray<Pauli>, long, long, IQArray<Qubit>), QVoid> Body => (_args) =>
             {
                 (IQArray<Pauli> paulis, long nom, long den, IQArray<Qubit> qubits) = _args;
 
@@ -31,15 +31,15 @@
                 return QVoid.Instance;
             };
 
-            public override Func<(IQArray<Pauli>, long, long, IQArray<Qubit>), QVoid> __AdjointBody__ => (_args) =>
+            public override Func<(IQArray<Pauli>, long, long, IQArray<Qubit>), QVoid> AdjointBody => (_args) =>
             {
                 (IQArray<Pauli> paulis, long nom, long den, IQArray<Qubit> qubits) = _args;
                 
-                return this.__Body__.Invoke((paulis, -nom, den, qubits));
+                return this.Body.Invoke((paulis, -nom, den, qubits));
             };
 
             public override Func<(IQArray<Qubit>, (IQArray<Pauli>, long, long, IQArray<Qubit>)), QVoid>
-                __ControlledBody__ => (_args) =>
+                ControlledBody => (_args) =>
                 {
                     (IQArray<Qubit> ctrls, (IQArray<Pauli> paulis, long nom, long den, IQArray<Qubit> qubits)) = _args;
 
@@ -64,11 +64,11 @@
                 };
 
             public override Func<(IQArray<Qubit>, (IQArray<Pauli>, long, long, IQArray<Qubit>)), QVoid>
-                __ControlledAdjointBody__ => (_args) =>
+                ControlledAdjointBody => (_args) =>
                 {
                     (IQArray<Qubit> ctrls, (IQArray<Pauli> paulis, long nom, long den, IQArray<Qubit> qubits)) = _args;
 
-                    return this.__ControlledBody__.Invoke((ctrls, (paulis, -nom, den, qubits)));
+                    return this.ControlledBody.Invoke((ctrls, (paulis, -nom, den, qubits)));
                 };
         }
     }
