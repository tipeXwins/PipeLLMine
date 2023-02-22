--- qsharp-runtime/qsharp-runtime#349/after/GenericPartial.cs	2022-01-10 16:02:54.000000000 +0000
+++ qsharp-runtime/qsharp-runtime#349/before/GenericPartial.cs	2022-01-10 16:02:54.000000000 +0000
@@ -18,7 +18,7 @@
     {
         private Lazy<Qubit[]> __qubits = null;
 
-        public GenericPartial(GenericCallable baseOp, object partialValues) : base(baseOp.__Factory__, null)
+        public GenericPartial(GenericCallable baseOp, object partialValues) : base(baseOp.Factory, null)
         {
             Debug.Assert(baseOp != null, "Received a null base operation");
             Debug.Assert(partialValues != null, "Received a null partial value");
