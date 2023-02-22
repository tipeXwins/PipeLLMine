--- qsharp-compiler/qsharp-compiler#809/after/ConcreteCallGraphWalker.cs	2022-01-10 16:02:54.000000000 +0000
+++ qsharp-compiler/qsharp-compiler#809/before/ConcreteCallGraphWalker.cs	2022-01-10 16:02:54.000000000 +0000
@@ -39,11 +39,8 @@
             /// </summary>
             public static void PopulateConcreteGraph(ConcreteGraphBuilder graph, QsCompilation compilation)
             {
-                var globals = compilation.Namespaces.GlobalCallableResolutions();
                 var walker = new BuildGraph(graph);
-                var entryPointNodes = compilation.EntryPoints.SelectMany(name =>
-                    GetSpecializationKinds(globals, name).Select(kind =>
-                        new ConcreteCallGraphNode(name, kind, TypeParameterResolutions.Empty)));
+                var entryPointNodes = compilation.EntryPoints.Select(name => new ConcreteCallGraphNode(name, QsSpecializationKind.QsBody, TypeParameterResolutions.Empty));
                 foreach (var entryPoint in entryPointNodes)
                 {
                     // Make sure all the entry points are added to the graph
@@ -51,6 +48,7 @@
                     walker.SharedState.RequestStack.Push(entryPoint);
                 }
 
+                var globals = compilation.Namespaces.GlobalCallableResolutions();
                 while (walker.SharedState.RequestStack.TryPop(out var currentRequest))
                 {
                     // If there is a call to an unknown callable, throw exception
@@ -258,15 +256,9 @@
                     var called = new ConcreteCallGraphNode(identifier, kind, typeRes);
                     var edge = new ConcreteCallGraphEdge(referenceRange);
                     this.Graph.AddDependency(this.CurrentNode, called, edge);
-                    var newNodes = this.GetSpecializationKinds(identifier)
-                        .Select(specKind => new ConcreteCallGraphNode(identifier, specKind, typeRes));
-                    foreach (var node in newNodes)
+                    if (!this.RequestStack.Contains(called) && !this.ResolvedNodeSet.Contains(called))
                     {
-                        if (!this.RequestStack.Contains(node) && !this.ResolvedNodeSet.Contains(node))
-                        {
-                            this.Graph.AddNode(node);
-                            this.RequestStack.Push(node);
-                        }
+                        this.RequestStack.Push(called);
                     }
                 }
             }
