--- qsharp-runtime/qsharp-runtime#349/after/GetQubitsTests.cs	2022-01-10 16:02:54.000000000 +0000
+++ qsharp-runtime/qsharp-runtime#349/before/GetQubitsTests.cs	2022-01-10 16:02:54.000000000 +0000
@@ -22,27 +22,27 @@
     {
         public UnitaryNoOp() : base(null) { }
 
-        public override void __Init__() { }
+        public override void Init() { }
 
-        public override Func<(IQArray<Qubit>, TInput), QVoid> __ControlledAdjointBody__ => (arg) =>
+        public override Func<(IQArray<Qubit>, TInput), QVoid> ControlledAdjointBody => (arg) =>
         {
             Debug.Write("NoOp:ControlledAdjointBody:" + typeof(TInput).FullName);
             return QVoid.Instance;
         };
 
-        public override Func<TInput, QVoid> __AdjointBody__ => (arg) =>
+        public override Func<TInput, QVoid> AdjointBody => (arg) =>
         {
             Debug.Write("NoOp:AdjointBody:" + typeof(TInput).FullName);
             return QVoid.Instance;
         };
 
-        public override Func<(IQArray<Qubit>, TInput), QVoid> __ControlledBody__ => (arg) =>
+        public override Func<(IQArray<Qubit>, TInput), QVoid> ControlledBody => (arg) =>
         {
             Debug.Write("NoOp:ControlledBody:" + typeof(TInput).FullName);
             return QVoid.Instance;
         };
 
-        public override Func<TInput, QVoid> __Body__ => (TInput arg) =>
+        public override Func<TInput, QVoid> Body => (TInput arg) =>
         {
             Debug.Write("NoOp:Body:" + typeof(TInput).FullName);
             return QVoid.Instance;
@@ -392,4 +392,4 @@
             AssertEnumerable(expected, d.Qubits);
         }
     }
-}
+}
\ No newline at end of file
