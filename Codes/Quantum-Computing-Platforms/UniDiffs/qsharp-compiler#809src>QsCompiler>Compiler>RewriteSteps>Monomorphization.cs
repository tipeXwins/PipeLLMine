--- qsharp-compiler/qsharp-compiler#809/after/src>QsCompiler>Compiler>RewriteSteps>Monomorphization.cs	2022-01-10 16:02:54.000000000 +0000
+++ qsharp-compiler/qsharp-compiler#809/before/src>QsCompiler>Compiler>RewriteSteps>Monomorphization.cs	2022-01-10 16:02:54.000000000 +0000
@@ -14,7 +14,6 @@
     /// </summary>
     internal class Monomorphization : IRewriteStep
     {
-        private readonly bool keepAllIntrinsics;
         public string Name => "Monomorphization";
 
         public int Priority => RewriteStepPriorities.TypeParameterElimination;
@@ -29,9 +28,8 @@
 
         public bool ImplementsPostconditionVerification => true;
 
-        public Monomorphization(bool keepAllIntrinsics = true)
+        public Monomorphization()
         {
-            this.keepAllIntrinsics = keepAllIntrinsics;
             this.AssemblyConstants = new Dictionary<string, string?>();
         }
 
@@ -39,7 +37,7 @@
 
         public bool Transformation(QsCompilation compilation, out QsCompilation transformed)
         {
-            transformed = Monomorphize.Apply(compilation, this.keepAllIntrinsics);
+            transformed = Monomorphize.Apply(compilation);
             return true;
         }
 
