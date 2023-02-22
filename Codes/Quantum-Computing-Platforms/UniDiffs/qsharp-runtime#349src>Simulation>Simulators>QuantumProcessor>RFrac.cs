--- qsharp-runtime/qsharp-runtime#349/after/src>Simulation>Simulators>QuantumProcessor>RFrac.cs	2022-01-10 16:02:54.000000000 +0000
+++ qsharp-runtime/qsharp-runtime#349/before/src>Simulation>Simulators>QuantumProcessor>RFrac.cs	2022-01-10 16:02:54.000000000 +0000
@@ -20,7 +20,7 @@
                 this.Simulator = m;
             }
 
-            public override Func<(Pauli, long, long, Qubit), QVoid> __Body__ => (_args) =>
+            public override Func<(Pauli, long, long, Qubit), QVoid> Body => (_args) =>
             {
                 (Pauli basis, long num, long denom, Qubit q1) = _args;
                 if (basis != Pauli.PauliI)
@@ -31,13 +31,13 @@
                 return QVoid.Instance;
             };
 
-            public override Func<(Pauli, long, long, Qubit), QVoid> __AdjointBody__ => (_args) =>
+            public override Func<(Pauli, long, long, Qubit), QVoid> AdjointBody => (_args) =>
             {
                 (Pauli basis, long num, long denom, Qubit q1) = _args;
-                return this.__Body__.Invoke((basis, -num, denom, q1));
+                return this.Body.Invoke((basis, -num, denom, q1));
             };
 
-            public override Func<(IQArray<Qubit>, (Pauli, long, long, Qubit)), QVoid> __ControlledBody__ => (_args) =>
+            public override Func<(IQArray<Qubit>, (Pauli, long, long, Qubit)), QVoid> ControlledBody => (_args) =>
             {
                 (IQArray<Qubit> ctrls, (Pauli basis, long num, long denom, Qubit q1)) = _args;
                 (long numNew, long denomNew) = CommonUtils.Reduce(num, denom);
@@ -54,10 +54,10 @@
                 return QVoid.Instance;
             };
 
-            public override Func<(IQArray<Qubit>, (Pauli, long, long, Qubit)), QVoid> __ControlledAdjointBody__ => (_args) =>
+            public override Func<(IQArray<Qubit>, (Pauli, long, long, Qubit)), QVoid> ControlledAdjointBody => (_args) =>
             {
                 (IQArray<Qubit> ctrls, (Pauli basis, long num, long denom, Qubit q1)) = _args;
-                return this.__ControlledBody__.Invoke((ctrls, (basis, -num, denom, q1)));
+                return this.ControlledBody.Invoke((ctrls, (basis, -num, denom, q1)));
             };
         }
     }
