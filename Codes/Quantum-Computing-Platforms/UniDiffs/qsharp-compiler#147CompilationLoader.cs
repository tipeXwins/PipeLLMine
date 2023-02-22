--- qsharp-compiler/qsharp-compiler#147/after/CompilationLoader.cs	2022-01-10 16:02:54.000000000 +0000
+++ qsharp-compiler/qsharp-compiler#147/before/CompilationLoader.cs	2022-01-10 16:02:54.000000000 +0000
@@ -218,6 +218,12 @@
 
             // executing the specified rewrite steps 
 
+            if (this.Config.GenerateFunctorSupport)
+            {
+                this.CompilationStatus.FunctorSupport = 0;
+                var functorSpecGenerated = this.GeneratedSyntaxTree != null && FunctorGeneration.GenerateFunctorSpecializations(this.GeneratedSyntaxTree, out this.GeneratedSyntaxTree);
+                if (!functorSpecGenerated) this.LogAndUpdate(ref this.CompilationStatus.FunctorSupport, ErrorCode.FunctorGenerationFailed, Enumerable.Empty<string>());
+            }
             if (!this.Config.SkipSyntaxTreeTrimming)
             {
                 this.CompilationStatus.TreeTrimming = 0;
@@ -225,12 +231,6 @@
                 this.GeneratedSyntaxTree = this.GeneratedSyntaxTree?.Select(ns => rewrite.Transform(ns))?.ToImmutableArray();
                 if (this.GeneratedSyntaxTree == null || !rewrite.Success) this.LogAndUpdate(ref this.CompilationStatus.TreeTrimming, ErrorCode.TreeTrimmingFailed, Enumerable.Empty<string>());
             }
-            if (this.Config.GenerateFunctorSupport)
-            {
-                this.CompilationStatus.FunctorSupport = 0;
-                var functorSpecGenerated = this.GeneratedSyntaxTree != null && FunctorGeneration.GenerateFunctorSpecializations(this.GeneratedSyntaxTree, out this.GeneratedSyntaxTree);
-                if (!functorSpecGenerated) this.LogAndUpdate(ref this.CompilationStatus.FunctorSupport, ErrorCode.FunctorGenerationFailed, Enumerable.Empty<string>());
-            }
 
             // generating the compiled binary
 
