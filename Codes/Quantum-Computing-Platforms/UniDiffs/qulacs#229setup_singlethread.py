--- qulacs/qulacs#229/after/setup_singlethread.py	2022-01-10 16:02:54.000000000 +0000
+++ qulacs/qulacs#229/before/setup_singlethread.py	2022-01-10 16:02:54.000000000 +0000
@@ -12,13 +12,6 @@
 
 project_name = 'Qulacs'
 
-def _is_valid_compiler(cmd):
-    try:
-        out = subprocess.check_output([cmd, '-dumpfullversion', '-dumpversion']).decode()
-        version = LooseVersion(out)
-        return version >= LooseVersion('7.0.0')
-    except:
-        return False
 class CMakeExtension(Extension):
     def __init__(self, name, sourcedir=''):
         Extension.__init__(self, name, sources=[])
@@ -65,25 +58,22 @@
                 cmake_args += ['-A', 'x64']
             build_args += ['--', '/m']
         else:
-            env_gcc = os.getenv('C_COMPILER')
-            if env_gcc:
-                gcc_candidates = [env_gcc]
+            try:
+                gcc_out = subprocess.check_output(['gcc', '-dumpfullversion', '-dumpversion']).decode()
+                gcc_version = LooseVersion(gcc_out)
+                gxx_out = subprocess.check_output(['g++', '-dumpfullversion', '-dumpversion']).decode()
+                gxx_version = LooseVersion(gxx_out)
+            except OSError:
+                raise RuntimeError("gcc/g++ must be installed to build the following extensions: " +
+                               ", ".join(e.name for e in self.extensions))
+            if(gcc_version >= LooseVersion('7.0.0')):
+                cmake_args += ['-DCMAKE_C_COMPILER=gcc']
             else:
-                gcc_candidates = ['gcc', 'gcc-9', 'gcc-8', 'gcc-7']
-            gcc = next(iter(filter(_is_valid_compiler, gcc_candidates)), None)
-
-            env_gxx = os.getenv('CXX_COMPILER')
-            if env_gxx:
-                gxx_candidates = [env_gxx]
+                cmake_args += ['-DCMAKE_C_COMPILER=gcc-7']
+            if(gxx_version >= LooseVersion('7.0.0')):
+                cmake_args += ['-DCMAKE_CXX_COMPILER=g++']
             else:
-                gxx_candidates = ['g++', 'g++-9', 'g++-8', 'g++-7']
-            gxx = next(iter(filter(_is_valid_compiler, gxx_candidates)), None)
-            if gcc is None or gxx is None:
-                raise RuntimeError("gcc/g++ >= 7.0.0 must be installed to build the following extensions: " +
-                               ", ".join(e.name for e in self.extensions))
-            cmake_args += ['-DCMAKE_C_COMPILER=' + gcc]
-            cmake_args += ['-DCMAKE_CXX_COMPILER=' + gxx]
-
+                cmake_args += ['-DCMAKE_CXX_COMPILER=g++-7']
             cmake_args += ['-DCMAKE_BUILD_TYPE=' + cfg]
             build_args += ['--', '-j2']
 
