--- qsharp-runtime/qsharp-runtime#256/after/InterfaceUtils.cs	2022-01-10 16:02:54.000000000 +0000
+++ qsharp-runtime/qsharp-runtime#256/before/InterfaceUtils.cs	2022-01-10 16:02:54.000000000 +0000
@@ -2,7 +2,6 @@
 // Licensed under the MIT License.
 
 using System;
-using System.Collections.Generic;
 using System.Diagnostics;
 
 using Microsoft.Quantum.Simulation.Core;
@@ -74,18 +73,5 @@
         {
             return InterfaceType(t, typeof(IControllable<>));
         }
-        internal static IEnumerable<TResult> SelectAggregates<TSource, TResult>(
-            this IEnumerable<TSource> source,
-            Func<TResult, TSource, TResult> aggregate,
-            TResult initial = default
-        )
-        {
-            var acc = initial;
-            foreach (var element in source)
-            {
-                acc = aggregate(acc, element);
-                yield return acc;
-            }
-        }
     }
-}
+}
\ No newline at end of file
