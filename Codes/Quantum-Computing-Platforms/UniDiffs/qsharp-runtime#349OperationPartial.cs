--- qsharp-runtime/qsharp-runtime#349/after/OperationPartial.cs	2022-01-10 16:02:54.000000000 +0000
+++ qsharp-runtime/qsharp-runtime#349/before/OperationPartial.cs	2022-01-10 16:02:54.000000000 +0000
@@ -29,7 +29,7 @@
 
             public In(Operation<I, O> op, Func<P, I> mapper, P data)
             {
-                this.__data = new Lazy<IApplyData>(() => op?.__DataIn__(mapper(data)));
+                this.__data = new Lazy<IApplyData>(() => op?.__dataIn(mapper(data)));
             }
 
             public object Value => __data.Value.Value;
@@ -38,27 +38,27 @@
         }
 
 
-        public OperationPartial(Operation<I, O> op, Func<P, I> mapper) : base(op.__Factory__)
+        public OperationPartial(Operation<I, O> op, Func<P, I> mapper) : base(op.Factory)
         {
             Debug.Assert(op != null);
             Debug.Assert(mapper != null);
 
             this.BaseOp = op;
             this.Mapper = mapper;
-            this.__qubits = new Lazy<Qubit[]>(() => op?.__DataIn__(mapper(default(P)))?.Qubits?.ToArray());
+            this.__qubits = new Lazy<Qubit[]>(() => op?.__dataIn(mapper(default(P)))?.Qubits?.ToArray());
         }
 
-        public OperationPartial(Operation<I, O> op, object partialTuple) : base(op.__Factory__)
+        public OperationPartial(Operation<I, O> op, object partialTuple) : base(op.Factory)
         {
             Debug.Assert(op != null);
             Debug.Assert(partialTuple != null);
 
             this.BaseOp = op;
             this.Mapper = PartialMapper.Create<P, I>(partialTuple);
-            this.__qubits = new Lazy<Qubit[]>(() => op?.__DataIn__(this.Mapper(default(P)))?.Qubits?.ToArray());
+            this.__qubits = new Lazy<Qubit[]>(() => op?.__dataIn(this.Mapper(default(P)))?.Qubits?.ToArray());
         }
 
-        public override void __Init__() { }
+        public override void Init() { }
 
         public Operation<I, O> BaseOp { get; }
         ICallable IOperationWrapper.BaseOperation => BaseOp;
@@ -70,39 +70,39 @@
 
         OperationFunctor ICallable.Variant => ((ICallable)this.BaseOp).Variant;
 
-        public override IApplyData __DataIn__(P data) => new In(this.BaseOp, this.Mapper, data);
+        public override IApplyData __dataIn(P data) => new In(this.BaseOp, this.Mapper, data);
 
-        public override IApplyData __DataOut__(O data) => this.BaseOp.__DataOut__(data);
+        public override IApplyData __dataOut(O data) => this.BaseOp.__dataOut(data);
 
-        public override Func<P, O> __Body__ => (a) =>
+        public override Func<P, O> Body => (a) =>
         {
             var args = this.Mapper(a);
-            return this.BaseOp.__Body__.Invoke(args);
+            return this.BaseOp.Body.Invoke(args);
         };
 
-        public override Func<P, QVoid> __AdjointBody__ => (a) =>
+        public override Func<P, QVoid> AdjointBody => (a) =>
         {
             Debug.Assert(typeof(O) == typeof(QVoid));
             var op = this.BaseOp;
 
             var args = this.Mapper(a);
-            return op.__AdjointBody__.Invoke(args);
+            return op.AdjointBody.Invoke(args);
         };
 
-        public override Func<(IQArray<Qubit>, P), QVoid> __ControlledBody__ => (a) =>
+        public override Func<(IQArray<Qubit>, P), QVoid> ControlledBody => (a) =>
         {
             Debug.Assert(typeof(O) == typeof(QVoid));
             var op = this.BaseOp;
             var (ctrl, ps) = a;
-            return op.__ControlledBody__.Invoke((ctrl, this.Mapper(ps)));
+            return op.ControlledBody.Invoke((ctrl, this.Mapper(ps)));
         };
 
-        public override Func<(IQArray<Qubit>, P), QVoid> __ControlledAdjointBody__ => (a) =>
+        public override Func<(IQArray<Qubit>, P), QVoid> ControlledAdjointBody => (a) =>
         {
             Debug.Assert(typeof(O) == typeof(QVoid));
             var op = this.BaseOp;
             var (ctrl, ps) = a;
-            return op.__ControlledAdjointBody__.Invoke((ctrl, this.Mapper(ps)));
+            return op.ControlledAdjointBody.Invoke((ctrl, this.Mapper(ps)));
         };
 
         IEnumerable<Qubit> IApplyData.Qubits => __qubits.Value;
@@ -167,4 +167,4 @@
             public Operation<I, O> Base => _op.BaseOp;
         }
     }
-}
+}
\ No newline at end of file
