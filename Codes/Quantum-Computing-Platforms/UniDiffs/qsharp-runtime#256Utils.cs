--- qsharp-runtime/qsharp-runtime#256/after/Utils.cs	2022-01-10 16:02:54.000000000 +0000
+++ qsharp-runtime/qsharp-runtime#256/before/Utils.cs	2022-01-10 16:02:54.000000000 +0000
@@ -1,9 +1,7 @@
 ﻿// Copyright (c) Microsoft Corporation. All rights reserved.
 // Licensed under the MIT License.
 
-using System;
 using System.Collections.Generic;
-using System.Linq;
 using Microsoft.Quantum.Simulation.Core;
 using Microsoft.Quantum.Simulation.QCTraceSimulatorRuntime;
 
@@ -216,29 +214,32 @@
         /// <param name="uniformZeroOneSample"> Number between Zero and one, uniformly distributed</param>
         public static long SampleDistribution(IQArray<double> unnormalizedDistribution, double uniformZeroOneSample)
         {
-            if (unnormalizedDistribution.Any(prob => prob < 0.0))
+            double total = 0.0;
+            foreach (double prob in unnormalizedDistribution)
             {
-                throw new ExecutionFailException("Random expects array of non-negative doubles.");
+                if (prob < 0)
+                {
+                    throw new ExecutionFailException("Random expects array of non-negative doubles.");
+                }
+                total += prob;
             }
 
-            var total = unnormalizedDistribution.Sum();
             if (total == 0)
             {
                 throw new ExecutionFailException("Random expects array of non-negative doubles with positive sum.");
             }
 
-            var sample = uniformZeroOneSample * total;
-            return unnormalizedDistribution
-                .SelectAggregates((double acc, double x) => acc + x)
-                .Select((cumulativeProb, idx) => (cumulativeProb, idx))
-                .Where(item => item.cumulativeProb >= sample)
-                .Select(
-                    item => (long)item.idx
-                )
-                .DefaultIfEmpty(
-                    unnormalizedDistribution.Length - 1
-                )
-                .First();
+            double sample = uniformZeroOneSample * total;
+            double sum = unnormalizedDistribution[0];
+            for (int i = 0; i < unnormalizedDistribution.Length - 1; ++i)
+            {
+                if (sum >= sample)
+                {
+                    return i;
+                }
+                sum += unnormalizedDistribution[i];
+            }
+            return unnormalizedDistribution.Length;
         }
     }
 }
