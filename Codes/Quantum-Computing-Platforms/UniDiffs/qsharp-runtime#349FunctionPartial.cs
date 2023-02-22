--- qsharp-runtime/qsharp-runtime#349/after/FunctionPartial.cs	2022-01-10 16:02:54.000000000 +0000
+++ qsharp-runtime/qsharp-runtime#349/before/FunctionPartial.cs	2022-01-10 16:02:54.000000000 +0000
@@ -14,7 +14,7 @@
     public class FunctionPartial<P, I, O> : Function<P, O>, ICallable<P, O>
     {
 
-        public FunctionPartial(Function<I, O> op, Func<P, I> mapper) : base(op.__Factory__)
+        public FunctionPartial(Function<I, O> op, Func<P, I> mapper) : base(op.Factory)
         {
             Debug.Assert(op != null);
             Debug.Assert(mapper != null);
@@ -23,7 +23,7 @@
             this.Mapper = mapper;
         }
 
-        public FunctionPartial(Function<I, O> op, object partialTuple) : base(op.__Factory__)
+        public FunctionPartial(Function<I, O> op, object partialTuple) : base(op.Factory)
         {
             Debug.Assert(op != null);
             Debug.Assert(partialTuple != null);
@@ -32,7 +32,7 @@
             this.Mapper = PartialMapper.Create<P, I>(partialTuple);
         }
 
-        public override void __Init__() { }
+        public override void Init() { }
 
         public ICallable<I, O> BaseOp { get; }
 
@@ -43,7 +43,7 @@
 
         OperationFunctor ICallable.Variant => ((ICallable)this.BaseOp).Variant;
 
-        public override Func<P, O> __Body__ => (a) =>
+        public override Func<P, O> Body => (a) =>
         {
             var args = this.Mapper(a);
             return this.BaseOp.Apply(args);
@@ -79,4 +79,4 @@
             public ICallable<I, O> Base => _op.BaseOp;
         }
     }
-}
+}
\ No newline at end of file
