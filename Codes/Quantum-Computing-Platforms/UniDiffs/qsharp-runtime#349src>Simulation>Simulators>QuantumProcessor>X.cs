--- qsharp-runtime/qsharp-runtime#349/after/src>Simulation>Simulators>QuantumProcessor>X.cs	2022-01-10 16:02:54.000000000 +0000
+++ qsharp-runtime/qsharp-runtime#349/before/src>Simulation>Simulators>QuantumProcessor>X.cs	2022-01-10 16:02:54.000000000 +0000
@@ -17,13 +17,13 @@
                 this.Simulator = m;
             }
 
-            public override Func<Qubit, QVoid> __Body__ => (q1) =>
+            public override Func<Qubit, QVoid> Body => (q1) =>
             {
                 Simulator.QuantumProcessor.X(q1);
                 return QVoid.Instance;
             };
 
-            public override Func<(IQArray<Qubit>, Qubit), QVoid> __ControlledBody__ => (args) =>
+            public override Func<(IQArray<Qubit>, Qubit), QVoid> ControlledBody => (args) =>
             {
                 (IQArray<Qubit> ctrls, Qubit q1) = args;
 
