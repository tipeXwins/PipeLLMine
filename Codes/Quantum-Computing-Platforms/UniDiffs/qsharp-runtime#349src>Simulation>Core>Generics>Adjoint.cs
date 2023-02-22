--- qsharp-runtime/qsharp-runtime#349/after/src>Simulation>Core>Generics>Adjoint.cs	2022-01-10 16:02:54.000000000 +0000
+++ qsharp-runtime/qsharp-runtime#349/before/src>Simulation>Core>Generics>Adjoint.cs	2022-01-10 16:02:54.000000000 +0000
@@ -25,7 +25,7 @@
     [DebuggerTypeProxy(typeof(GenericAdjoint.DebuggerProxy))]
     public class GenericAdjoint : GenericCallable, IApplyData, IOperationWrapper
     {
-        public GenericAdjoint(GenericCallable baseOp) : base(baseOp.__Factory__, null)
+        public GenericAdjoint(GenericCallable baseOp) : base(baseOp.Factory, null)
         {
             this.BaseOp = baseOp;
         }
