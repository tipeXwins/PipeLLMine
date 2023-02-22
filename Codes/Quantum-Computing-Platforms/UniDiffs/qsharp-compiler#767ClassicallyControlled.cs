--- qsharp-compiler/qsharp-compiler#767/after/ClassicallyControlled.cs	2022-01-10 16:02:54.000000000 +0000
+++ qsharp-compiler/qsharp-compiler#767/before/ClassicallyControlled.cs	2022-01-10 16:02:54.000000000 +0000
@@ -160,40 +160,6 @@
                     }
                 }
 
-                private (bool, QsConditionalStatement) ProcessNOT(QsConditionalStatement conditionStatement)
-                {
-                    if (conditionStatement.ConditionalBlocks.Length != 1)
-                    {
-                        return (false, conditionStatement);
-                    }
-                    var (condition, block) = conditionStatement.ConditionalBlocks[0];
-                    if (condition.Expression is ExpressionKind.NOT notCondition)
-                    {
-                        if (conditionStatement.Default.IsValue)
-                        {
-                            return (true, new QsConditionalStatement(
-                                ImmutableArray.Create(Tuple.Create(notCondition.Item, conditionStatement.Default.Item)),
-                                QsNullable<QsPositionedBlock>.NewValue(block)));
-                        }
-                        else
-                        {
-                            var emptyScope = new QsScope(
-                                ImmutableArray<QsStatement>.Empty,
-                                LocalDeclarations.Empty);
-                            var newConditionalBlock = new QsPositionedBlock(
-                                    emptyScope,
-                                    QsNullable<QsLocation>.Null,
-                                    QsComments.Empty);
-                            return (true, new QsConditionalStatement(
-                                ImmutableArray.Create(Tuple.Create(notCondition.Item, newConditionalBlock)),
-                                QsNullable<QsPositionedBlock>.NewValue(block)));
-                        }
-                    }
-                    else
-                    {
-                        return (false, conditionStatement);
-                    }
-                }
                 /// <summary>
                 /// Converts conditional statements to nested structures so they do not
                 /// have elif blocks or top-most OR or AND conditions.
@@ -204,14 +170,13 @@
                     {
                         var stm = condition.Item;
                         (_, stm) = this.ProcessElif(stm);
-                        bool wasOrProcessed, wasAndProcessed, wasNotProcessed;
+                        bool wasOrProcessed, wasAndProcessed;
                         do
                         {
                             (wasOrProcessed, stm) = this.ProcessOR(stm);
                             (wasAndProcessed, stm) = this.ProcessAND(stm);
-                            (wasNotProcessed, stm) = this.ProcessNOT(stm);
                         }
-                        while (wasOrProcessed || wasAndProcessed || wasNotProcessed);
+                        while (wasOrProcessed || wasAndProcessed);
 
                         return new QsStatement(
                             QsStatementKind.NewQsConditionalStatement(stm),
@@ -349,6 +314,36 @@
 
                     return null;
                 }
+                private (TypedExpression Id, TypedExpression Args) GetNoOp()
+                {
+                    var opInfo = BuiltIn.NoOp;
+                    var properties = new[] { OpProperty.Adjointable, OpProperty.Controllable };
+                    var characteristics = new CallableInformation(
+                        ResolvedCharacteristics.FromProperties(properties),
+                        new InferredCallableInformation(((BuiltInKind.Operation)opInfo.Kind).IsSelfAdjoint, false));
+                    var unitType = ResolvedType.New(ResolvedTypeKind.UnitType);
+                    var operationType = ResolvedType.New(ResolvedTypeKind.NewOperation(
+                            Tuple.Create(unitType, unitType),
+                            characteristics));
+                    var args = new TypedExpression(
+                        ExpressionKind.UnitValue,
+                        TypeArgsResolution.Empty,
+                        unitType,
+                        new InferredExpressionInformation(false, false),
+                        QsNullable<Range>.Null);
+                    var typeArgs = ImmutableArray.Create(unitType);
+                    var identifier = new TypedExpression(
+                        ExpressionKind.NewIdentifier(
+                            Identifier.NewGlobalCallable(opInfo.FullName),
+                            QsNullable<ImmutableArray<ResolvedType>>.NewValue(typeArgs)),
+                        typeArgs
+                            .Zip(((BuiltInKind.Operation)opInfo.Kind).TypeParameters, (type, param) => Tuple.Create(opInfo.FullName, param, type))
+                            .ToImmutableArray(),
+                        operationType,
+                        new InferredExpressionInformation(false, false),
+                        QsNullable<Range>.Null);
+                    return (identifier, args);
+                }
 
                 /// <summary>
                 /// Creates a value tuple expression containing the given expressions.
@@ -436,8 +431,8 @@
                         return null; // ToDo: Diagnostic message - inequality block exists, but is not valid
                     }
 
