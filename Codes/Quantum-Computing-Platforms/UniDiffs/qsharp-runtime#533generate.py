--- qsharp-runtime/qsharp-runtime#533/after/generate.py	2022-01-10 16:02:54.000000000 +0000
+++ qsharp-runtime/qsharp-runtime#533/before/generate.py	2022-01-10 16:02:54.000000000 +0000
@@ -35,10 +35,7 @@
 
   # Compile as a lib so all functions are retained and don't have to workaround the current limitations of
   # @EntryPoint attribute.
-  command = (qsc + " build --qir qir --input " + files_to_process + " --proj " + output_file)
+  command = (qsc + " build --qir s --input " + files_to_process + " --proj " + output_file)
   log("Executing: " + command)
   subprocess.run(command, shell = True)
-  generated_file = os.path.join(root_dir, "qir", output_file) + ".ll"
-  build_input_file = os.path.join(root_dir, output_file) + ".ll"
-  shutil.copyfile(generated_file, build_input_file)
 
