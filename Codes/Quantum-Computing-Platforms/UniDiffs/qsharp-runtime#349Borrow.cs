--- qsharp-runtime/qsharp-runtime#349/after/Borrow.cs	2022-01-10 16:02:54.000000000 +0000
+++ qsharp-runtime/qsharp-runtime#349/before/Borrow.cs	2022-01-10 16:02:54.000000000 +0000
@@ -13,7 +13,7 @@
 
         public abstract IQArray<Qubit> Apply(long count);
 
-        public override void __Init__() { }
+        public override void Init() { }
     }
 }
 
