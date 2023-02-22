--- qsharp-compiler/qsharp-compiler#987/after/Context.cs	2022-01-10 16:02:54.000000000 +0000
+++ qsharp-compiler/qsharp-compiler#987/before/Context.cs	2022-01-10 16:02:54.000000000 +0000
@@ -1099,7 +1099,7 @@
                 throw new InvalidOperationException("a default value is required if either onCondTrue or onCondFalse is null");
             }
 
-            var defaultRequiresRefCount = increaseReferenceCount && defaultValue != null && ScopeManager.RequiresReferenceCount(defaultValue.LlvmType);
+            var defaultRequiresRefCount = increaseReferenceCount && defaultValue != null && this.ScopeMgr.RequiresReferenceCount(defaultValue.LlvmType);
             var requiresTrueBlock = onCondTrue != null || defaultRequiresRefCount;
             var requiresFalseBlock = onCondFalse != null || defaultRequiresRefCount;
 
@@ -1126,7 +1126,7 @@
                 {
                     this.ScopeMgr.OpenScope();
                     var evaluated = evaluate?.Invoke() ?? defaultValue!;
-                    this.ScopeMgr.CloseScope(evaluated); // forces that the ref count is increased within the branch
+                    this.ScopeMgr.CloseScope(evaluated, false); // force that the ref count is increased within the branch
                     return evaluated;
                 }
                 else
