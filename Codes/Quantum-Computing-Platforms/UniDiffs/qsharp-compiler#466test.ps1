--- qsharp-compiler/qsharp-compiler#466/after/test.ps1	2022-01-10 16:02:54.000000000 +0000
+++ qsharp-compiler/qsharp-compiler#466/before/test.ps1	2022-01-10 16:02:54.000000000 +0000
@@ -19,16 +19,11 @@
 
     Write-Host "##[info]Testing $project..."
 
-    if ("" -ne "$Env:ASSEMBLY_CONSTANTS") {
-        $args = @("/property:DefineConstants=$Env:ASSEMBLY_CONSTANTS");
-    }  else {
-        $args = @();
-    }
     dotnet test (Join-Path $PSScriptRoot $project) `
         -c $Env:BUILD_CONFIGURATION `
         -v $Env:BUILD_VERBOSITY `
         --logger trx `
-        @args `
+        /property:DefineConstants=$Env:ASSEMBLY_CONSTANTS `
         /property:Version=$Env:ASSEMBLY_VERSION
 
     if  ($LastExitCode -ne 0) {
