--- qsharp-runtime/qsharp-runtime#349/after/src>Simulation>Simulators>QuantumProcessor>Measure.cs	2022-01-10 16:02:54.000000000 +0000
+++ qsharp-runtime/qsharp-runtime#349/before/src>Simulation>Simulators>QuantumProcessor>Measure.cs	2022-01-10 16:02:54.000000000 +0000
@@ -18,7 +18,7 @@
                 this.Simulator = m;
             }
 
-            public override Func<(IQArray<Pauli>, IQArray<Qubit>), Result> __Body__ => (_args) =>
+            public override Func<(IQArray<Pauli>, IQArray<Qubit>), Result> Body => (_args) =>
             {
                 (IQArray<Pauli> paulis, IQArray<Qubit> qubits) = _args;
 
