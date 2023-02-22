--- qsharp-runtime/qsharp-runtime#349/after/src>Simulation>Simulators>QuantumSimulator>RFrac.cs	2022-01-10 16:02:54.000000000 +0000
+++ qsharp-runtime/qsharp-runtime#349/before/src>Simulation>Simulators>QuantumSimulator>RFrac.cs	2022-01-10 16:02:54.000000000 +0000
@@ -19,32 +19,32 @@
             public static double Angle(long numerator, long power) =>
                 (-2.0 * System.Math.PI * numerator) / (1 << (int)power);
 
-            public override Func<(Pauli, long, long, Qubit), QVoid> __Body__ => (args) =>
+            public override Func<(Pauli, long, long, Qubit), QVoid> Body => (args) =>
             {
                 var (pauli, numerator, power, qubit) = args;
                 var angle = Angle(numerator, power);
-                return R__.Apply((pauli, angle, qubit));
+                return R.Apply((pauli, angle, qubit));
             };
 
-            public override Func<(Pauli, long, long, Qubit), QVoid> __AdjointBody__ => (args) =>
+            public override Func<(Pauli, long, long, Qubit), QVoid> AdjointBody => (args) =>
             {
                 var (pauli, numerator, power, qubit) = args;
                 var angle = Angle(numerator, power);
-                return R__.Adjoint.Apply((pauli, angle, qubit));
+                return R.Adjoint.Apply((pauli, angle, qubit));
             };
 
-            public override Func<(IQArray<Qubit>, (Pauli, long, long, Qubit)), QVoid> __ControlledBody__ => (args) =>
+            public override Func<(IQArray<Qubit>, (Pauli, long, long, Qubit)), QVoid> ControlledBody => (args) =>
             {
                 var (ctrls, (pauli, numerator, power, qubit)) = args;
                 var angle = Angle(numerator, power);
-                return R__.Controlled.Apply((ctrls, (pauli, angle, qubit)));
+                return R.Controlled.Apply((ctrls, (pauli, angle, qubit)));
             };
 
-            public override Func<(IQArray<Qubit>, (Pauli, long, long, Qubit)), QVoid> __ControlledAdjointBody__ => (args) =>
+            public override Func<(IQArray<Qubit>, (Pauli, long, long, Qubit)), QVoid> ControlledAdjointBody => (args) =>
             {
                 var (ctrls, (pauli, numerator, power, qubit)) = args;
                 var angle = Angle(numerator, power);
-                return R__.Adjoint.Controlled.Apply((ctrls, (pauli, angle, qubit)));
+                return R.Adjoint.Controlled.Apply((ctrls, (pauli, angle, qubit)));
             };
         }
     }
