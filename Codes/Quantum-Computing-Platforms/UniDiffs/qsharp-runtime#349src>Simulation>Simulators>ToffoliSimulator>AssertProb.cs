--- qsharp-runtime/qsharp-runtime#349/after/src>Simulation>Simulators>ToffoliSimulator>AssertProb.cs	2022-01-10 16:02:54.000000000 +0000
+++ qsharp-runtime/qsharp-runtime#349/before/src>Simulation>Simulators>ToffoliSimulator>AssertProb.cs	2022-01-10 16:02:54.000000000 +0000
@@ -29,7 +29,7 @@
             /// <summary>
             /// The implementation of the operation.
             /// </summary>
-            public override Func<(IQArray<Pauli>, IQArray<Qubit>, Result, double, string, double), QVoid> __Body__ => (_args) =>
+            public override Func<(IQArray<Pauli>, IQArray<Qubit>, Result, double, string, double), QVoid> Body => (_args) =>
             {
 
                 Qubit? f(Pauli p, Qubit q) =>
@@ -82,19 +82,19 @@
             /// The implementation of the adjoint specialization of the operation.
             /// The current definition is that this is a no-op.
             /// </summary>
-            public override Func<(IQArray<Pauli>, IQArray<Qubit>, Result, double, string, double), QVoid> __AdjointBody__ => (_args) => { return QVoid.Instance; };
+            public override Func<(IQArray<Pauli>, IQArray<Qubit>, Result, double, string, double), QVoid> AdjointBody => (_args) => { return QVoid.Instance; };
 
             /// <summary>
             /// The implementation of the controlled specialization of the operation.
             /// The current definition is that this is a no-op.
             /// </summary>
-            public override Func<(IQArray<Qubit>, (IQArray<Pauli>, IQArray<Qubit>, Result, double, string, double)), QVoid> __ControlledBody__ => (_args) => { return QVoid.Instance; };
+            public override Func<(IQArray<Qubit>, (IQArray<Pauli>, IQArray<Qubit>, Result, double, string, double)), QVoid> ControlledBody => (_args) => { return QVoid.Instance; };
 
             /// <summary>
             /// The implementation of the controlled adjoint specialization of the operation.
             /// The current definition is that this is a no-op.
             /// </summary>
-            public override Func<(IQArray<Qubit>, (IQArray<Pauli>, IQArray<Qubit>, Result, double, string, double)), QVoid> __ControlledAdjointBody__ => (_args) => { return QVoid.Instance; };
+            public override Func<(IQArray<Qubit>, (IQArray<Pauli>, IQArray<Qubit>, Result, double, string, double)), QVoid> ControlledAdjointBody => (_args) => { return QVoid.Instance; };
         }
     }
 }
