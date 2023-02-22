--- ProjectQ/ProjectQ#121/after/tutorials.rst	2022-01-10 16:02:54.000000000 +0000
+++ ProjectQ/ProjectQ#121/before/tutorials.rst	2022-01-10 16:02:54.000000000 +0000
@@ -22,8 +22,6 @@
 	cd /home/projectq
 	python -m pip install --user .
 
-ProjectQ comes with a high-performance quantum simulator written in C++. Please see the detailed OS specific installation instructions below to make sure that you are installing the fastest version.
-
 .. note::
 	The setup will try to build a C++-Simulator, which is much faster than the Python implementation. If it fails, you may use the `--without-cppsimulator` parameter, i.e., 
 	
@@ -50,7 +48,6 @@
 -------------------------------------------
 
 **Ubuntu**:
-
 	After having installed the build tools (for g++):
 
 	.. code-block:: bash
@@ -73,47 +70,21 @@
 
 
 **Windows**:
-
 	It is easiest to install a pre-compiled version of Python, including numpy and many more useful packages. One way to do so is using, e.g., the Python3.5 installers from `python.org <https://www.python.org/downloads>`_ or `ANACONDA <https://www.continuum.io/downloads>`_. Installing ProjectQ right away will succeed for the (slow) Python simulator (i.e., with the `--without-cppsimulator` flag). For a compiled version of the simulator, install the Visual C++ Build Tools and the Microsoft Windows SDK prior to doing a pip install. The built simulator will not support multi-threading due to the limited OpenMP support of msvc.
 
 	Should you want to run multi-threaded simulations, you can install a compiler which supports newer OpenMP versions, such as MinGW GCC and then manually build the C++ simulator with OpenMP enabled.
 
 
 **macOS**:
-
 	These are the steps to install ProjectQ on a new Mac:
 
-	In order to install the fast C++ simulator, we require that your system has a C++ compiler (see option 3 below on how to only install the slower Python simulator via the `--without-cppsimulator` parameter)
-
-	Below you will find two options to install the fast C++ simulator. The first one is the easiest and requires only the standard compiler which Apple distributes with XCode. The second option uses macports to install the simulator with additional support for multi-threading by using OpenMP, which makes it slightly faster. We show how to install the required C++ compiler (clang) which supports OpenMP and additionally, we show how to install a newer python version.
-
-.. note::
-	Depending on your system you might need to use `sudo` for the installation.
-
-1. Installation using XCode and the default python:
-
-	Install XCode by opening a terminal and running the following command:
+	Install XCode:
 
 	.. code-block:: bash
 
 		xcode-select --install
 
-	Next, you will need to install Python and pip. See option 2 for information on how to install a newer python version with macports. Here, we are using the standard python which is preinstalled with macOS. Pip can be installed by:
-
-	.. code-block:: bash
-
-		sudo easy_install pip
-
-	Now, you can install ProjectQ with the C++ simulator using the standard command:
-
-	.. code-block:: bash
-
-		python -m pip install --user projectq
-
-
-2. Installation using macports:
-
-	Either use the standard python and install pip as shown in option 1 or better use macports to install a newer python version, e.g., Python 3.5 and the corresponding pip. Visit `macports.org <https://www.macports.org/install.php>`_ and install the latest version (afterwards open a new terminal). Then, use macports to install Python 3.5 by
+	Next, you need to install Python and pip. One way of doing so is using macports to install Python 3.5 and the corresponding version of pip. Visit `macports.org <https://www.macports.org/install.php>`_ and install the latest version (afterwards open a new terminal). Then, use macports to install Python 3.5 by
 
 	.. code-block:: bash
 
@@ -131,7 +102,7 @@
 
 		sudo port install py35-pip
 
-	Next, we can install ProjectQ with the high performance simulator written in C++. First, we will need to install a suitable compiler with support for **C++11**, OpenMP, and instrinsics. The best option is to install clang 3.9 also using macports (note: gcc installed via macports does not work)
+	Next, we can install ProjectQ with the high performance simulator written in C++. Therefore, we first need to install a suitable compiler which supports OpenMP and instrinsics. One option is to install clang 3.9 also using macports (note: gcc installed via macports does not work as the gcc compiler claims to support instrinsics, while the assembler of gcc does not support it)
 
 	.. code-block:: bash
 
@@ -143,21 +114,27 @@
 
 		env CC=clang-mp-3.9 env CXX=clang++-mp-3.9 python3.5 -m pip install --user projectq
 
-3. Installation with only the slow Python simulator:
-
-	While this simulator works fine for small examples, it is suggested to install the high performance simulator written in C++.
+	If you don't want to install clang 3.9, you can try and specify your preferred compiler by changing CC and CXX in the above command (the compiler must support **C++11**). 
 
-	If you just want to install ProjectQ with the (slow) Python simulator and no compiler, then first try to install ProjectQ with the default compiler 
+	Should something go wrong when compiling the C++ simulator extension in one of the above installation procedures, 
+	you can turn off this feature using the ``--without-cppsimulator`` 
+	parameter (note: this only works if one of the above installation methods has been tried and hence 
+	all requirements are now installed), i.e.,
 
 	.. code-block:: bash
+	
+		python3.5 -m pip install --user --global-option=--without-cppsimulator projectq
 
-		python -m pip install --user projectq
+	While this simulator works fine for small examples, it is suggested to install the high performance simulator written in C++. 
 
-	which most likely will fail. Then, try again with the flag ``--without-cppsimulator``:
+	If you just want to install ProjectQ with the (slow) Python simulator and no compiler, then first try to install ProjectQ with the default compiler 
 
 	.. code-block:: bash
 
-		python -m pip install --user --global-option=--without-cppsimulator projectq
+		python3.5 -m pip install --user projectq
+
+	which most likely will fail and then use the command above using the ``--without-cppsimulator`` 
+	parameter.
 
 
 The ProjectQ syntax
