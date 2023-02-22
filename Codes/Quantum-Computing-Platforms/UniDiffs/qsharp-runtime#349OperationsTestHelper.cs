--- qsharp-runtime/qsharp-runtime#349/after/OperationsTestHelper.cs	2022-01-10 16:02:54.000000000 +0000
+++ qsharp-runtime/qsharp-runtime#349/before/OperationsTestHelper.cs	2022-01-10 16:02:54.000000000 +0000
@@ -103,10 +103,10 @@
                 this.Log = new Log<string>();
             }
 
-            public override Func<string, QVoid> __Body__ => (tag) => this.Log.Record(OperationFunctor.Body, tag);
-            public override Func<string, QVoid> __AdjointBody__ => (tag) => this.Log.Record(OperationFunctor.Adjoint, tag);
-            public override Func<(IQArray<Qubit>, string), QVoid> __ControlledBody__ => (args) => this.Log.Record(OperationFunctor.Controlled, args.Item2);
-            public override Func<(IQArray<Qubit>, string), QVoid> __ControlledAdjointBody__ => (args) => this.Log.Record(OperationFunctor.ControlledAdjoint, args.Item2);
+            public override Func<string, QVoid> Body => (tag) => this.Log.Record(OperationFunctor.Body, tag);
+            public override Func<string, QVoid> AdjointBody => (tag) => this.Log.Record(OperationFunctor.Adjoint, tag);
+            public override Func<(IQArray<Qubit>, string), QVoid> ControlledBody => (args) => this.Log.Record(OperationFunctor.Controlled, args.Item2);
+            public override Func<(IQArray<Qubit>, string), QVoid> ControlledAdjointBody => (args) => this.Log.Record(OperationFunctor.ControlledAdjoint, args.Item2);
 
             public Log<string> Log { get; }
         }
@@ -118,10 +118,10 @@
                 this.Log = new Log<T>();
             }
 
-            public override Func<T, QVoid> __Body__ => (tag) => this.Log.Record(OperationFunctor.Body, tag);
-            public override Func<T, QVoid> __AdjointBody__ => (tag) => this.Log.Record(OperationFunctor.Adjoint, tag);
-            public override Func<(IQArray<Qubit>, T), QVoid> __ControlledBody__ => (args) => this.Log.Record(OperationFunctor.Controlled, args.Item2);
-            public override Func<(IQArray<Qubit>, T), QVoid> __ControlledAdjointBody__ => (args) => this.Log.Record(OperationFunctor.ControlledAdjoint, args.Item2);
+            public override Func<T, QVoid> Body => (tag) => this.Log.Record(OperationFunctor.Body, tag);
+            public override Func<T, QVoid> AdjointBody => (tag) => this.Log.Record(OperationFunctor.Adjoint, tag);
+            public override Func<(IQArray<Qubit>, T), QVoid> ControlledBody => (args) => this.Log.Record(OperationFunctor.Controlled, args.Item2);
+            public override Func<(IQArray<Qubit>, T), QVoid> ControlledAdjointBody => (args) => this.Log.Record(OperationFunctor.ControlledAdjoint, args.Item2);
 
             public int GetNumberOfCalls(OperationFunctor functor, T tag) => this.Log.GetNumberOfCalls(functor, tag);
 
