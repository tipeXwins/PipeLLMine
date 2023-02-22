--- qsharp-runtime/qsharp-runtime#349/after/src>Simulation>Simulators>QuantumSimulator>AssertProb.cs	2022-01-10 16:02:54.000000000 +0000
+++ qsharp-runtime/qsharp-runtime#349/before/src>Simulation>Simulators>QuantumSimulator>AssertProb.cs	2022-01-10 16:02:54.000000000 +0000
@@ -25,7 +25,7 @@
                 this.Simulator = m;
             }
 
-            public override Func<(IQArray<Pauli>, IQArray<Qubit>, Result, double, string, double), QVoid> __Body__ => (_args) =>
+            public override Func<(IQArray<Pauli>, IQArray<Qubit>, Result, double, string, double), QVoid> Body => (_args) =>
             {
                 var (paulis, qubits, result, expectedPr, msg, tol) = _args;
 
@@ -68,11 +68,11 @@
                 return QVoid.Instance;
             };
 
-            public override Func<(IQArray<Pauli>, IQArray<Qubit>, Result, double, string, double), QVoid> __AdjointBody__ => (_args) => { return QVoid.Instance; };
+            public override Func<(IQArray<Pauli>, IQArray<Qubit>, Result, double, string, double), QVoid> AdjointBody => (_args) => { return QVoid.Instance; };
 
-            public override Func<(IQArray<Qubit>, (IQArray<Pauli>, IQArray<Qubit>, Result, double, string, double)), QVoid> __ControlledBody__ => (_args) => { return QVoid.Instance; };
+            public override Func<(IQArray<Qubit>, (IQArray<Pauli>, IQArray<Qubit>, Result, double, string, double)), QVoid> ControlledBody => (_args) => { return QVoid.Instance; };
 
-            public override Func<(IQArray<Qubit>, (IQArray<Pauli>, IQArray<Qubit>, Result, double, string, double)), QVoid> __ControlledAdjointBody__ => (_args) => { return QVoid.Instance; };
+            public override Func<(IQArray<Qubit>, (IQArray<Pauli>, IQArray<Qubit>, Result, double, string, double)), QVoid> ControlledAdjointBody => (_args) => { return QVoid.Instance; };
         }
     }
 }
