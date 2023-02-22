--- qsharp-compiler/qsharp-compiler#885/after/src>QsCompiler>CommandLineTool>Logging.cs	2022-01-10 16:02:54.000000000 +0000
+++ qsharp-compiler/qsharp-compiler#885/before/src>QsCompiler>CommandLineTool>Logging.cs	2022-01-10 16:02:54.000000000 +0000
@@ -41,14 +41,12 @@
         /// Prints the given message to the Console.
         /// Errors and Warnings are printed to the error stream.
         /// </summary>
-        private static void PrintToConsole(DiagnosticSeverity? severity, string message)
+        private static void PrintToConsole(DiagnosticSeverity severity, string message)
         {
-            var (stream, color) = severity switch
-            {
-                DiagnosticSeverity.Error => (Console.Error, ConsoleColor.Red),
-                DiagnosticSeverity.Warning => (Console.Error, ConsoleColor.Yellow),
-                _ => (Console.Out, Console.ForegroundColor)
-            };
+            var (stream, color) =
+                severity == DiagnosticSeverity.Error ? (Console.Error, ConsoleColor.Red) :
+                severity == DiagnosticSeverity.Warning ? (Console.Error, ConsoleColor.Yellow) :
+                (Console.Out, Console.ForegroundColor);
 
             var consoleColor = Console.ForegroundColor;
             Console.ForegroundColor = color;
