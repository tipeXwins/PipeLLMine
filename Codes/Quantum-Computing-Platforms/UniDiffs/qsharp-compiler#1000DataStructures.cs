--- qsharp-compiler/qsharp-compiler#1000/after/DataStructures.cs	2022-01-10 16:02:54.000000000 +0000
+++ qsharp-compiler/qsharp-compiler#1000/before/DataStructures.cs	2022-01-10 16:02:54.000000000 +0000
@@ -51,8 +51,8 @@
 
             public bool IsCached =>
                 this.cache.Item2 != null &&
-                this.sharedState.IsOpenBranch(this.cache.Item1) &&
-                (this.store == null || !this.sharedState.IsWithinLoop || this.sharedState.IsWithinCurrentLoop(this.cache.Item1));
+                (this.store == null || !this.sharedState.IsWithinLoop || this.cache.Item1 == this.sharedState.CurrentBranch) &&
+                this.sharedState.IsOpenBranch(this.cache.Item1);
 
             /// <summary>
             /// Returns the cached value stored or loads it if necessary.
