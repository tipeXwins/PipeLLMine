--- qsharp-compiler/qsharp-compiler#885/after/DiagnosticTools.cs	2022-01-10 16:02:54.000000000 +0000
+++ qsharp-compiler/qsharp-compiler#885/before/DiagnosticTools.cs	2022-01-10 16:02:54.000000000 +0000
@@ -37,35 +37,28 @@
         [return: NotNullIfNotNull("message")]
         public static Diagnostic? Copy(this Diagnostic message)
         {
-            Lsp.Position CopyPosition(Lsp.Position position) =>
-                new Lsp.Position(position.Line, position.Character);
+            Lsp.Position? CopyPosition(Lsp.Position? position) =>
+                position is null ? null : new Lsp.Position(position.Line, position.Character);
 
-            Lsp.Range CopyRange(Lsp.Range range) =>
-                new Lsp.Range
-                {
-                    Start = CopyPosition(range.Start),
-                    End = CopyPosition(range.End)
-                };
+            Lsp.Range? CopyRange(Lsp.Range? range) =>
+                range is null
+                    ? null
+                    : new Lsp.Range
+                    {
+                        Start = CopyPosition(range.Start),
+                        End = CopyPosition(range.End)
+                    };
 
-            // NB: The nullability metadata on Diagnostic.Range is incorrect,
-            //     such that some Diagnostic values may have nullable ranges.
-            //     We cannot assign that to a new Diagnostic without
-            //     contradicting nullability metadata, however, so we need to
-            //     explicitly disable nullable references for the following
-            //     statement. Once the upstream bug in the LSP client package
-            //     is fixed, we can remove the nullable disable here.
-            #nullable disable
             return message is null
                 ? null
                 : new Diagnostic
                 {
-                    Range = message.Range == null ? null : CopyRange(message.Range),
+                    Range = CopyRange(message.Range),
                     Severity = message.Severity,
                     Code = message.Code,
                     Source = message.Source,
                     Message = message.Message
                 };
-            #nullable restore
         }
 
         /// <summary>
@@ -77,17 +70,12 @@
         public static Diagnostic WithLineNumOffset(this Diagnostic diagnostic, int offset)
         {
             var copy = diagnostic.Copy();
-            // NB: Despite the nullability metadata, Range may be null here.
-            //     We thus need to guard accordingly.
-            if (copy.Range != null)
+            copy.Range.Start.Line += offset;
+            copy.Range.End.Line += offset;
+            if (copy.Range.Start.Line < 0 || copy.Range.End.Line < 0)
             {
-                copy.Range.Start.Line += offset;
-                copy.Range.End.Line += offset;
-                if (copy.Range.Start.Line < 0 || copy.Range.End.Line < 0)
-                {
-                    throw new ArgumentOutOfRangeException(
-                        nameof(offset), "Translated diagnostic has negative line numbers.");
-                }
+                throw new ArgumentOutOfRangeException(
+                    nameof(offset), "Translated diagnostic has negative line numbers.");
             }
             return copy;
         }
