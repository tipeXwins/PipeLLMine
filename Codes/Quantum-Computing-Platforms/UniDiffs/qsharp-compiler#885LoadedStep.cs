--- qsharp-compiler/qsharp-compiler#885/after/LoadedStep.cs	2022-01-10 16:02:54.000000000 +0000
+++ qsharp-compiler/qsharp-compiler#885/before/LoadedStep.cs	2022-01-10 16:02:54.000000000 +0000
@@ -123,9 +123,7 @@
                 Severity = severity,
                 Message = $"{stageAnnotation}{diagnostic.Message}",
                 Source = diagnostic.Source,
-                Range = diagnostic.Source is null || diagnostic.Range is null
-                        ? new VisualStudio.LanguageServer.Protocol.Range()
-                        : diagnostic.Range.ToLsp()
+                Range = diagnostic.Source is null ? null : diagnostic.Range?.ToLsp()
             };
         }
 
