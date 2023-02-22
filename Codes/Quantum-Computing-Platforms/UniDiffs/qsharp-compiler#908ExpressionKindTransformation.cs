--- qsharp-compiler/qsharp-compiler#908/after/ExpressionKindTransformation.cs	2022-01-10 16:02:54.000000000 +0000
+++ qsharp-compiler/qsharp-compiler#908/before/ExpressionKindTransformation.cs	2022-01-10 16:02:54.000000000 +0000
@@ -127,10 +127,6 @@
 
         // static methods
 
-        private static bool ExpressionIsSelfEvaluating(TypedExpression ex) =>
-            ex.Expression.IsIdentifier || ex.Expression.IsBoolLiteral || ex.Expression.IsDoubleLiteral
-                || ex.Expression.IsIntLiteral || ex.Expression.IsPauliLiteral || ex.Expression.IsRangeLiteral
-                || ex.Expression.IsResultLiteral || ex.Expression.IsUnitValue;
         /// <summary>
         /// Determines the location of the item with the given name within the tuple of type items.
         /// The returned list contains the index of the item starting from the outermost tuple
@@ -382,43 +378,6 @@
         }
 
         // private helpers
-        private Value ConditionalEvaluation(Value condition, TypedExpression? onCondTrue = null, TypedExpression? onCondFalse = null)
-        {
-            var contBlock = this.SharedState.AddBlockAfterCurrent("condContinue");
-            var falseBlock = onCondFalse != null
-                ? this.SharedState.AddBlockAfterCurrent("condFalse")
-                : contBlock;
-            var trueBlock = onCondTrue != null
-                ? this.SharedState.AddBlockAfterCurrent("condTrue")
-                : contBlock;
-            this.SharedState.CurrentBuilder.Branch(condition, trueBlock, falseBlock);
-            var entryBlock = this.SharedState.CurrentBlock!;
-            var (evaluatedOnTrue, afterTrue) = (condition, entryBlock);
-            if (onCondTrue != null)
-            {
-                this.SharedState.ScopeMgr.OpenScope();
-                this.SharedState.SetCurrentBlock(trueBlock);
-                var onTrue = this.SharedState.EvaluateSubexpression(onCondTrue);
-                this.SharedState.ScopeMgr.CloseScope(onTrue, false); // force that the ref count is increased within the branch
-                this.SharedState.CurrentBuilder.Branch(contBlock);
-                (evaluatedOnTrue, afterTrue) = (onTrue.Value, this.SharedState.CurrentBlock!);
-            }
-            var (evaluatedOnFalse, afterFalse) = (condition, entryBlock);
-            if (onCondFalse != null)
-            {
-                this.SharedState.ScopeMgr.OpenScope();
-                this.SharedState.SetCurrentBlock(falseBlock);
-                var onFalse = this.SharedState.EvaluateSubexpression(onCondFalse);
-                this.SharedState.ScopeMgr.CloseScope(onFalse, false); // force that the ref count is increased within the branch
-                this.SharedState.CurrentBuilder.Branch(contBlock);
-                (evaluatedOnFalse, afterFalse) = (onFalse.Value, this.SharedState.CurrentBlock!);
-            }
-            this.SharedState.SetCurrentBlock(contBlock);
-            var phi = this.SharedState.CurrentBuilder.PhiNode(this.SharedState.CurrentLlvmExpressionType());
-            phi.AddIncoming(evaluatedOnTrue, afterTrue);
-            phi.AddIncoming(evaluatedOnFalse, afterFalse);
-            return phi;
-        }
 
         /// <summary>
         /// Handles calls to specific functor specializations of global callables.
