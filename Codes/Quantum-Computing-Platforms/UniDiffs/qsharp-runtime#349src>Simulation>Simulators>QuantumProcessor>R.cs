--- qsharp-runtime/qsharp-runtime#349/after/src>Simulation>Simulators>QuantumProcessor>R.cs	2022-01-10 16:02:54.000000000 +0000
+++ qsharp-runtime/qsharp-runtime#349/before/src>Simulation>Simulators>QuantumProcessor>R.cs	2022-01-10 16:02:54.000000000 +0000
@@ -19,7 +19,7 @@
                 this.Simulator = m;
             }
 
-            public override Func<(Pauli, double, Qubit), QVoid> __Body__ => (_args) =>
+            public override Func<(Pauli, double, Qubit), QVoid> Body => (_args) =>
             {
                 (Pauli basis, double angle, Qubit q1) = _args;
                 if (basis != Pauli.PauliI)
@@ -29,13 +29,13 @@
                 return QVoid.Instance;
             };
 
-            public override Func<(Pauli, double, Qubit), QVoid> __AdjointBody__ => (_args) =>
+            public override Func<(Pauli, double, Qubit), QVoid> AdjointBody => (_args) =>
             {
                 (Pauli basis, double angle, Qubit q1) = _args;
-                return this.__Body__.Invoke((basis, -angle, q1));
+                return this.Body.Invoke((basis, -angle, q1));
             };
 
-            public override Func<(IQArray<Qubit>, (Pauli, double, Qubit)), QVoid> __ControlledBody__ => (_args) =>
+            public override Func<(IQArray<Qubit>, (Pauli, double, Qubit)), QVoid> ControlledBody => (_args) =>
             {
                 (IQArray<Qubit> ctrls, (Pauli basis, double angle, Qubit q1)) = _args;
 
@@ -52,10 +52,10 @@
             };
 
 
-            public override Func<(IQArray<Qubit>, (Pauli, double, Qubit)), QVoid> __ControlledAdjointBody__ => (_args) =>
+            public override Func<(IQArray<Qubit>, (Pauli, double, Qubit)), QVoid> ControlledAdjointBody => (_args) =>
             {
                 (IQArray<Qubit> ctrls, (Pauli basis, double angle, Qubit q1)) = _args;
-                return this.__ControlledBody__.Invoke((ctrls, (basis, -angle, q1)));
+                return this.ControlledBody.Invoke((ctrls, (basis, -angle, q1)));
             };
         }
     }
