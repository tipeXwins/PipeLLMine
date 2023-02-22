--- qsharp-runtime/qsharp-runtime#744/after/build.rs	2022-01-10 16:02:54.000000000 +0000
+++ qsharp-runtime/qsharp-runtime#744/before/build.rs	2022-01-10 16:02:54.000000000 +0000
@@ -1,6 +1,8 @@
 // Copyright (c) Microsoft Corporation.
 // Licensed under the MIT License.
 
+use std::env;
+use std::path::Path;
 fn main() -> Result<(), String> {
     built::write_built_file().expect("Failed to acquire build-time information");
 
