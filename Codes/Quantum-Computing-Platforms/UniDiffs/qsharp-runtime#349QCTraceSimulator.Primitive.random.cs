--- qsharp-runtime/qsharp-runtime#349/after/QCTraceSimulator.Primitive.random.cs	2022-01-10 16:02:54.000000000 +0000
+++ qsharp-runtime/qsharp-runtime#349/before/QCTraceSimulator.Primitive.random.cs	2022-01-10 16:02:54.000000000 +0000
@@ -17,7 +17,7 @@
                 core = m;
             }
 
-            public override Func<IQArray<double>, Int64> __Body__ => (p) =>
+            public override Func<IQArray<double>, Int64> Body => (p) =>
             {
                 return CommonUtils.SampleDistribution(p, core.RandomGenerator.NextDouble());
             };
