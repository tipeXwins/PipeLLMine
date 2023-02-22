--- qsharp-compiler/qsharp-compiler#885/after/CodeCompletion.cs	2022-01-10 16:02:54.000000000 +0000
+++ qsharp-compiler/qsharp-compiler#885/before/CodeCompletion.cs	2022-01-10 16:02:54.000000000 +0000
@@ -430,7 +430,7 @@
         /// completion item data is missing properties.
         /// </summary>
         private static string? TryGetDocumentation(
-            CompilationUnit compilation, CompletionItemData data, CompletionItemKind? kind, bool useMarkdown)
+            CompilationUnit compilation, CompletionItemData data, CompletionItemKind kind, bool useMarkdown)
         {
             if (data.QualifiedName == null
                 || data.SourceFile == null
@@ -619,7 +619,7 @@
             new CompletionList
             {
                 IsIncomplete = isIncomplete,
-                Items = items?.ToArray() ?? new CompletionItem[] { }
+                Items = items?.ToArray()
             };
 
         /// <summary>
