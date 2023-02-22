--- qsharp-compiler/qsharp-compiler#1000/after/ExpressionKindTransformation.cs	2022-01-10 16:02:54.000000000 +0000
+++ qsharp-compiler/qsharp-compiler#1000/before/ExpressionKindTransformation.cs	2022-01-10 16:02:54.000000000 +0000
@@ -273,14 +273,12 @@
                     var falseBlock = sharedState.AddBlockAfterCurrent("condFalse");
 
                     sharedState.CurrentBuilder.Branch(wasCopied, contBlock, falseBlock);
+                    sharedState.ScopeMgr.OpenScope();
                     sharedState.SetCurrentBlock(falseBlock);
 
-                    sharedState.StartBranch(); // needed for the caching of length to work properly
-                    sharedState.ScopeMgr.OpenScope();
                     sharedState.ScopeMgr.IncreaseReferenceCount(value, shallow);
                     sharedState.ScopeMgr.DecreaseReferenceCount(pointer, shallow);
                     sharedState.ScopeMgr.CloseScope(false);
-                    sharedState.EndBranch();
                     sharedState.CurrentBuilder.Branch(contBlock);
                     sharedState.SetCurrentBlock(contBlock);
                 }
