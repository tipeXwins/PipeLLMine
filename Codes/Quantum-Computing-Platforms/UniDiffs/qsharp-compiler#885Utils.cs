--- qsharp-compiler/qsharp-compiler#885/after/Utils.cs	2022-01-10 16:02:54.000000000 +0000
+++ qsharp-compiler/qsharp-compiler#885/before/Utils.cs	2022-01-10 16:02:54.000000000 +0000
@@ -168,10 +168,8 @@
         /// <summary>
         /// Converts the Q# compiler position into a language server protocol position.
         /// </summary>
-        public static Lsp.Position ToLsp(this Position? position) =>
-            position == null
-            ? new Lsp.Position()
-            : new Lsp.Position(position.Line, position.Column);
+        public static Lsp.Position ToLsp(this Position position) =>
+            new Lsp.Position(position.Line, position.Column);
 
         /// <summary>
         /// Converts the language server protocol range into a Q# compiler range.
