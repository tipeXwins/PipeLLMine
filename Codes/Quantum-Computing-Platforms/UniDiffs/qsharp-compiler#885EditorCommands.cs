--- qsharp-compiler/qsharp-compiler#885/after/EditorCommands.cs	2022-01-10 16:02:54.000000000 +0000
+++ qsharp-compiler/qsharp-compiler#885/before/EditorCommands.cs	2022-01-10 16:02:54.000000000 +0000
@@ -203,7 +203,7 @@
             Hover? GetHover(string? info) => info == null ? null : new Hover
             {
                 Contents = new MarkupContent { Kind = format, Value = info },
-                Range = new Lsp.Range { Start = position.ToLsp(), End = position.ToLsp() }
+                Range = new Lsp.Range { Start = position?.ToLsp(), End = position?.ToLsp() }
             };
 
             var markdown = format == MarkupKind.Markdown;
@@ -393,7 +393,7 @@
             MarkupContent AsMarkupContent(string str) => new MarkupContent { Kind = format, Value = str };
             ParameterInformation AsParameterInfo(string? paramName) => new ParameterInformation
             {
-                Label = paramName ?? "<unknown parameter>",
+                Label = paramName,
                 Documentation = AsMarkupContent(documentation.ParameterDescription(paramName))
             };
 
