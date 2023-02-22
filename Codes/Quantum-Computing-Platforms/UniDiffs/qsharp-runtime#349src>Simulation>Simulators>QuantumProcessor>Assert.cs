--- qsharp-runtime/qsharp-runtime#349/after/src>Simulation>Simulators>QuantumProcessor>Assert.cs	2022-01-10 16:02:54.000000000 +0000
+++ qsharp-runtime/qsharp-runtime#349/before/src>Simulation>Simulators>QuantumProcessor>Assert.cs	2022-01-10 16:02:54.000000000 +0000
@@ -18,7 +18,7 @@
                 this.Simulator = m;
             }
 
-            public override Func<(IQArray<Pauli>, IQArray<Qubit>, Result, string), QVoid> __Body__ => (_args) =>
+            public override Func<(IQArray<Pauli>, IQArray<Qubit>, Result, string), QVoid> Body => (_args) =>
             {
                 (IQArray<Pauli> paulis, IQArray<Qubit> qubits, Result result, string msg) = _args;
                 if (paulis.Length != qubits.Length)
@@ -33,11 +33,11 @@
                 return QVoid.Instance;
             };
 
-            public override Func<(IQArray<Pauli>, IQArray<Qubit>, Result, string), QVoid> __AdjointBody__ => (_args) => { return QVoid.Instance; };
+            public override Func<(IQArray<Pauli>, IQArray<Qubit>, Result, string), QVoid> AdjointBody => (_args) => { return QVoid.Instance; };
 
-            public override Func<(IQArray<Qubit>, (IQArray<Pauli>, IQArray<Qubit>, Result, string)), QVoid> __ControlledBody__ => (_args) => { return QVoid.Instance; };
+            public override Func<(IQArray<Qubit>, (IQArray<Pauli>, IQArray<Qubit>, Result, string)), QVoid> ControlledBody => (_args) => { return QVoid.Instance; };
 
-            public override Func<(IQArray<Qubit>, (IQArray<Pauli>, IQArray<Qubit>, Result, string)), QVoid> __ControlledAdjointBody__ => (_args) => { return QVoid.Instance; };
+            public override Func<(IQArray<Qubit>, (IQArray<Pauli>, IQArray<Qubit>, Result, string)), QVoid> ControlledAdjointBody => (_args) => { return QVoid.Instance; };
         }
     }
 }
