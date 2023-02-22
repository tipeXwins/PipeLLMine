--- qsharp-runtime/qsharp-runtime#349/after/src>Simulation>Simulators>QuantumSimulator>random.cs	2022-01-10 16:02:54.000000000 +0000
+++ qsharp-runtime/qsharp-runtime#349/before/src>Simulation>Simulators>QuantumSimulator>random.cs	2022-01-10 16:02:54.000000000 +0000
@@ -22,7 +22,7 @@
                 this.SimulatorId = m.Id;
             }
 
-            public override Func<IQArray<double>, Int64> __Body__ => (p) =>
+            public override Func<IQArray<double>, Int64> Body => (p) =>
             {
                 return random_choice(this.SimulatorId, p.Length, p.ToArray());
             };            
