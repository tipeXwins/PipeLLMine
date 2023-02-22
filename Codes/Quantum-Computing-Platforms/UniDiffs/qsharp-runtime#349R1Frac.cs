--- qsharp-runtime/qsharp-runtime#349/after/R1Frac.cs	2022-01-10 16:02:54.000000000 +0000
+++ qsharp-runtime/qsharp-runtime#349/before/R1Frac.cs	2022-01-10 16:02:54.000000000 +0000
@@ -19,7 +19,7 @@
                 this.Simulator = m;
             }
 
-            public override Func<(long, long, Qubit), QVoid> __Body__ => (_args) =>
+            public override Func<(long, long, Qubit), QVoid> Body => (_args) =>
             {
                 (long num, long denom, Qubit q1) = _args;
                 (long numNew, long denomNew) = CommonUtils.Reduce(num, denom);
@@ -27,13 +27,13 @@
                 return QVoid.Instance;
             };
 
-            public override Func<(long, long, Qubit), QVoid> __AdjointBody__ => (_args) =>
+            public override Func<(long, long, Qubit), QVoid> AdjointBody => (_args) =>
             {
                 (long num, long denom, Qubit q1) = _args;
-                return this.__Body__.Invoke((-num, denom, q1));
+                return this.Body.Invoke((-num, denom, q1));
             };
 
-            public override Func<(IQArray<Qubit>, (long, long, Qubit)), QVoid> __ControlledBody__ => (_args) =>
+            public override Func<(IQArray<Qubit>, (long, long, Qubit)), QVoid> ControlledBody => (_args) =>
             {
                 (IQArray<Qubit> ctrls, (long num, long denom, Qubit q1)) = _args;
                 (long numNew, long denomNew) = CommonUtils.Reduce(num, denom);
@@ -50,10 +50,10 @@
                 return QVoid.Instance;
             };
 
-            public override Func<(IQArray<Qubit>, (long, long, Qubit)), QVoid> __ControlledAdjointBody__ => (_args) =>
+            public override Func<(IQArray<Qubit>, (long, long, Qubit)), QVoid> ControlledAdjointBody => (_args) =>
             {
                 (IQArray<Qubit> ctrls, (long num, long denom, Qubit q1)) = _args;
-                return this.__ControlledBody__.Invoke((ctrls, (-num, denom, q1)));
+                return this.ControlledBody.Invoke((ctrls, (-num, denom, q1)));
             };
         }
     }
