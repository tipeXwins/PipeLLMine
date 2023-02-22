--- qsharp-runtime/qsharp-runtime#349/after/src>Simulation>Simulators>QuantumSimulator>ClassicalControl.cs	2022-01-10 16:02:54.000000000 +0000
+++ qsharp-runtime/qsharp-runtime#349/before/src>Simulation>Simulators>QuantumSimulator>ClassicalControl.cs	2022-01-10 16:02:54.000000000 +0000
@@ -122,7 +122,7 @@
                 this.Simulator = m;
             }
 
-            public override Func<(Result, ICallable, ICallable), QVoid> __Body__ => (q) =>
+            public override Func<(Result, ICallable, ICallable), QVoid> Body => (q) =>
             {
                 (Result measurementResult, ICallable onZero, ICallable onOne) = q;
                 return ExecuteConditionalStatement(measurementResult, onZero, onOne, OperationFunctor.Body, null);
@@ -138,13 +138,13 @@
                 this.Simulator = m;
             }
 
-            public override Func<(Result, IAdjointable, IAdjointable), QVoid> __Body__ => (q) =>
+            public override Func<(Result, IAdjointable, IAdjointable), QVoid> Body => (q) =>
             {
                 (Result measurementResult, ICallable onZero, ICallable onOne) = q;
                 return ExecuteConditionalStatement(measurementResult, onZero, onOne, OperationFunctor.Body, null);
             };
 
-            public override Func<(Result, IAdjointable, IAdjointable), QVoid> __AdjointBody__ => (q) =>
+            public override Func<(Result, IAdjointable, IAdjointable), QVoid> AdjointBody => (q) =>
             {
                 (Result measurementResult, ICallable onZero, ICallable onOne) = q;
                 return ExecuteConditionalStatement(measurementResult, onZero, onOne, OperationFunctor.Adjoint, null);
@@ -160,13 +160,13 @@
                 this.Simulator = m;
             }
 
-            public override Func<(Result, IControllable, IControllable), QVoid> __Body__ => (q) =>
+            public override Func<(Result, IControllable, IControllable), QVoid> Body => (q) =>
             {
                 (Result measurementResult, ICallable onZero, ICallable onOne) = q;
                 return ExecuteConditionalStatement(measurementResult, onZero, onOne, OperationFunctor.Body, null);
             };
 
-            public override Func<(IQArray<Qubit>, (Result, IControllable, IControllable)), QVoid> __ControlledBody__ => (q) =>
+            public override Func<(IQArray<Qubit>, (Result, IControllable, IControllable)), QVoid> ControlledBody => (q) =>
             {
                 (IQArray<Qubit> ctrls, (Result measurementResult, ICallable onZero, ICallable onOne)) = q;
                 OperationFunctor type = AdjustForNoControls(OperationFunctor.Controlled, ctrls);
@@ -183,26 +183,26 @@
                 this.Simulator = m;
             }
 
-            public override Func<(Result, IUnitary, IUnitary), QVoid> __Body__ => (q) =>
+            public override Func<(Result, IUnitary, IUnitary), QVoid> Body => (q) =>
             {
                 (Result measurementResult, ICallable onZero, ICallable onOne) = q;
                 return ExecuteConditionalStatement(measurementResult, onZero, onOne, OperationFunctor.Body, null);
             };
 
-            public override Func<(Result, IUnitary, IUnitary), QVoid> __AdjointBody__ => (q) =>
+            public override Func<(Result, IUnitary, IUnitary), QVoid> AdjointBody => (q) =>
             {
                 (Result measurementResult, ICallable onZero, ICallable onOne) = q;
                 return ExecuteConditionalStatement(measurementResult, onZero, onOne, OperationFunctor.Adjoint, null);
             };
 
-            public override Func<(IQArray<Qubit>, (Result, IUnitary, IUnitary)), QVoid> __ControlledBody__ => (q) =>
+            public override Func<(IQArray<Qubit>, (Result, IUnitary, IUnitary)), QVoid> ControlledBody => (q) =>
             {
                 (IQArray<Qubit> ctrls, (Result measurementResult, ICallable onZero, ICallable onOne)) = q;
                 OperationFunctor type = AdjustForNoControls(OperationFunctor.Controlled, ctrls);
                 return ExecuteConditionalStatement(measurementResult, onZero, onOne, type, ctrls);
             };
 
-            public override Func<(IQArray<Qubit>, (Result, IUnitary, IUnitary)), QVoid> __ControlledAdjointBody__ => (q) =>
+            public override Func<(IQArray<Qubit>, (Result, IUnitary, IUnitary)), QVoid> ControlledAdjointBody => (q) =>
             {
                 (IQArray<Qubit> ctrls, (Result measurementResult, ICallable onZero, ICallable onOne)) = q;
                 OperationFunctor type = AdjustForNoControls(OperationFunctor.ControlledAdjoint, ctrls);
@@ -223,7 +223,7 @@
                 this.Simulator = m;
             }
 
-            public override Func<(IQArray<Result>, IQArray<Result>, ICallable, ICallable), QVoid> __Body__ => (q) =>
+            public override Func<(IQArray<Result>, IQArray<Result>, ICallable, ICallable), QVoid> Body => (q) =>
             {
                 (IQArray<Result> measurementResults, IQArray<Result> comparisonResults, ICallable onEqualOp, ICallable onNonEqualOp) = q;
                 return ExecuteConditionalStatement(measurementResults, comparisonResults, onEqualOp, onNonEqualOp, OperationFunctor.Body, null);
@@ -239,13 +239,13 @@
                 this.Simulator = m;
             }
 
