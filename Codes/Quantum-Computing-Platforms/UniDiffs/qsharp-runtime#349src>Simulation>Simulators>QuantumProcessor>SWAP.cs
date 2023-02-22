--- qsharp-runtime/qsharp-runtime#349/after/src>Simulation>Simulators>QuantumProcessor>SWAP.cs	2022-01-10 16:02:54.000000000 +0000
+++ qsharp-runtime/qsharp-runtime#349/before/src>Simulation>Simulators>QuantumProcessor>SWAP.cs	2022-01-10 16:02:54.000000000 +0000
@@ -17,13 +17,13 @@
                 this.Simulator = m;
             }
 
-            public override Func<(Qubit,Qubit), QVoid> __Body__ => (q1) =>
+            public override Func<(Qubit,Qubit), QVoid> Body => (q1) =>
             {
                 Simulator.QuantumProcessor.SWAP(q1.Item1, q1.Item2);
                 return QVoid.Instance;
             };
 
-            public override Func<(IQArray<Qubit>, (Qubit, Qubit)), QVoid> __ControlledBody__ => (args) =>
+            public override Func<(IQArray<Qubit>, (Qubit, Qubit)), QVoid> ControlledBody => (args) =>
             {
                 (IQArray<Qubit> ctrls, (Qubit q1, Qubit q2) ) = args;
 
