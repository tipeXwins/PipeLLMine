--- qsharp-compiler/qsharp-compiler#885/after/ProjectManager.cs	2022-01-10 16:02:54.000000000 +0000
+++ qsharp-compiler/qsharp-compiler#885/before/ProjectManager.cs	2022-01-10 16:02:54.000000000 +0000
@@ -929,30 +929,10 @@
 
             try
             {
-                // NB: As of version 16.9.1180 of the LSP client, document
-                //     changes are presented as the sum type
-                //     TextDocumentEdit[] | (TextDocumentEdit | CreateFile | RenameFile | DeleteFile)[].
-                //     Thus, to collect them with a SelectMany call, we need
-                //     to ensure that the first case (TextDocumentEdit[]) is
-                //     first wrapped in a cast to the sum type
-                //     TextDocumentEdit | CreateFile | RenameFile | DeleteFile.
-                //     Note that the SumType struct is defined in the LSP client,
-                //     and works by defining explicit cast operators for each case.
-                IEnumerable<SumType<TextDocumentEdit, CreateFile, RenameFile, DeleteFile>> CastToSumType(SumType<TextDocumentEdit[], SumType<TextDocumentEdit, CreateFile, RenameFile, DeleteFile>[]>? editCollection) =>
-                    editCollection switch
-                    {
-                        { } edits => edits.Match(
-                            simpleEdits => simpleEdits.Cast<SumType<TextDocumentEdit, CreateFile, RenameFile, DeleteFile>>(),
-                            complexEdits => complexEdits),
-                        null => ImmutableList<SumType<TextDocumentEdit, CreateFile, RenameFile, DeleteFile>>.Empty
-                    };
-
                 // if a file belongs to several compilation units, then this will fail
                 var changes = edits.SelectMany(edit => edit.Changes)
                     .ToDictionary(pair => pair.Key, pair => pair.Value);
-                var documentChanges = edits
-                    .SelectMany(edits => CastToSumType(edits.DocumentChanges).ToArray())
-                    .ToArray();
+                var documentChanges = edits.SelectMany(edit => edit.DocumentChanges).ToArray();
                 return new WorkspaceEdit { Changes = changes, DocumentChanges = documentChanges };
             }
             catch
