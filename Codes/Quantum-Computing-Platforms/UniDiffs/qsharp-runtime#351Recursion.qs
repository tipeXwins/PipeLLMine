--- qsharp-runtime/qsharp-runtime#351/after/Recursion.qs	2022-01-10 16:02:54.000000000 +0000
+++ qsharp-runtime/qsharp-runtime#351/before/Recursion.qs	2022-01-10 16:02:54.000000000 +0000
@@ -46,7 +46,7 @@
             return x;
         }
         else {
-            let fct = GenRecursionPartial<'T>(_, cnt - 1);
+            let fct = GenRecursionPartial(_, cnt - 1);
             return fct(x);
         }
     }
