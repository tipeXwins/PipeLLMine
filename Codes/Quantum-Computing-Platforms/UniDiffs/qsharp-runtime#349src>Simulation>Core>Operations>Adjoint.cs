--- qsharp-runtime/qsharp-runtime#349/after/src>Simulation>Core>Operations>Adjoint.cs	2022-01-10 16:02:54.000000000 +0000
+++ qsharp-runtime/qsharp-runtime#349/before/src>Simulation>Core>Operations>Adjoint.cs	2022-01-10 16:02:54.000000000 +0000
@@ -43,7 +43,7 @@
     [DebuggerTypeProxy(typeof(AdjointedOperation<,>.DebuggerProxy))]
     public class AdjointedOperation<I, O> : Unitary<I>, IApplyData, ICallable, IOperationWrapper
     {
-        public AdjointedOperation(Operation<I, O> op) : base(op.__Factory__)
+        public AdjointedOperation(Operation<I, O> op) : base(op.Factory)
         {
             Debug.Assert(typeof(O) == typeof(QVoid));
             Debug.Assert(op is Operation<I, QVoid>);
@@ -54,25 +54,25 @@
         public Operation<I, QVoid> BaseOp { get; }
         ICallable IOperationWrapper.BaseOperation => BaseOp;
 
-        public override void __Init__() { }
+        public override void Init() { }
 
         string ICallable.Name => ((ICallable)this.BaseOp).Name;
         string ICallable.FullName => ((ICallable)this.BaseOp).FullName;
         OperationFunctor ICallable.Variant => ((ICallable)this.BaseOp).AdjointVariant();
         
-        public override Func<I, QVoid> __Body__ => this.BaseOp.__AdjointBody__;
+        public override Func<I, QVoid> Body => this.BaseOp.AdjointBody;
 
-        public override Func<I, QVoid> __AdjointBody__ => this.BaseOp.__Body__;
+        public override Func<I, QVoid> AdjointBody => this.BaseOp.Body;
 
-        public override Func<(IQArray<Qubit>, I), QVoid> __ControlledBody__ => this.BaseOp.__ControlledAdjointBody__;
+        public override Func<(IQArray<Qubit>, I), QVoid> ControlledBody => this.BaseOp.ControlledAdjointBody;
                                                  
-        public override Func<(IQArray<Qubit>, I), QVoid> __ControlledAdjointBody__ => this.BaseOp.__ControlledBody__;
+        public override Func<(IQArray<Qubit>, I), QVoid> ControlledAdjointBody => this.BaseOp.ControlledBody;
 
         IEnumerable<Qubit> IApplyData.Qubits => ((IApplyData)this.BaseOp).Qubits;
 
-        public override IApplyData __DataIn__(I data) => this.BaseOp.__DataIn__(data);
+        public override IApplyData __dataIn(I data) => this.BaseOp.__dataIn(data);
 
-        public override IApplyData __DataOut__(QVoid data) => data;
+        public override IApplyData __dataOut(QVoid data) => data;
 
         /// <inheritdoc/>
         public override RuntimeMetadata? GetRuntimeMetadata(IApplyData args)
