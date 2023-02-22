--- qsharp-runtime/qsharp-runtime#349/after/R1.cs	2022-01-10 16:02:54.000000000 +0000
+++ qsharp-runtime/qsharp-runtime#349/before/R1.cs	2022-01-10 16:02:54.000000000 +0000
@@ -18,20 +18,20 @@
                 this.Simulator = m;
             }
 
-            public override Func<(double, Qubit), QVoid> __Body__ => (_args) =>
+            public override Func<(double, Qubit), QVoid> Body => (_args) =>
             {
                 (double angle, Qubit q1) = _args;
                 Simulator.QuantumProcessor.R1(angle, q1);
                 return QVoid.Instance;
             };
 
-            public override Func<(double, Qubit), QVoid> __AdjointBody__ => (_args) =>
+            public override Func<(double, Qubit), QVoid> AdjointBody => (_args) =>
             {
                 (double angle, Qubit q1) = _args;
-                return this.__Body__.Invoke((-angle, q1));
+                return this.Body.Invoke((-angle, q1));
             };
 
-            public override Func<(IQArray<Qubit>, ( double, Qubit)), QVoid> __ControlledBody__ => (_args) =>
+            public override Func<(IQArray<Qubit>, ( double, Qubit)), QVoid> ControlledBody => (_args) =>
             {
                 (IQArray<Qubit> ctrls, (double angle, Qubit q1)) = _args;
 
@@ -48,10 +48,10 @@
             };
 
 
-            public override Func<(IQArray<Qubit>, (double, Qubit)), QVoid> __ControlledAdjointBody__ => (_args) =>
+            public override Func<(IQArray<Qubit>, (double, Qubit)), QVoid> ControlledAdjointBody => (_args) =>
             {
                 (IQArray<Qubit> ctrls, (double angle, Qubit q1)) = _args;
-                return this.__ControlledBody__.Invoke((ctrls, (-angle, q1)));
+                return this.ControlledBody.Invoke((ctrls, (-angle, q1)));
             };
         }
     }
