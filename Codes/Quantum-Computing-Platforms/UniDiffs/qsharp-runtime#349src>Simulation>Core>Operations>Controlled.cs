--- qsharp-runtime/qsharp-runtime#349/after/src>Simulation>Core>Operations>Controlled.cs	2022-01-10 16:02:54.000000000 +0000
+++ qsharp-runtime/qsharp-runtime#349/before/src>Simulation>Core>Operations>Controlled.cs	2022-01-10 16:02:54.000000000 +0000
@@ -60,7 +60,7 @@
             IEnumerable<Qubit> IApplyData.Qubits => Qubit.Concat(Ctrls, BaseData?.Qubits);
         }
 
-        public ControlledOperation(Operation<I, O> op) : base(op.__Factory__)
+        public ControlledOperation(Operation<I, O> op) : base(op.Factory)
         {
             Debug.Assert(typeof(O) == typeof(QVoid));
             Debug.Assert(op is Operation<I, QVoid>);
@@ -71,17 +71,17 @@
         public Operation<I, QVoid> BaseOp { get; }
         ICallable IOperationWrapper.BaseOperation => BaseOp;
 
-        public override void __Init__() { }
+        public override void Init() { }
 
         string ICallable.Name => ((ICallable)this.BaseOp).Name;
         string ICallable.FullName => ((ICallable)this.BaseOp).FullName;
         OperationFunctor ICallable.Variant => ((ICallable)this.BaseOp).ControlledVariant();
 
-        public override Func<(IQArray<Qubit>, I), QVoid> __Body__ => this.BaseOp.__ControlledBody__;
+        public override Func<(IQArray<Qubit>, I), QVoid> Body => this.BaseOp.ControlledBody;
 
-        public override Func<(IQArray<Qubit>, I), QVoid> __AdjointBody__ => this.BaseOp.__ControlledAdjointBody__;
+        public override Func<(IQArray<Qubit>, I), QVoid> AdjointBody => this.BaseOp.ControlledAdjointBody;
 
-        public override Func<(IQArray<Qubit>, (IQArray<Qubit>, I)), QVoid> __ControlledBody__
+        public override Func<(IQArray<Qubit>, (IQArray<Qubit>, I)), QVoid> ControlledBody
         {
             get
             {
@@ -89,12 +89,12 @@
                 {
                     var (ctrl1, (ctrl2, args)) = __in;
                     var ctrls = QArray<Qubit>.Add(ctrl1, ctrl2);
-                    return this.BaseOp.__ControlledBody__.Invoke((ctrls, args));
+                    return this.BaseOp.ControlledBody.Invoke((ctrls, args));
                 };
             }
         }
 
-        public override Func<(IQArray<Qubit>, (IQArray<Qubit>, I)), QVoid> __ControlledAdjointBody__
+        public override Func<(IQArray<Qubit>, (IQArray<Qubit>, I)), QVoid> ControlledAdjointBody
         {
             get
             {
@@ -102,16 +102,16 @@
                 {
                     var (ctrl1, (ctrl2, args)) = __in;
                     var ctrls = QArray<Qubit>.Add(ctrl1, ctrl2);
-                    return this.BaseOp.__ControlledAdjointBody__.Invoke((ctrls, args));
+                    return this.BaseOp.ControlledAdjointBody.Invoke((ctrls, args));
                 };
             }
         }
 
         IEnumerable<Qubit> IApplyData.Qubits => ((IApplyData)this.BaseOp).Qubits;
 
-        public override IApplyData __DataIn__((IQArray<Qubit>, I) data) => new In((data.Item1, this.BaseOp.__DataIn__(data.Item2)));
+        public override IApplyData __dataIn((IQArray<Qubit>, I) data) => new In((data.Item1, this.BaseOp.__dataIn(data.Item2)));
 
-        public override IApplyData __DataOut__(QVoid data) => data;
+        public override IApplyData __dataOut(QVoid data) => data;
 
         /// <inheritdoc/>
         public override RuntimeMetadata? GetRuntimeMetadata(IApplyData args)
@@ -121,7 +121,7 @@
             if (args.Value is ValueTuple<IQArray<Qubit>, I> ctrlArgs)
             {
                 var (controls, baseArgs) = ctrlArgs;
-                var baseMetadata = this.BaseOp.GetRuntimeMetadata(this.BaseOp.__DataIn__(baseArgs));
+                var baseMetadata = this.BaseOp.GetRuntimeMetadata(this.BaseOp.__dataIn(baseArgs));
                 if (baseMetadata == null) return null;
                 baseMetadata.IsControlled = true;
                 baseMetadata.Controls = controls.Concat(baseMetadata.Controls);
