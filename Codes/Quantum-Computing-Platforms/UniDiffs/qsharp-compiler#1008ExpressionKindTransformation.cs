--- qsharp-compiler/qsharp-compiler#1008/after/ExpressionKindTransformation.cs	2022-01-10 16:02:54.000000000 +0000
+++ qsharp-compiler/qsharp-compiler#1008/before/ExpressionKindTransformation.cs	2022-01-10 16:02:54.000000000 +0000
@@ -594,7 +594,6 @@
                 {
                     Value comma = CreateConstantString(", ");
                     var openParens = CreateConstantString("[");
-                    UpdateStringRefCount(openParens, 1); // added to avoid dangling pointer in comparison inside loop
                     var outputStr = sharedState.IterateThroughArray(array, openParens, (item, str) =>
                     {
                         var cond = sharedState.CurrentBuilder.Compare(IntPredicate.NotEqual, str!, openParens);
@@ -608,7 +607,6 @@
 
                     outputStr = DoAppend(outputStr, CreateConstantString("]"));
                     UpdateStringRefCount(comma, -1);
-                    UpdateStringRefCount(openParens, -1);
                     return outputStr;
                 }
 
@@ -2096,7 +2094,7 @@
                     else
                     {
                         var parArgsTuple = paArgsType.Resolution.IsUnitType
-                            ? this.SharedState.Values.Unit
+                            ? this.SharedState.Values.FromTuple(parameters[1], ImmutableArray.Create(paArgsType)) // todo: this is a bit hacky...
                             : this.SharedState.AsArgumentTuple(paArgsType, parameters[1]);
                         var typedInnerArg = partialArgs.BuildItem(captureTuple, parArgsTuple);
                         innerArg = typedInnerArg is TupleValue innerArgTuple
