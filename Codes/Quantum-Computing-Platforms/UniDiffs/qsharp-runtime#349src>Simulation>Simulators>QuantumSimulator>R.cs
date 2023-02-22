--- qsharp-runtime/qsharp-runtime#349/after/src>Simulation>Simulators>QuantumSimulator>R.cs	2022-01-10 16:02:54.000000000 +0000
+++ qsharp-runtime/qsharp-runtime#349/before/src>Simulation>Simulators>QuantumSimulator>R.cs	2022-01-10 16:02:54.000000000 +0000
@@ -26,7 +26,7 @@
                 this.Simulator = m;
             }
 
-            public override Func<(Pauli, double, Qubit), QVoid> __Body__ => (_args) =>
+            public override Func<(Pauli, double, Qubit), QVoid> Body => (_args) =>
             {
                 var (basis, angle, q1) = _args;
 
@@ -38,14 +38,14 @@
                 return QVoid.Instance;
             };
 
-            public override Func<(Pauli, double, Qubit), QVoid> __AdjointBody__ => (_args) =>
+            public override Func<(Pauli, double, Qubit), QVoid> AdjointBody => (_args) =>
             {
                 var (basis, angle, q1) = _args;
 
-                return this.__Body__.Invoke((basis, -angle, q1));
+                return this.Body.Invoke((basis, -angle, q1));
             };
 
-            public override Func<(IQArray<Qubit>, (Pauli, double, Qubit)), QVoid> __ControlledBody__ => (_args) =>
+            public override Func<(IQArray<Qubit>, (Pauli, double, Qubit)), QVoid> ControlledBody => (_args) =>
             {
                 var (ctrls, (basis, angle, q1)) = _args;
 
@@ -53,18 +53,18 @@
                 CheckAngle(angle);
 
                 SafeControlled(ctrls,
-                    () => this.__Body__.Invoke((basis, angle, q1)),
+                    () => this.Body.Invoke((basis, angle, q1)),
                     (count, ids) => MCR(Simulator.Id, basis, angle, count, ids, (uint)q1.Id));
 
                 return QVoid.Instance;
             };
 
 
-            public override Func<(IQArray<Qubit>, (Pauli, double, Qubit)), QVoid> __ControlledAdjointBody__ => (_args) =>
+            public override Func<(IQArray<Qubit>, (Pauli, double, Qubit)), QVoid> ControlledAdjointBody => (_args) =>
             {
                 var (ctrls, (basis, angle, q1)) = _args;
 
-                return this.__ControlledBody__.Invoke((ctrls, (basis, -angle, q1)));
+                return this.ControlledBody.Invoke((ctrls, (basis, -angle, q1)));
             };
         }
     }
