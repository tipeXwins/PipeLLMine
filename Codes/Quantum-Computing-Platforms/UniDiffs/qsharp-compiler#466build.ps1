--- qsharp-compiler/qsharp-compiler#466/after/build.ps1	2022-01-10 16:02:54.000000000 +0000
+++ qsharp-compiler/qsharp-compiler#466/before/build.ps1	2022-01-10 16:02:54.000000000 +0000
@@ -17,15 +17,10 @@
     );
 
     Write-Host "##[info]Building $project ..."
-    if ("" -ne "$Env:ASSEMBLY_CONSTANTS") {
-        $args = @("/property:DefineConstants=$Env:ASSEMBLY_CONSTANTS");
-    }  else {
-        $args = @();
-    }
     dotnet build (Join-Path $PSScriptRoot $project) `
         -c $Env:BUILD_CONFIGURATION `
         -v $Env:BUILD_VERBOSITY `
-        @args `
+        /property:DefineConstants=$Env:ASSEMBLY_CONSTANTS `
         /property:Version=$Env:ASSEMBLY_VERSION
 
     if  ($LastExitCode -ne 0) {
@@ -75,14 +70,9 @@
             
             if (Get-Command msbuild -ErrorAction SilentlyContinue) {
                 Try {
-                    if ("" -ne "$Env:ASSEMBLY_CONSTANTS") {
-                        $args = @("/property:DefineConstants=$Env:ASSEMBLY_CONSTANTS");
-                    }  else {
-                        $args = @();
-                    }
                     msbuild VisualStudioExtension.sln `
                         /property:Configuration=$Env:BUILD_CONFIGURATION `
-                        @args `
+                        /property:DefineConstants=$Env:ASSEMBLY_CONSTANTS `
                         /property:AssemblyVersion=$Env:ASSEMBLY_VERSION
     
                     if ($LastExitCode -ne 0) {
