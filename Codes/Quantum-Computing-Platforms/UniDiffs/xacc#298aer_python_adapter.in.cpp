--- xacc/xacc#298/after/aer_python_adapter.in.cpp	2022-01-10 16:02:54.000000000 +0000
+++ xacc/xacc#298/before/aer_python_adapter.in.cpp	2022-01-10 16:02:54.000000000 +0000
@@ -4,8 +4,6 @@
 #ifdef XACC_QISKIT_FOUND
 #include <pybind11/embed.h>
 #include <pybind11/stl.h>
-#include <dlfcn.h>
-#include "xacc_config.hpp"
 #endif
 
 namespace xacc {
@@ -15,15 +13,7 @@
                         const std::vector<int> &uChanLoRefs,
                         const std::string &qObjJson) {
 #ifdef XACC_QISKIT_FOUND
-  static bool PythonInit = false;
-  if (!PythonInit) {
-    if (!XACC_IS_APPLE) {
-      auto libPythonPreload =
-          dlopen("@PYTHON_LIB_NAME@", RTLD_LAZY | RTLD_GLOBAL);
-    }
-    pybind11::initialize_interpreter();
-    PythonInit = true;
-  }
+  pybind11::scoped_interpreter guard{};
   auto py_src = R"#(
 import json, warnings
 import numpy as np
