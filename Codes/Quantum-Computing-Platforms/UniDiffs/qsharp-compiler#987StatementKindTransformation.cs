--- qsharp-compiler/qsharp-compiler#987/after/StatementKindTransformation.cs	2022-01-10 16:02:54.000000000 +0000
+++ qsharp-compiler/qsharp-compiler#987/before/StatementKindTransformation.cs	2022-01-10 16:02:54.000000000 +0000
@@ -289,10 +289,13 @@
                 this.SharedState.EndBranch();
             }
 
-            this.SharedState.SetCurrentBlock(contBlock);
-            if (!contBlockUsed)
+            if (contBlockUsed)
             {
-                this.OnFailStatement(SyntaxGenerator.StringLiteral("reached unreachable code...", ImmutableArray<TypedExpression>.Empty));
+                this.SharedState.SetCurrentBlock(contBlock);
+            }
+            else
+            {
+                this.SharedState.CurrentFunction.BasicBlocks.Remove(contBlock);
             }
             return QsStatementKind.EmptyStatement;
         }
@@ -413,7 +416,7 @@
                 // We need to make sure to properly invoke all calls to unreference, release, and remove alias counts
                 // for variables and values in the repeat-block after the statement ends.
                 this.SharedState.SetCurrentBlock(contBlock);
-                this.SharedState.ScopeMgr.ExitScope();
+                this.SharedState.ScopeMgr.ExitScope(false);
 
                 this.SharedState.SetCurrentBlock(fixupBlock);
                 this.Transformation.Statements.OnScope(stm.FixupBlock.Body);
