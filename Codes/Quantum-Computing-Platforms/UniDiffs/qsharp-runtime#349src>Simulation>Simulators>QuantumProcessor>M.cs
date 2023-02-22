--- qsharp-runtime/qsharp-runtime#349/after/src>Simulation>Simulators>QuantumProcessor>M.cs	2022-01-10 16:02:54.000000000 +0000
+++ qsharp-runtime/qsharp-runtime#349/before/src>Simulation>Simulators>QuantumProcessor>M.cs	2022-01-10 16:02:54.000000000 +0000
@@ -17,7 +17,7 @@
                 this.Simulator = m;
             }
 
-            public override Func<Qubit, Result> __Body__ => (q) =>
+            public override Func<Qubit, Result> Body => (q) =>
             {
                 return Simulator.QuantumProcessor.M(q);
             };