-            public override Func<(IQArray<Result>, IQArray<Result>, IAdjointable, IAdjointable), QVoid> __Body__ => (q) =>
+            public override Func<(IQArray<Result>, IQArray<Result>, IAdjointable, IAdjointable), QVoid> Body => (q) =>
             {
                 (IQArray<Result> measurementResults, IQArray<Result> comparisonResults, ICallable onEqualOp, ICallable onNonEqualOp) = q;
                 return ExecuteConditionalStatement(measurementResults, comparisonResults, onEqualOp, onNonEqualOp, OperationFunctor.Body, null);
             };
 
-            public override Func<(IQArray<Result>, IQArray<Result>, IAdjointable, IAdjointable), QVoid> __AdjointBody__ => (q) =>
+            public override Func<(IQArray<Result>, IQArray<Result>, IAdjointable, IAdjointable), QVoid> AdjointBody => (q) =>
             {
                 (IQArray<Result> measurementResults, IQArray<Result> comparisonResults, ICallable onEqualOp, ICallable onNonEqualOp) = q;
                 return ExecuteConditionalStatement(measurementResults, comparisonResults, onEqualOp, onNonEqualOp, OperationFunctor.Adjoint, null);
@@ -261,13 +261,13 @@
                 this.Simulator = m;
             }
 
-            public override Func<(IQArray<Result>, IQArray<Result>, IControllable, IControllable), QVoid> __Body__ => (q) =>
+            public override Func<(IQArray<Result>, IQArray<Result>, IControllable, IControllable), QVoid> Body => (q) =>
             {
                 (IQArray<Result> measurementResults, IQArray<Result> comparisonResults, ICallable onEqualOp, ICallable onNonEqualOp) = q;
                 return ExecuteConditionalStatement(measurementResults, comparisonResults, onEqualOp, onNonEqualOp, OperationFunctor.Body, null);
             };
 
-            public override Func<(IQArray<Qubit>, (IQArray<Result>, IQArray<Result>, IControllable, IControllable)), QVoid> __ControlledBody__ => (q) =>
+            public override Func<(IQArray<Qubit>, (IQArray<Result>, IQArray<Result>, IControllable, IControllable)), QVoid> ControlledBody => (q) =>
             {
                 (IQArray<Qubit> ctrls, (IQArray<Result> measurementResults, IQArray<Result> comparisonResults, ICallable onEqualOp, ICallable onNonEqualOp)) = q;
                 OperationFunctor type = AdjustForNoControls(OperationFunctor.Controlled, ctrls);
@@ -284,26 +284,26 @@
                 this.Simulator = m;
             }
 
-            public override Func<(IQArray<Result>, IQArray<Result>, IUnitary, IUnitary), QVoid> __Body__ => (q) =>
+            public override Func<(IQArray<Result>, IQArray<Result>, IUnitary, IUnitary), QVoid> Body => (q) =>
             {
                 (IQArray<Result> measurementResults, IQArray<Result> comparisonResults, ICallable onEqualOp, ICallable onNonEqualOp) = q;
                 return ExecuteConditionalStatement(measurementResults, comparisonResults, onEqualOp, onNonEqualOp, OperationFunctor.Body, null);
             };
 
-            public override Func<(IQArray<Result>, IQArray<Result>, IUnitary, IUnitary), QVoid> __AdjointBody__ => (q) =>
+            public override Func<(IQArray<Result>, IQArray<Result>, IUnitary, IUnitary), QVoid> AdjointBody => (q) =>
             {
                 (IQArray<Result> measurementResults, IQArray<Result> comparisonResults, ICallable onEqualOp, ICallable onNonEqualOp) = q;
                 return ExecuteConditionalStatement(measurementResults, comparisonResults, onEqualOp, onNonEqualOp, OperationFunctor.Adjoint, null);
             };
 
-            public override Func<(IQArray<Qubit>, (IQArray<Result>, IQArray<Result>, IUnitary, IUnitary)), QVoid> __ControlledBody__ => (q) =>
+            public override Func<(IQArray<Qubit>, (IQArray<Result>, IQArray<Result>, IUnitary, IUnitary)), QVoid> ControlledBody => (q) =>
             {
                 (IQArray<Qubit> ctrls, (IQArray<Result> measurementResults, IQArray<Result> comparisonResults, ICallable onEqualOp, ICallable onNonEqualOp)) = q;
                 OperationFunctor type = AdjustForNoControls(OperationFunctor.Controlled, ctrls);
                 return ExecuteConditionalStatement(measurementResults, comparisonResults, onEqualOp, onNonEqualOp, type, ctrls);
             };
 
-            public override Func<(IQArray<Qubit>, (IQArray<Result>, IQArray<Result>, IUnitary, IUnitary)), QVoid> __ControlledAdjointBody__ => (q) =>
+            public override Func<(IQArray<Qubit>, (IQArray<Result>, IQArray<Result>, IUnitary, IUnitary)), QVoid> ControlledAdjointBody => (q) =>
             {
                 (IQArray<Qubit> ctrls, (IQArray<Result> measurementResults, IQArray<Result> comparisonResults, ICallable onEqualOp, ICallable onNonEqualOp)) = q;
                 OperationFunctor type = AdjustForNoControls(OperationFunctor.ControlledAdjoint, ctrls);
