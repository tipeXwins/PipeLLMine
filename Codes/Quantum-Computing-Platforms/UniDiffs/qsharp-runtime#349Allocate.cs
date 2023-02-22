--- qsharp-runtime/qsharp-runtime#349/after/Allocate.cs	2022-01-10 16:02:54.000000000 +0000
+++ qsharp-runtime/qsharp-runtime#349/before/Allocate.cs	2022-01-10 16:02:54.000000000 +0000
@@ -13,6 +13,6 @@
 
         public abstract IQArray<Qubit> Apply(long count);
 
-        public override void __Init__() { }
+        public override void Init() { }
     }
 }
