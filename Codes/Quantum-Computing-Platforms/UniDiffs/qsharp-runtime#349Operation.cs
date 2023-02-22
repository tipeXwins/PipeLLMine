--- qsharp-runtime/qsharp-runtime#349/after/Operation.cs	2022-01-10 16:02:54.000000000 +0000
+++ qsharp-runtime/qsharp-runtime#349/before/Operation.cs	2022-01-10 16:02:54.000000000 +0000
@@ -55,21 +55,21 @@
         OperationFunctor ICallable.Variant => OperationFunctor.Body;
 
 
-        public virtual IApplyData __DataIn__(I data) => new QTuple<I>(data);
+        public virtual IApplyData __dataIn(I data) => new QTuple<I>(data);
 
-        public virtual IApplyData __DataOut__(O data) => new QTuple<O>(data);
+        public virtual IApplyData __dataOut(O data) => new QTuple<O>(data);
 
         [DebuggerBrowsable(DebuggerBrowsableState.Never)]
-        public abstract Func<I, O> __Body__ { get; }
+        public abstract Func<I, O> Body { get; }
 
         [DebuggerBrowsable(DebuggerBrowsableState.Never)]
-        public virtual Func<I, QVoid> __AdjointBody__ => throw new NotImplementedException();
+        public virtual Func<I, QVoid> AdjointBody => throw new NotImplementedException();
 
         [DebuggerBrowsable(DebuggerBrowsableState.Never)]
-        public virtual Func<(IQArray<Qubit>, I), QVoid> __ControlledBody__ => throw new NotImplementedException();
+        public virtual Func<(IQArray<Qubit>, I), QVoid> ControlledBody => throw new NotImplementedException();
 
         [DebuggerBrowsable(DebuggerBrowsableState.Never)]
-        public virtual Func<(IQArray<Qubit>, I), QVoid> __ControlledAdjointBody__ => throw new NotImplementedException();
+        public virtual Func<(IQArray<Qubit>, I), QVoid> ControlledAdjointBody => throw new NotImplementedException();
 
         [DebuggerBrowsable(DebuggerBrowsableState.Never)]
         public AdjointedOperation<I, O> Adjoint => _adjoint.Value;
@@ -92,17 +92,17 @@
 
             try
             {
-                this.__Factory__?.StartOperation(this, __DataIn__(a));
-                __result__ = this.__Body__(a);
+                this.Factory?.StartOperation(this, __dataIn(a));
+                __result__ = this.Body(a);
             }
             catch (Exception e)
             {
-                this.__Factory__?.Fail(System.Runtime.ExceptionServices.ExceptionDispatchInfo.Capture(e));
+                this.Factory?.Fail(System.Runtime.ExceptionServices.ExceptionDispatchInfo.Capture(e));
                 throw;
             }
             finally
             {
-                this.__Factory__?.EndOperation(this, __DataOut__(__result__));
+                this.Factory?.EndOperation(this, __dataOut(__result__));
             }
 
             return __result__;
