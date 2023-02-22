--- qsharp-compiler/qsharp-compiler#885/after/LanguageServer.cs	2022-01-10 16:02:54.000000000 +0000
+++ qsharp-compiler/qsharp-compiler#885/before/LanguageServer.cs	2022-01-10 16:02:54.000000000 +0000
@@ -273,7 +273,6 @@
                 CompletionProvider = supportsCompletion ? new CompletionOptions() : null,
                 SignatureHelpProvider = new SignatureHelpOptions(),
                 ExecuteCommandProvider = new ExecuteCommandOptions(),
-                DocumentRangeFormattingProvider = false
             };
             capabilities.TextDocumentSync.Change = TextDocumentSyncKind.Incremental;
             capabilities.TextDocumentSync.OpenClose = true;
@@ -354,11 +353,7 @@
                 return Task.CompletedTask;
             }
             var param = Utils.TryJTokenAs<DidSaveTextDocumentParams>(arg);
-            // NB: if param.Text is null, then there's nothing to actually
-            //     do here.
-            return param.Text == null
-                   ? Task.CompletedTask
-                   : this.editorState.SaveFileAsync(param.TextDocument, param.Text);
+            return this.editorState.SaveFileAsync(param.TextDocument, param.Text);
         }
 
         [JsonRpcMethod(Methods.TextDocumentDidChangeName)]
@@ -403,8 +398,10 @@
             var param = Utils.TryJTokenAs<TextDocumentPositionParams>(arg);
             var defaultLocation = new Location
             {
-                Uri = param.TextDocument.Uri,
-                Range = new VisualStudio.LanguageServer.Protocol.Range { Start = param.Position, End = param.Position }
+                Uri = param?.TextDocument?.Uri,
+                Range = param?.Position != null
+                    ? new VisualStudio.LanguageServer.Protocol.Range { Start = param.Position, End = param.Position }
+                    : null
             };
             try
             {
@@ -598,12 +595,6 @@
                 return ProtocolError.AwaitingInitialization;
             }
             var param = Utils.TryJTokenAs<Workarounds.CodeActionParams>(arg).ToCodeActionParams();
-            if (param == null)
-            {
-                this.LogToWindow("No code action parameters found; skipping code actions.", MessageType.Warning);
-                return Array.Empty<CodeAction>();
-            }
-
             try
             {
                 return
