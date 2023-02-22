--- qsharp-runtime/qsharp-runtime#349/after/QCTraceSimulator.Primitive.Assert.cs	2022-01-10 16:02:54.000000000 +0000
+++ qsharp-runtime/qsharp-runtime#349/before/QCTraceSimulator.Primitive.Assert.cs	2022-01-10 16:02:54.000000000 +0000
@@ -17,7 +17,7 @@
                 core = m.tracingCore;
             }
 
-            public override Func<(IQArray<Pauli>, IQArray<Qubit>, Result, string), QVoid> __Body__
+            public override Func<(IQArray<Pauli>, IQArray<Qubit>, Result, string), QVoid> Body
                 => (arg) =>
                 {
                     (IQArray<Pauli> observable, IQArray<Qubit> target, Result result, string msg) = arg;
@@ -25,11 +25,11 @@
                     return QVoid.Instance;
                 };
 
-            public override Func<(IQArray<Pauli>, IQArray<Qubit>, Result, string), QVoid> __AdjointBody__ => (_args) => { return QVoid.Instance; };
+            public override Func<(IQArray<Pauli>, IQArray<Qubit>, Result, string), QVoid> AdjointBody => (_args) => { return QVoid.Instance; };
 
-            public override Func<(IQArray<Qubit>, (IQArray<Pauli>, IQArray<Qubit>, Result, string)), QVoid> __ControlledBody__ => (_args) => { return QVoid.Instance; };
+            public override Func<(IQArray<Qubit>, (IQArray<Pauli>, IQArray<Qubit>, Result, string)), QVoid> ControlledBody => (_args) => { return QVoid.Instance; };
 
-            public override Func<(IQArray<Qubit>, (IQArray<Pauli>, IQArray<Qubit>, Result, string)), QVoid> __ControlledAdjointBody__ => (_args) => { return QVoid.Instance; };
+            public override Func<(IQArray<Qubit>, (IQArray<Pauli>, IQArray<Qubit>, Result, string)), QVoid> ControlledAdjointBody => (_args) => { return QVoid.Instance; };
         }
     }
-}
+}
\ No newline at end of file
