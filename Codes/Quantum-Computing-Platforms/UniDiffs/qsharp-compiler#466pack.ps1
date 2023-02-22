--- qsharp-compiler/qsharp-compiler#466/after/pack.ps1	2022-01-10 16:02:54.000000000 +0000
+++ qsharp-compiler/qsharp-compiler#466/before/pack.ps1	2022-01-10 16:02:54.000000000 +0000
@@ -17,15 +17,10 @@
     );
 
     Write-Host "##[info]Publishing $project ..."
-    if ("" -ne "$Env:ASSEMBLY_CONSTANTS") {
-        $args = @("/property:DefineConstants=$Env:ASSEMBLY_CONSTANTS");
-    }  else {
-        $args = @();
-    }
     dotnet publish (Join-Path $PSScriptRoot $project) `
         -c $Env:BUILD_CONFIGURATION `
         -v $Env:BUILD_VERBOSITY `
-        @args `
+        /property:DefineConstants=$Env:ASSEMBLY_CONSTANTS `
         /property:Version=$Env:ASSEMBLY_VERSION
 
     if  ($LastExitCode -ne 0) {
@@ -117,11 +112,6 @@
         New-Item -ItemType Directory -Path $ArchiveDir -Force -ErrorAction SilentlyContinue;
 
         try {
-            if ("" -ne "$Env:ASSEMBLY_CONSTANTS") {
-                $args = @("/property:DefineConstants=$Env:ASSEMBLY_CONSTANTS");
-            }  else {
-                $args = @();
-            }
             $ArchivePath = Join-Path $ArchiveDir "$BaseName-$DotNetRuntimeID-$Env:ASSEMBLY_VERSION.zip";
             dotnet publish (Join-Path $PSScriptRoot $Project) `
                 -c $Env:BUILD_CONFIGURATION `
@@ -129,7 +119,7 @@
                 --self-contained `
                 --runtime $DotNetRuntimeID `
                 --output $TargetDir `
-                @args `
+                /property:DefineConstants=$Env:ASSEMBLY_CONSTANTS `
                 /property:Version=$Env:ASSEMBLY_VERSION
             Write-Host "##[info]Writing self-contained deployment to $ArchivePath..."
             Compress-Archive `
