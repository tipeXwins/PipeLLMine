--- qsharp-compiler/qsharp-compiler#885/after/Diagnostics.cs	2022-01-10 16:02:54.000000000 +0000
+++ qsharp-compiler/qsharp-compiler#885/before/Diagnostics.cs	2022-01-10 16:02:54.000000000 +0000
@@ -121,7 +121,7 @@
                 Code = Code(code),
                 Source = source,
                 Message = DiagnosticItem.Message(code, args ?? Enumerable.Empty<string>()),
-                Range = new Lsp.Range { Start = new Lsp.Position(0, 0), End = new Lsp.Position(0, 0) }
+                Range = null
             };
 
         // warnings 20**
@@ -134,7 +134,7 @@
                 Code = WarningCode.ExcessSemicolon.Code(),
                 Source = filename,
                 Message = DiagnosticItem.Message(WarningCode.ExcessSemicolon, Enumerable.Empty<string>()),
-                Range = new Lsp.Range { Start = pos.ToLsp(), End = pos.ToLsp() }
+                Range = pos == null ? null : new Lsp.Range { Start = pos.ToLsp(), End = pos.ToLsp() }
             };
         }
     }
@@ -156,42 +156,32 @@
                 Code = Code(code),
                 Source = source,
                 Message = DiagnosticItem.Message(code, args ?? Enumerable.Empty<string>()),
-                Range = new Lsp.Range { Start = new Lsp.Position(0, 0), End = new Lsp.Position(0, 0) }
+                Range = null
             };
 
         // errors 20**
 
         internal static Diagnostic InvalidFragmentEnding(string filename, ErrorCode code, Position pos)
         {
-            if (pos == null)
-            {
-                throw new ArgumentNullException(nameof(pos));
-            }
-
             return new Diagnostic
             {
                 Severity = DiagnosticSeverity.Error,
                 Code = Code(code),
                 Source = filename,
                 Message = DiagnosticItem.Message(code, Enumerable.Empty<string>()),
-                Range = new Lsp.Range { Start = pos.ToLsp(), End = pos.ToLsp() }
+                Range = pos == null ? null : new Lsp.Range { Start = pos.ToLsp(), End = pos.ToLsp() }
             };
         }
 
         internal static Diagnostic MisplacedOpeningBracketError(string filename, Position pos)
         {
-            if (pos == null)
-            {
-                throw new ArgumentNullException(nameof(pos));
-            }
-
             return new Diagnostic
             {
                 Severity = DiagnosticSeverity.Error,
                 Code = ErrorCode.MisplacedOpeningBracket.Code(),
                 Source = filename,
                 Message = DiagnosticItem.Message(ErrorCode.MisplacedOpeningBracket, Enumerable.Empty<string>()),
-                Range = new Lsp.Range { Start = pos.ToLsp(), End = pos.ToLsp() }
+                Range = pos == null ? null : new Lsp.Range { Start = pos.ToLsp(), End = pos.ToLsp() }
             };
         }
 
@@ -199,69 +189,49 @@
 
         internal static Diagnostic ExcessBracketError(string filename, Position pos)
         {
-            if (pos == null)
-            {
-                throw new ArgumentNullException(nameof(pos));
-            }
-
             return new Diagnostic
             {
                 Severity = DiagnosticSeverity.Error,
                 Code = ErrorCode.ExcessBracketError.Code(),
                 Source = filename,
                 Message = DiagnosticItem.Message(ErrorCode.ExcessBracketError, Enumerable.Empty<string>()),
-                Range = new Lsp.Range { Start = pos.ToLsp(), End = pos.ToLsp() }
+                Range = pos == null ? null : new Lsp.Range { Start = pos.ToLsp(), End = pos.ToLsp() }
             };
         }
 
         internal static Diagnostic MissingClosingBracketError(string filename, Position pos)
         {
-            if (pos == null)
-            {
-                throw new ArgumentNullException(nameof(pos));
-            }
-
             return new Diagnostic
             {
                 Severity = DiagnosticSeverity.Error,
                 Code = ErrorCode.MissingBracketError.Code(),
                 Source = filename,
                 Message = DiagnosticItem.Message(ErrorCode.MissingBracketError, Enumerable.Empty<string>()),
-                Range = new Lsp.Range { Start = pos.ToLsp(), End = pos.ToLsp() }
+                Range = pos == null ? null : new Lsp.Range { Start = pos.ToLsp(), End = pos.ToLsp() }
             };
         }
 
         internal static Diagnostic MissingStringDelimiterError(string filename, Position pos)
         {
-            if (pos == null)
-            {
-                throw new ArgumentNullException(nameof(pos));
-            }
-
             return new Diagnostic
             {
                 Severity = DiagnosticSeverity.Error,
                 Code = ErrorCode.MissingStringDelimiterError.Code(),
                 Source = filename,
                 Message = DiagnosticItem.Message(ErrorCode.MissingStringDelimiterError, Enumerable.Empty<string>()),
-                Range = new Lsp.Range { Start = pos.ToLsp(), End = pos.ToLsp() }
+                Range = pos == null ? null : new Lsp.Range { Start = pos.ToLsp(), End = pos.ToLsp() }
             };
         }
 
         internal static Diagnostic InvalidCharacterInInterpolatedArgument(string filename, Position pos, char invalidCharacter)
         {
-            if (pos == null)
-            {
-                throw new ArgumentNullException(nameof(pos));
-            }
-
             return new Diagnostic
             {
                 Severity = DiagnosticSeverity.Error,
                 Code = ErrorCode.InvalidCharacterInInterpolatedArgument.Code(),
                 Source = filename,
                 Message = DiagnosticItem.Message(ErrorCode.InvalidCharacterInInterpolatedArgument, new[] { invalidCharacter.ToString() }),
-                Range = new Lsp.Range { Start = pos.ToLsp(), End = pos.ToLsp() }
+                Range = pos == null ? null : new Lsp.Range { Start = pos.ToLsp(), End = pos.ToLsp() }
             };
         }
     }
