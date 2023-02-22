--- qsharp-runtime/qsharp-runtime#349/after/AbstractCallable.cs	2022-01-10 16:02:54.000000000 +0000
+++ qsharp-runtime/qsharp-runtime#349/before/AbstractCallable.cs	2022-01-10 16:02:54.000000000 +0000
@@ -21,15 +21,15 @@
 
         public AbstractCallable(IOperationFactory m)
         {
-            this.__Factory__ = m;
+            this.Factory = m;
         }
 
-        public IOperationFactory __Factory__ { get; private set; }
+        public IOperationFactory Factory { get; private set; }
 
         /// <summary>
         /// This method is called once, to let the Operation initialize and verify its dependencies.
         /// </summary>
-        public abstract void __Init__();
+        public abstract void Init();
 
         /// <summary>
         /// Retrieves the runtime metadata of the Operation. If the Operation has no associated