@@ -890,6 +849,10 @@
 
         public override ResolvedExpressionKind OnConditionalExpression(TypedExpression condEx, TypedExpression ifTrueEx, TypedExpression ifFalseEx)
         {
+            static bool ExpressionIsSelfEvaluating(TypedExpression ex) =>
+                ex.Expression.IsIdentifier || ex.Expression.IsBoolLiteral || ex.Expression.IsDoubleLiteral
+                    || ex.Expression.IsIntLiteral || ex.Expression.IsPauliLiteral || ex.Expression.IsRangeLiteral
+                    || ex.Expression.IsResultLiteral || ex.Expression.IsUnitValue;
             var cond = this.SharedState.EvaluateSubexpression(condEx);
             var exType = this.SharedState.CurrentExpressionType();
             IValue value;
@@ -905,8 +868,29 @@
             }
             else
             {
-                var evaluated = this.ConditionalEvaluation(cond.Value, onCondTrue: ifTrueEx, onCondFalse: ifFalseEx);
-                value = this.SharedState.Values.From(evaluated, exType);
+                var contBlock = this.SharedState.AddBlockAfterCurrent("condContinue");
+                var falseBlock = this.SharedState.AddBlockAfterCurrent("condFalse");
+                var trueBlock = this.SharedState.AddBlockAfterCurrent("condTrue");
+                this.SharedState.CurrentBuilder.Branch(cond.Value, trueBlock, falseBlock);
+                this.SharedState.ScopeMgr.OpenScope();
+                this.SharedState.SetCurrentBlock(trueBlock);
+                this.Transformation.Expressions.OnTypedExpression(ifTrueEx);
+                var ifTrue = this.SharedState.ValueStack.Pop();
+                this.SharedState.ScopeMgr.CloseScope(ifTrue, false); // force that the ref count is increased within the branch
+                BasicBlock afterTrue = this.SharedState.CurrentBlock!;
+                this.SharedState.CurrentBuilder.Branch(contBlock);
+                this.SharedState.ScopeMgr.OpenScope();
+                this.SharedState.SetCurrentBlock(falseBlock);
+                this.Transformation.Expressions.OnTypedExpression(ifFalseEx);
+                var ifFalse = this.SharedState.ValueStack.Pop();
+                this.SharedState.ScopeMgr.CloseScope(ifFalse, false); // force that the ref count is increased within the branch
+                BasicBlock afterFalse = this.SharedState.CurrentBlock!;
+                this.SharedState.CurrentBuilder.Branch(contBlock);
+                this.SharedState.SetCurrentBlock(contBlock);
+                var phi = this.SharedState.CurrentBuilder.PhiNode(this.SharedState.CurrentLlvmExpressionType());
+                phi.AddIncoming(ifTrue.Value, afterTrue);
+                phi.AddIncoming(ifFalse.Value, afterFalse);
+                value = this.SharedState.Values.From(phi, exType);
                 this.SharedState.ScopeMgr.RegisterValue(value);
             }
 
@@ -1329,20 +1313,11 @@
 
         public override ResolvedExpressionKind OnLogicalAnd(TypedExpression lhsEx, TypedExpression rhsEx)
         {
-            Value evaluated;
+            var lhs = this.SharedState.EvaluateSubexpression(lhsEx);
+            var rhs = this.SharedState.EvaluateSubexpression(rhsEx);
             var exType = this.SharedState.CurrentExpressionType();
-            if (ExpressionIsSelfEvaluating(rhsEx))
-            {
-                var lhs = this.SharedState.EvaluateSubexpression(lhsEx);
-                var rhs = this.SharedState.EvaluateSubexpression(rhsEx);
-                evaluated = this.SharedState.CurrentBuilder.And(lhs.Value, rhs.Value);
-            }
-            else
-            {
-                var cond = this.SharedState.EvaluateSubexpression(lhsEx).Value;
-                evaluated = this.ConditionalEvaluation(cond, onCondTrue: rhsEx);
-            }
-            var value = this.SharedState.Values.FromSimpleValue(evaluated, exType);
+            var res = this.SharedState.CurrentBuilder.And(lhs.Value, rhs.Value);
+            var value = this.SharedState.Values.FromSimpleValue(res, exType);
             this.SharedState.ValueStack.Push(value);
             return ResolvedExpressionKind.InvalidExpr;
         }
@@ -1360,20 +1335,11 @@
 
         public override ResolvedExpressionKind OnLogicalOr(TypedExpression lhsEx, TypedExpression rhsEx)
         {
-            Value evaluated;
+            var lhs = this.SharedState.EvaluateSubexpression(lhsEx);
+            var rhs = this.SharedState.EvaluateSubexpression(rhsEx);
             var exType = this.SharedState.CurrentExpressionType();
-            if (ExpressionIsSelfEvaluating(rhsEx))
-            {
-                var lhs = this.SharedState.EvaluateSubexpression(lhsEx);
-                var rhs = this.SharedState.EvaluateSubexpression(rhsEx);
-                evaluated = this.SharedState.CurrentBuilder.Or(lhs.Value, rhs.Value);
-            }
-            else
-            {
-                var cond = this.SharedState.EvaluateSubexpression(lhsEx).Value;
-                evaluated = this.ConditionalEvaluation(cond, onCondFalse: rhsEx);
-            }
-            var value = this.SharedState.Values.FromSimpleValue(evaluated, exType);
+            var res = this.SharedState.CurrentBuilder.Or(lhs.Value, rhs.Value);
+            var value = this.SharedState.Values.FromSimpleValue(res, exType);
             this.SharedState.ValueStack.Push(value);
             return ResolvedExpressionKind.InvalidExpr;
         }
