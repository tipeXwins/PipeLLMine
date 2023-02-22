--- qsharp-compiler/qsharp-compiler#712/after/pack.ps1	2022-01-10 16:02:54.000000000 +0000
+++ qsharp-compiler/qsharp-compiler#712/before/pack.ps1	2022-01-10 16:02:54.000000000 +0000
@@ -25,7 +25,6 @@
     dotnet publish (Join-Path $PSScriptRoot $project) `
         -c $Env:BUILD_CONFIGURATION `
         -v $Env:BUILD_VERBOSITY `
-        --no-build `
         @args `
         /property:Version=$Env:ASSEMBLY_VERSION
 
@@ -66,7 +65,6 @@
         -o $Env:NUGET_OUTDIR `
         -c $Env:BUILD_CONFIGURATION `
         -v detailed `
-        --no-build `
         @args `
         /property:Version=$Env:ASSEMBLY_VERSION `
         /property:PackageVersion=$Env:NUGET_VERSION `
