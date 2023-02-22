--- qsharp-runtime/qsharp-runtime#349/after/src>Simulation>Simulators>QuantumProcessor>ClassicalControl.cs	2022-01-10 16:02:54.000000000 +0000
+++ qsharp-runtime/qsharp-runtime#349/before/src>Simulation>Simulators>QuantumProcessor>ClassicalControl.cs	2022-01-10 16:02:54.000000000 +0000
@@ -89,7 +89,7 @@
 
             public QuantumProcessorApplyIfElse(QuantumProcessorDispatcher m) : base(m) { this.Simulator = m; }
 
-            public override Func<(Result, ICallable, ICallable), QVoid> __Body__ => (q) =>
+            public override Func<(Result, ICallable, ICallable), QVoid> Body => (q) =>
             {
                 (Result measurementResult, ICallable onZero, ICallable onOne) = q;
                 return ExecuteConditionalStatement(Simulator, measurementResult, Result.Zero, onZero, onOne, OperationFunctor.Body, null);
@@ -102,13 +102,13 @@
 
             public QuantumProcessorApplyIfElseA(QuantumProcessorDispatcher m) : base(m) { this.Simulator = m; }
 
-            public override Func<(Result, IAdjointable, IAdjointable), QVoid> __Body__ => (q) =>
+            public override Func<(Result, IAdjointable, IAdjointable), QVoid> Body => (q) =>
             {
                 (Result measurementResult, ICallable onZero, ICallable onOne) = q;
                 return ExecuteConditionalStatement(Simulator, measurementResult, Result.Zero, onZero, onOne, OperationFunctor.Body, null);
             };
 
-            public override Func<(Result, IAdjointable, IAdjointable), QVoid> __AdjointBody__ => (q) =>
+            public override Func<(Result, IAdjointable, IAdjointable), QVoid> AdjointBody => (q) =>
             {
                 (Result measurementResult, ICallable onZero, ICallable onOne) = q;
                 return ExecuteConditionalStatement(Simulator, measurementResult, Result.Zero, onZero, onOne, OperationFunctor.Adjoint, null);
@@ -121,13 +121,13 @@
 
             public QuantumProcessorApplyIfElseC(QuantumProcessorDispatcher m) : base(m) { this.Simulator = m; }
 
-            public override Func<(Result, IControllable, IControllable), QVoid> __Body__ => (q) =>
+            public override Func<(Result, IControllable, IControllable), QVoid> Body => (q) =>
             {
                 (Result measurementResult, ICallable onZero, ICallable onOne) = q;
                 return ExecuteConditionalStatement(Simulator, measurementResult, Result.Zero, onZero, onOne, OperationFunctor.Body, null);
             };
 
-            public override Func<(IQArray<Qubit>, (Result, IControllable, IControllable)), QVoid> __ControlledBody__ => (q) =>
+            public override Func<(IQArray<Qubit>, (Result, IControllable, IControllable)), QVoid> ControlledBody => (q) =>
             {
                 (IQArray<Qubit> ctrls, (Result measurementResult, ICallable onZero, ICallable onOne)) = q;
                 if ((ctrls == null) || (ctrls.Count == 0))
@@ -147,19 +147,19 @@
 
             public QuantumProcessorApplyIfElseCA(QuantumProcessorDispatcher m) : base(m) { this.Simulator = m; }
 
-            public override Func<(Result, IUnitary, IUnitary), QVoid> __Body__ => (q) =>
+            public override Func<(Result, IUnitary, IUnitary), QVoid> Body => (q) =>
             {
                 (Result measurementResult, ICallable onZero, ICallable onOne) = q;
                 return ExecuteConditionalStatement(Simulator, measurementResult, Result.Zero, onZero, onOne, OperationFunctor.Body, null);
             };
 
-            public override Func<(Result, IUnitary, IUnitary), QVoid> __AdjointBody__ => (q) =>
+            public override Func<(Result, IUnitary, IUnitary), QVoid> AdjointBody => (q) =>
             {
                 (Result measurementResult, ICallable onZero, ICallable onOne) = q;
                 return ExecuteConditionalStatement(Simulator, measurementResult, Result.Zero, onZero, onOne, OperationFunctor.Adjoint, null);
             };
 
-            public override Func<(IQArray<Qubit>, (Result, IUnitary, IUnitary)), QVoid> __ControlledBody__ => (q) =>
+            public override Func<(IQArray<Qubit>, (Result, IUnitary, IUnitary)), QVoid> ControlledBody => (q) =>
             {
                 (IQArray<Qubit> ctrls, (Result measurementResult, ICallable onZero, ICallable onOne)) = q;
 
@@ -173,7 +173,7 @@
                 }
             };
 
-            public override Func<(IQArray<Qubit>, (Result, IUnitary, IUnitary)), QVoid> __ControlledAdjointBody__ => (q) =>
+            public override Func<(IQArray<Qubit>, (Result, IUnitary, IUnitary)), QVoid> ControlledAdjointBody => (q) =>
             {
                 (IQArray<Qubit> ctrls, (Result measurementResult, ICallable onZero, ICallable onOne)) = q;
 
@@ -196,7 +196,7 @@
 
             public QuantumProcessorApplyConditionally(QuantumProcessorDispatcher m) : base(m) { this.Simulator = m; }
 
-            public override Func<(IQArray<Result>, IQArray<Result>, ICallable, ICallable), QVoid> __Body__ => (q) =>
+            public override Func<(IQArray<Result>, IQArray<Result>, ICallable, ICallable), QVoid> Body => (q) =>
             {
                 (IQArray<Result> measurementResults, IQArray<Result> resultsValues, ICallable onEqualOp, ICallable onNonEqualOp) = q;
                 return ExecuteConditionalStatement(Simulator, measurementResults, resultsValues, onEqualOp, onNonEqualOp, OperationFunctor.Body, null);
@@ -209,13 +209,13 @@
 
             public QuantumProcessorApplyConditionallyA(QuantumProcessorDispatcher m) : base(m) { this.Simulator = m; }
 
-            public override Func<(IQArray<Result>, IQArray<Result>, IAdjointable, IAdjointable), QVoid> __Body__ => (q) =>
+            public override Func<(IQArray<Result>, IQArray<Result>, IAdjointable, IAdjointable), QVoid> Body => (q) =>
             {
                 (IQArray<Result> measurementResults, IQArray<Result> resultsValues, ICallable onEqualOp, ICallable onNonEqualOp) = q;
                 return ExecuteConditionalStatement(Simulator, measurementResults, resultsValues, onEqualOp, onNonEqualOp, OperationFunctor.Body, null);
             };
 
-            public override Func<(IQArray<Result>, IQArray<Result>, IAdjointable, IAdjointable), QVoid> __AdjointBody__ => (q) =>
+            public override Func<(IQArray<Result>, IQArray<Result>, IAdjointable, IAdjointable), QVoid> AdjointBody => (q) =>
             {
                 (IQArray<Result> measurementResults, IQArray<Result> resultsValues, ICallable onEqualOp, ICallable onNonEqualOp) = q;
                 return ExecuteConditionalStatement(Simulator, measurementResults, resultsValues, onEqualOp, onNonEqualOp, OperationFunctor.Adjoint, null);
@@ -228,13 +228,13 @@
 
             public QuantumProcessorApplyConditionallyC(QuantumProcessorDispatcher m) : base(m) { this.Simulator = m; }
 
-            public override Func<(IQArray<Result>, IQArray<Result>, IControllable, IControllable), QVoid> __Body__ => (q) =>
+            public override Func<(IQArray<Result>, IQArray<Result>, IControllable, IControllable), QVoid> Body => (q) =>
             {
                 (IQArray<Result> measurementResults, IQArray<Result> resultsValues, ICallable onEqualOp, ICallable onNonEqualOp) = q;
                 return ExecuteConditionalStatement(Simulator, measurementResults, resultsValues, onEqualOp, onNonEqualOp, OperationFunctor.Body, null);
             };
 
-            public override Func<(IQArray<Qubit>, (IQArray<Result>, IQArray<Result>, IControllable, IControllable)), QVoid> __ControlledBody__ => (q) =>
+            public override Func<(IQArray<Qubit>, (IQArray<Result>, IQArray<Result>, IControllable, IControllable)), QVoid> ControlledBody => (q) =>
             {
                 (IQArray<Qubit> ctrls, (IQArray<Result> measurementResults, IQArray<Result> resultsValues, ICallable onEqualOp, ICallable onNonEqualOp)) = q;
 
@@ -255,19 +255,19 @@
 
             public QuantumProcessorApplyConditionallyCA(QuantumProcessorDispatcher m) : base(m) { this.Simulator = m; }
 
-            public override Func<(IQArray<Result>, IQArray<Result>, IUnitary, IUnitary), QVoid> __Body__ => (q) =>
+            public override Func<(IQArray<Result>, IQArray<Result>, IUnitary, IUnitary), QVoid> Body => (q) =>
             {
                 (IQArray<Result> measurementResults, IQArray<Result> resultsValues, ICallable onEqualOp, ICallable onNonEqualOp) = q;
                 return ExecuteConditionalStatement(Simulator, measurementResults, resultsValues, onEqualOp, onNonEqualOp, OperationFunctor.Body, null);
             };
 
-            public override Func<(IQArray<Result>, IQArray<Result>, IUnitary, IUnitary), QVoid> __AdjointBody__ => (q) =>
+            public override Func<(IQArray<Result>, IQArray<Result>, IUnitary, IUnitary), QVoid> AdjointBody => (q) =>
             {
                 (IQArray<Result> measurementResults, IQArray<Result> resultsValues, ICallable onEqualOp, ICallable onNonEqualOp) = q;
                 return ExecuteConditionalStatement(Simulator, measurementResults, resultsValues, onEqualOp, onNonEqualOp, OperationFunctor.Adjoint, null);
             };
 
-            public override Func<(IQArray<Qubit>, (IQArray<Result>, IQArray<Result>, IUnitary, IUnitary)), QVoid> __ControlledBody__ => (q) =>
+            public override Func<(IQArray<Qubit>, (IQArray<Result>, IQArray<Result>, IUnitary, IUnitary)), QVoid> ControlledBody => (q) =>
             {
                 (IQArray<Qubit> ctrls, (IQArray<Result> measurementResults, IQArray<Result> resultsValues, ICallable onEqualOp, ICallable onNonEqualOp)) = q;
 
@@ -281,7 +281,7 @@
                 }
             };
 
-            public override Func<(IQArray<Qubit>, (IQArray<Result>, IQArray<Result>, IUnitary, IUnitary)), QVoid> __ControlledAdjointBody__ => (q) =>
+            public override Func<(IQArray<Qubit>, (IQArray<Result>, IQArray<Result>, IUnitary, IUnitary)), QVoid> ControlledAdjointBody => (q) =>
             {
                 (IQArray<Qubit> ctrls, (IQArray<Result> measurementResults, IQArray<Result> resultsValues, ICallable onEqualOp, ICallable onNonEqualOp)) = q;
 
