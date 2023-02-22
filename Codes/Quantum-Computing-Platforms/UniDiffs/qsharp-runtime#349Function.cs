--- qsharp-runtime/qsharp-runtime#349/after/Function.cs	2022-01-10 16:02:54.000000000 +0000
+++ qsharp-runtime/qsharp-runtime#349/before/Function.cs	2022-01-10 16:02:54.000000000 +0000
@@ -29,15 +29,15 @@
         OperationFunctor ICallable.Variant => OperationFunctor.Body;
 
         [DebuggerBrowsable(DebuggerBrowsableState.Never)]
-        public abstract Func<I, O> __Body__ { get; }
+        public abstract Func<I, O> Body { get; }
 
-        public virtual IApplyData __DataIn__(I data) => new QTuple<I>(data);
+        public virtual IApplyData __dataIn(I data) => new QTuple<I>(data);
 
-        public virtual IApplyData __DataOut__(O data) => new QTuple<O>(data);
+        public virtual IApplyData __dataOut(O data) => new QTuple<O>(data);
 
         public O Apply(I a)
         {
-            var __result__ = this.__Body__(a);
+            var __result__ = this.Body(a);
             return __result__; 
         }
 
