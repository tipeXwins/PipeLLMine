--- qsharp-runtime/qsharp-runtime#349/after/Random.cs	2022-01-10 16:02:54.000000000 +0000
+++ qsharp-runtime/qsharp-runtime#349/before/Random.cs	2022-01-10 16:02:54.000000000 +0000
@@ -29,7 +29,7 @@
             /// <summary>
             /// The implementation of the operation.
             /// </summary>
-            public override Func<IQArray<double>, Int64> __Body__ => (probs) =>
+            public override Func<IQArray<double>, Int64> Body => (probs) =>
                 CommonUtils.SampleDistribution(probs, Simulator.RandomGenerator.NextDouble());
         }
     }
