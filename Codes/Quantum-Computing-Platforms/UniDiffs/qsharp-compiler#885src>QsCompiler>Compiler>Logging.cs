--- qsharp-compiler/qsharp-compiler#885/after/src>QsCompiler>Compiler>Logging.cs	2022-01-10 16:02:54.000000000 +0000
+++ qsharp-compiler/qsharp-compiler#885/before/src>QsCompiler>Compiler>Logging.cs	2022-01-10 16:02:54.000000000 +0000
@@ -69,13 +69,6 @@
                 Message = $"{Environment.NewLine}{ex}{Environment.NewLine}"
             });
 
-        // NB: Calling the LSP.Range constructor results in an object with
-        //     non-nullable fields set to null values, confusing other places
-        //     where we use nullable reference type metadata. To address this,
-        //     we explicitly construct an empty range that runs from 0:0 to 0:0
-        //     that we can use when there is no reasonable range to provide.
-        private static readonly LSP.Range EmptyRange = new LSP.Range { Start = new Position(0, 0), End = new Position(0, 0) };
-
         // routines for convenience
 
         /// <summary>
@@ -89,7 +82,7 @@
                 Code = Errors.Code(code),
                 Source = source,
                 Message = DiagnosticItem.Message(code, args ?? Enumerable.Empty<string>()),
-                Range = range ?? EmptyRange
+                Range = range
             });
 
         /// <summary>
@@ -103,7 +96,7 @@
                 Code = Warnings.Code(code),
                 Source = source,
                 Message = DiagnosticItem.Message(code, args ?? Enumerable.Empty<string>()),
-                Range = range ?? EmptyRange
+                Range = range
             });
 
         /// <summary>
@@ -118,7 +111,7 @@
                 Code = null, // do not show a code for infos
                 Source = source,
                 Message = $"{DiagnosticItem.Message(code, args ?? Enumerable.Empty<string>())}{Environment.NewLine}{string.Join(Environment.NewLine, messageParam)}",
-                Range = range ?? EmptyRange
+                Range = range
             });
 
         /// <summary>
@@ -164,7 +157,6 @@
         public void Log(Diagnostic m)
         {
             if (m.Severity == DiagnosticSeverity.Warning &&
-                m.Code != null &&
                 CompilationBuilder.Diagnostics.TryGetCode(m.Code, out int code)
                 && this.noWarn.Contains(code))
             {
@@ -180,9 +172,7 @@
                 ++this.NrWarningsLogged;
             }
 
-            // We only want to print line number offsets if at least one of the
-            // start and end ranges are not both empty.
-            var msg = m.Range == EmptyRange ? m : m.WithLineNumOffset(this.lineNrOffset);
+            var msg = m.Range == null ? m : m.WithLineNumOffset(this.lineNrOffset);
             this.Output(msg);
         }
 
