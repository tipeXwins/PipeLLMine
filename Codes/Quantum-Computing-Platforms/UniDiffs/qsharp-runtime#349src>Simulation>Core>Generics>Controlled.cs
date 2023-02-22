--- qsharp-runtime/qsharp-runtime#349/after/src>Simulation>Core>Generics>Controlled.cs	2022-01-10 16:02:54.000000000 +0000
+++ qsharp-runtime/qsharp-runtime#349/before/src>Simulation>Core>Generics>Controlled.cs	2022-01-10 16:02:54.000000000 +0000
@@ -27,7 +27,7 @@
     [DebuggerTypeProxy(typeof(GenericControlled.DebuggerProxy))]
     public class GenericControlled : GenericCallable, IApplyData, IOperationWrapper
     {
-        public GenericControlled(GenericCallable baseOp) : base(baseOp.__Factory__, null)
+        public GenericControlled(GenericCallable baseOp) : base(baseOp.Factory, null)
         {
             this.BaseOp = baseOp;
         }
