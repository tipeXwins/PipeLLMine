--- qsharp-runtime/qsharp-runtime#55/after/Range.cs	2022-01-10 16:02:54.000000000 +0000
+++ qsharp-runtime/qsharp-runtime#55/before/Range.cs	2022-01-10 16:02:54.000000000 +0000
@@ -66,11 +66,9 @@
         public static Range Empty =>
             new Range(0L, -1L);
 
-        public bool IsEmpty =>
-            (End < Start && Step >= 0) || (End > Start && Step <= 0);
         public Range Reverse()
         {
-            if (IsEmpty) return Range.Empty; 
+            if ((End < Start && Step >= 0) || (End > Start && Step <= 0)) return Range.Empty; 
             long newStart = Start + ((End - Start) / Step) * Step;
             return new Range(newStart, -Step, Start);
         }
