--- qsharp-compiler/qsharp-compiler#885/after/Communication.cs	2022-01-10 16:02:54.000000000 +0000
+++ qsharp-compiler/qsharp-compiler#885/before/Communication.cs	2022-01-10 16:02:54.000000000 +0000
@@ -64,21 +64,13 @@
             [DataMember(Name = "context")]
             public CodeActionContext? Context { get; set; }
 
-            public VisualStudio.LanguageServer.Protocol.CodeActionParams? ToCodeActionParams() =>
-                this.TextDocument == null
-                ? null
-                : new VisualStudio.LanguageServer.Protocol.CodeActionParams
-                  {
-                      TextDocument = this.TextDocument,
-                      Range = this.Range ?? new Range(),
-                      Context = this.Context?.ToCodeActionContext() ??
-                          // Make a blank context if we're missing a code action
-                          // context.
-                          new VisualStudio.LanguageServer.Protocol.CodeActionContext
-                          {
-                              Diagnostics = new Diagnostic[] { }
-                          }
-                  };
+            public VisualStudio.LanguageServer.Protocol.CodeActionParams ToCodeActionParams() =>
+                new VisualStudio.LanguageServer.Protocol.CodeActionParams
+                {
+                    TextDocument = this.TextDocument,
+                    Range = this.Range,
+                    Context = this.Context?.ToCodeActionContext()
+                };
         }
 
         /// <summary>
@@ -95,7 +87,7 @@
             public VisualStudio.LanguageServer.Protocol.CodeActionContext ToCodeActionContext() =>
                 new VisualStudio.LanguageServer.Protocol.CodeActionContext
                 {
-                    Diagnostics = this.Diagnostics ?? new Diagnostic[] { },
+                    Diagnostics = this.Diagnostics,
                     Only = null
                 };
         }
