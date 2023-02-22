--- qsharp-runtime/qsharp-runtime#349/after/src>Simulation>Simulators>QuantumProcessor>random.cs	2022-01-10 16:02:54.000000000 +0000
+++ qsharp-runtime/qsharp-runtime#349/before/src>Simulation>Simulators>QuantumProcessor>random.cs	2022-01-10 16:02:54.000000000 +0000
@@ -18,7 +18,7 @@
                 Simulator = m;
             }
 
-            public override Func<IQArray<double>, Int64> __Body__ => (p) =>
+            public override Func<IQArray<double>, Int64> Body => (p) =>
             {
                 return CommonUtils.SampleDistribution(p, Simulator.RandomGenerator.NextDouble());
             };            
