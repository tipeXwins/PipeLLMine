--- qsharp-runtime/qsharp-runtime#349/after/src>Simulation>Simulators>QuantumSimulator>Z.cs	2022-01-10 16:02:54.000000000 +0000
+++ qsharp-runtime/qsharp-runtime#349/before/src>Simulation>Simulators>QuantumSimulator>Z.cs	2022-01-10 16:02:54.000000000 +0000
@@ -25,7 +25,7 @@
                 this.Simulator = m;
             }
 
-            public override Func<Qubit, QVoid> __Body__ => (q1) =>
+            public override Func<Qubit, QVoid> Body => (q1) =>
             {
                 Simulator.CheckQubit(q1); ;
 
@@ -34,7 +34,7 @@
                 return QVoid.Instance;
             };
 
-            public override Func<(IQArray<Qubit>, Qubit), QVoid> __ControlledBody__ => (_args) =>
+            public override Func<(IQArray<Qubit>, Qubit), QVoid> ControlledBody => (_args) =>
             {
                 (IQArray<Qubit> ctrls, Qubit q1) = _args;
 