-                    equalityInfo ??= LiftConditionBlocks.GetNoOp();
-                    inequalityInfo ??= LiftConditionBlocks.GetNoOp();
+                    equalityInfo ??= this.GetNoOp();
+                    inequalityInfo ??= this.GetNoOp();
 
                     // Get characteristic properties from global id
                     var props = ImmutableHashSet<OpProperty>.Empty;
@@ -787,36 +782,6 @@
     {
         public static QsCompilation Apply(QsCompilation compilation) =>
             new LiftContent().OnCompilation(compilation);
-        internal static (TypedExpression Id, TypedExpression Args) GetNoOp()
-        {
-            var opInfo = BuiltIn.NoOp;
-            var properties = new[] { OpProperty.Adjointable, OpProperty.Controllable };
-            var characteristics = new CallableInformation(
-                ResolvedCharacteristics.FromProperties(properties),
-                new InferredCallableInformation(((BuiltInKind.Operation)opInfo.Kind).IsSelfAdjoint, false));
-            var unitType = ResolvedType.New(ResolvedTypeKind.UnitType);
-            var operationType = ResolvedType.New(ResolvedTypeKind.NewOperation(
-                    Tuple.Create(unitType, unitType),
-                    characteristics));
-            var args = new TypedExpression(
-                ExpressionKind.UnitValue,
-                TypeArgsResolution.Empty,
-                unitType,
-                new InferredExpressionInformation(false, false),
-                QsNullable<Range>.Null);
-            var typeArgs = ImmutableArray.Create(unitType);
-            var identifier = new TypedExpression(
-                ExpressionKind.NewIdentifier(
-                    Identifier.NewGlobalCallable(opInfo.FullName),
-                    QsNullable<ImmutableArray<ResolvedType>>.NewValue(typeArgs)),
-                typeArgs
-                    .Zip(((BuiltInKind.Operation)opInfo.Kind).TypeParameters, (type, param) => Tuple.Create(opInfo.FullName, param, type))
-                    .ToImmutableArray(),
-                operationType,
-                new InferredExpressionInformation(false, false),
-                QsNullable<Range>.Null);
-            return (identifier, args);
-        }
 
         private class LiftContent : ContentLifting.LiftContent<LiftContent.TransformationState>
         {
@@ -871,30 +836,7 @@
                         // the condition logic for the conversion and using that condition here
                         // var (isExprCondition, _, _) = IsConditionedOnResultLiteralExpression(expr.Item);
 
-                        if (block.Body.Statements.Length == 0)
-                        {
-                            var (id, args) = GetNoOp();
-                            var callExpression = new TypedExpression(
-                                ExpressionKind.NewCallLikeExpression(id, args),
-                                TypeArgsResolution.Empty,
-                                ResolvedType.New(ResolvedTypeKind.UnitType),
-                                new InferredExpressionInformation(false, true),
-                                QsNullable<Range>.Null);
-                            var callStatement = new QsStatement(
-                                QsStatementKind.NewQsExpressionStatement(callExpression),
-                                LocalDeclarations.Empty,
-                                QsNullable<QsLocation>.Null,
-                                QsComments.Empty);
-                            newConditionBlocks.Add(Tuple.Create(
-                                expr.Item,
-                                new QsPositionedBlock(
-                                    new QsScope(
-                                        ImmutableArray.Create(callStatement),
-                                        LocalDeclarations.Empty),
-                                    block.Location,
-                                    block.Comments)));
-                        }
-                        else if (this.IsScopeSingleCall(block.Body))
+                        if (this.IsScopeSingleCall(block.Body))
                         {
                             newConditionBlocks.Add(Tuple.Create(expr.Item, block));
                         }
