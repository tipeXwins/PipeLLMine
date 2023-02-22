--- qsharp-runtime/qsharp-runtime#349/after/Core.cs	2022-01-10 16:02:54.000000000 +0000
+++ qsharp-runtime/qsharp-runtime#349/before/Core.cs	2022-01-10 16:02:54.000000000 +0000
@@ -11,7 +11,7 @@
         public class Native : Length<__T__>
         {
             public Native(IOperationFactory m) : base(m) { }
-            public override Func<IQArray<__T__>, long> __Body__ => (arg) => (arg.Length);
+            public override Func<IQArray<__T__>, long> Body => (arg) => (arg.Length);
         }
     }
 
@@ -20,7 +20,7 @@
         public class Native : RangeStart
         {
             public Native(IOperationFactory m) : base(m) { }
-            public override Func<QRange, long> __Body__ => (arg) => (arg.Start);
+            public override Func<QRange, long> Body => (arg) => (arg.Start);
         }
     }
 
@@ -29,7 +29,7 @@
         public class Native : RangeEnd
         {
             public Native(IOperationFactory m) : base(m) { }
-            public override Func<QRange, long> __Body__ => (arg) => (arg.End);
+            public override Func<QRange, long> Body => (arg) => (arg.End);
         }
     }
 
@@ -38,7 +38,7 @@
         public class Native : RangeStep
         {
             public Native(IOperationFactory m) : base(m) { }
-            public override Func<QRange, long> __Body__ => (arg) => (arg.Step);
+            public override Func<QRange, long> Body => (arg) => (arg.Step);
         }
     }
 
@@ -47,7 +47,7 @@
         public class Native : RangeReverse
         {
             public Native(IOperationFactory m) : base(m) { }
-            public override Func<QRange, QRange> __Body__ => (arg) => (arg.Reverse());
+            public override Func<QRange, QRange> Body => (arg) => (arg.Reverse());
         }
     }
 }
