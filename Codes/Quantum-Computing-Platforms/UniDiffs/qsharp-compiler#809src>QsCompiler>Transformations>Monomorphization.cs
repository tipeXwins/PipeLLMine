--- qsharp-compiler/qsharp-compiler#809/after/src>QsCompiler>Transformations>Monomorphization.cs	2022-01-10 16:02:54.000000000 +0000
+++ qsharp-compiler/qsharp-compiler#809/before/src>QsCompiler>Transformations>Monomorphization.cs	2022-01-10 16:02:54.000000000 +0000
@@ -34,7 +34,7 @@
         /// <summary>
         /// Performs Monomorphization on the given compilation.
         /// </summary>
-        public static QsCompilation Apply(QsCompilation compilation, bool keepAllIntrinsics = true)
+        public static QsCompilation Apply(QsCompilation compilation)
         {
             var globals = compilation.Namespaces.GlobalCallableResolutions();
             var concretizations = new List<QsCallable>();
@@ -66,9 +66,7 @@
 
                     // Generate the concrete version of the callable
                     var concrete = ReplaceTypeParamImplementations.Apply(originalGlobal, node.ParamResolutions, getAccessModifiers);
-                    concretizations.Add(
-                        concrete.WithFullName(oldName => concreteName)
-                        .WithSpecializations(specs => specs.Select(spec => spec.WithParent(_ => concreteName)).ToImmutableArray()));
+                    concretizations.Add(concrete.WithFullName(oldName => concreteName));
                 }
                 else
                 {
@@ -91,16 +89,16 @@
                 final.Add(ReplaceTypeParamCalls.Apply(callable, getConcreteIdentifier, intrinsicCallableSet));
             }
 
-            return ResolveGenerics.Apply(compilation, final, intrinsicCallableSet, keepAllIntrinsics);
+            return ResolveGenerics.Apply(compilation, final, intrinsicCallableSet);
         }
 
         #region ResolveGenerics
 
         private class ResolveGenerics : SyntaxTreeTransformation<ResolveGenerics.TransformationState>
         {
-            public static QsCompilation Apply(QsCompilation compilation, List<QsCallable> callables, ImmutableHashSet<QsQualifiedName> intrinsicCallableSet, bool keepAllIntrinsics)
+            public static QsCompilation Apply(QsCompilation compilation, List<QsCallable> callables, ImmutableHashSet<QsQualifiedName> intrinsicCallableSet)
             {
-                var filter = new ResolveGenerics(callables.ToLookup(res => res.FullName.Namespace), intrinsicCallableSet, keepAllIntrinsics);
+                var filter = new ResolveGenerics(callables.ToLookup(res => res.FullName.Namespace), intrinsicCallableSet);
 
                 return filter.OnCompilation(compilation);
             }
@@ -109,13 +107,11 @@
             {
                 public readonly ILookup<string, QsCallable> NamespaceCallables;
                 public readonly ImmutableHashSet<QsQualifiedName> IntrinsicCallableSet;
-                public readonly bool KeepAllIntrinsics;
 
-                public TransformationState(ILookup<string, QsCallable> namespaceCallables, ImmutableHashSet<QsQualifiedName> intrinsicCallableSet, bool keepAllIntrinsics)
+                public TransformationState(ILookup<string, QsCallable> namespaceCallables, ImmutableHashSet<QsQualifiedName> intrinsicCallableSet)
                 {
                     this.NamespaceCallables = namespaceCallables;
                     this.IntrinsicCallableSet = intrinsicCallableSet;
-                    this.KeepAllIntrinsics = keepAllIntrinsics;
                 }
             }
 
@@ -123,8 +119,8 @@
             /// Constructor for the ResolveGenericsSyntax class. Its transform function replaces global callables in the namespace.
             /// </summary>
             /// <param name="namespaceCallables">Maps namespace names to an enumerable of all global callables in that namespace.</param>
-            private ResolveGenerics(ILookup<string, QsCallable> namespaceCallables, ImmutableHashSet<QsQualifiedName> intrinsicCallableSet, bool keepAllIntrinsics)
-                : base(new TransformationState(namespaceCallables, intrinsicCallableSet, keepAllIntrinsics))
+            private ResolveGenerics(ILookup<string, QsCallable> namespaceCallables, ImmutableHashSet<QsQualifiedName> intrinsicCallableSet)
+                : base(new TransformationState(namespaceCallables, intrinsicCallableSet))
             {
                 this.Namespaces = new NamespaceTransformation(this);
                 this.Statements = new StatementTransformation<TransformationState>(this, TransformationOptions.Disabled);
@@ -142,8 +138,7 @@
                 {
                     if (elem is QsNamespaceElement.QsCallable call)
                     {
-                        return BuiltIn.RewriteStepDependencies.Contains(call.Item.FullName) ||
-                            (this.SharedState.KeepAllIntrinsics && this.SharedState.IntrinsicCallableSet.Contains(call.Item.FullName));
+                        return BuiltIn.RewriteStepDependencies.Contains(call.Item.FullName) || this.SharedState.IntrinsicCallableSet.Contains(call.Item.FullName);
                     }
                     else
                     {
