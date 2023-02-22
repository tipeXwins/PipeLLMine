--- qsharp-runtime/qsharp-runtime#349/after/src>Simulation>Simulators>QuantumSimulator>T.cs	2022-01-10 16:02:54.000000000 +0000
+++ qsharp-runtime/qsharp-runtime#349/before/src>Simulation>Simulators>QuantumSimulator>T.cs	2022-01-10 16:02:54.000000000 +0000
@@ -31,7 +31,7 @@
                 this.Simulator = m;
             }
 
-            public override Func<Qubit, QVoid> __Body__ => (q1) =>
+            public override Func<Qubit, QVoid> Body => (q1) =>
             {
                 Simulator.CheckQubit(q1);
 
@@ -39,7 +39,7 @@
                 return QVoid.Instance;
             };
 
-            public override Func<(IQArray<Qubit>, Qubit), QVoid> __ControlledBody__ => (_args) =>
+            public override Func<(IQArray<Qubit>, Qubit), QVoid> ControlledBody => (_args) =>
             {
                 (IQArray<Qubit> ctrls, Qubit q1) = _args;
 
@@ -52,7 +52,7 @@
                 return QVoid.Instance;
             };
 
-            public override Func<Qubit, QVoid> __AdjointBody__ => (q1) =>
+            public override Func<Qubit, QVoid> AdjointBody => (q1) =>
             {
                 Simulator.CheckQubit(q1);
                 
@@ -60,14 +60,14 @@
                 return QVoid.Instance;
             };
 
-            public override Func<(IQArray<Qubit>, Qubit), QVoid> __ControlledAdjointBody__ => (_args) =>
+            public override Func<(IQArray<Qubit>, Qubit), QVoid> ControlledAdjointBody => (_args) =>
             {
                 (IQArray<Qubit> ctrls, Qubit q1) = _args;
 
                 Simulator.CheckQubits(ctrls, q1);
 
                 SafeControlled(ctrls,
-                    () => this.__AdjointBody__(q1),
+                    () => this.AdjointBody(q1),
                     (count, ids) => MCAdjT(Simulator.Id, count, ids, (uint)q1.Id));
 
                 return QVoid.Instance;
