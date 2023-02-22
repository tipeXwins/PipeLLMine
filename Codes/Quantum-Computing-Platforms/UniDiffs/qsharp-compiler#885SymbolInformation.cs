--- qsharp-compiler/qsharp-compiler#885/after/SymbolInformation.cs	2022-01-10 16:02:54.000000000 +0000
+++ qsharp-compiler/qsharp-compiler#885/before/SymbolInformation.cs	2022-01-10 16:02:54.000000000 +0000
@@ -28,7 +28,7 @@
         internal static Location AsLocation(string source, Position offset, Range relRange) =>
             new Location
             {
-                Uri = CompilationUnitManager.TryGetUri(source, out var uri) ? uri : throw new Exception($"Source location {source} could not be converted to a valid URI."),
+                Uri = CompilationUnitManager.TryGetUri(source, out var uri) ? uri : null,
                 Range = (offset + relRange).ToLsp()
             };
 
