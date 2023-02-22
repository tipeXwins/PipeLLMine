--- qsharp-compiler/qsharp-compiler#880/after/Monomorphization.cs	2022-01-10 16:02:54.000000000 +0000
+++ qsharp-compiler/qsharp-compiler#880/before/Monomorphization.cs	2022-01-10 16:02:54.000000000 +0000
@@ -101,12 +101,7 @@
         {
             public static QsCompilation Apply(QsCompilation compilation, List<QsCallable> callables, ImmutableHashSet<QsQualifiedName> intrinsicCallableSet, bool keepAllIntrinsics)
             {
-                var filter = new ResolveGenerics(
-                    callables
-                        .Where(call => !keepAllIntrinsics || !intrinsicCallableSet.Contains(call.FullName))
-                        .ToLookup(res => res.FullName.Namespace),
-                    intrinsicCallableSet,
-                    keepAllIntrinsics);
+                var filter = new ResolveGenerics(callables.ToLookup(res => res.FullName.Namespace), intrinsicCallableSet, keepAllIntrinsics);
 
                 return filter.OnCompilation(compilation);
             }
