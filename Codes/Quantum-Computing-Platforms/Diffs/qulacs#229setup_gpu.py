15,21d14
< def _is_valid_compiler(cmd):
<     try:
<         out = subprocess.check_output([cmd, '-dumpfullversion', '-dumpversion']).decode()
<         version = LooseVersion(out)
<         return version >= LooseVersion('7.0.0')
<     except:
<         return False
68,70c61,70
<             env_gcc = os.getenv('C_COMPILER')
<             if env_gcc:
<                 gcc_candidates = [env_gcc]
---
>             try:
>                 gcc_out = subprocess.check_output(['gcc', '-dumpfullversion', '-dumpversion']).decode()
>                 gcc_version = LooseVersion(gcc_out)
>                 gxx_out = subprocess.check_output(['g++', '-dumpfullversion', '-dumpversion']).decode()
>                 gxx_version = LooseVersion(gxx_out)
>             except OSError:
>                 raise RuntimeError("gcc/g++ must be installed to build the following extensions: " +
>                                ", ".join(e.name for e in self.extensions))
>             if(gcc_version >= LooseVersion('7.0.0')):
>                 cmake_args += ['-DCMAKE_C_COMPILER=gcc']
72,76c72,74
<                 gcc_candidates = ['gcc', 'gcc-9', 'gcc-8', 'gcc-7']
<             gcc = next(iter(filter(_is_valid_compiler, gcc_candidates)), None)
<             env_gxx = os.getenv('CXX_COMPILER')
<             if env_gxx:
<                 gxx_candidates = [env_gxx]
---
>                 cmake_args += ['-DCMAKE_C_COMPILER=gcc-7']
>             if(gxx_version >= LooseVersion('7.0.0')):
>                 cmake_args += ['-DCMAKE_CXX_COMPILER=g++']
78,84c76
<                 gxx_candidates = ['g++', 'g++-9', 'g++-8', 'g++-7']
<             gxx = next(iter(filter(_is_valid_compiler, gxx_candidates)), None)
<             if gcc is None or gxx is None:
<                 raise RuntimeError("gcc/g++ >= 7.0.0 must be installed to build the following extensions: " +
<                                ", ".join(e.name for e in self.extensions))
<             cmake_args += ['-DCMAKE_C_COMPILER=' + gcc]
<             cmake_args += ['-DCMAKE_CXX_COMPILER=' + gxx]
---
>                 cmake_args += ['-DCMAKE_CXX_COMPILER=g++-7']
