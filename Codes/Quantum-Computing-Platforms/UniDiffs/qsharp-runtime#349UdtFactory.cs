--- qsharp-runtime/qsharp-runtime#349/after/UdtFactory.cs	2022-01-10 16:02:54.000000000 +0000
+++ qsharp-runtime/qsharp-runtime#349/before/UdtFactory.cs	2022-01-10 16:02:54.000000000 +0000
@@ -47,7 +47,7 @@
 
         public ICallable Partial(object partialTuple) => this.Partial<ICallable>(partialTuple);
 
-        public override void __Init__()
+        public override void Init()
         { }
     }
-}
+}
\ No newline at end of file
