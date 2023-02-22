--- qsharp-runtime/qsharp-runtime#55/after/QArray.cs	2022-01-10 16:02:54.000000000 +0000
+++ qsharp-runtime/qsharp-runtime#55/before/QArray.cs	2022-01-10 16:02:54.000000000 +0000
@@ -387,11 +387,11 @@
                 return new QArray<T>();
             }
 
-            if (range.IsEmpty)
+            long rangeCount = 1 + (range.End - range.Start) / range.Step;
+            if (rangeCount <= 0)
             {
                 return new QArray<T>();
             }
-            long rangeCount = 1 + (range.End - range.Start) / range.Step;
             long rangeEnd = range.Start + (rangeCount - 1) * range.Step;
 
             // Make sure the slice fits
