--- Cirq/Cirq#3948/after/_compat.py	2022-01-10 16:02:54.000000000 +0000
+++ Cirq/Cirq#3948/before/_compat.py	2022-01-10 16:02:54.000000000 +0000
@@ -15,6 +15,7 @@
 """Workarounds for compatibility issues between versions and libraries."""
 import functools
 import importlib
+from importlib.machinery import ModuleSpec
 import os
 import re
 import sys
@@ -324,33 +325,14 @@
         # in older environments this line makes them work as well
         if hasattr(loader, 'load_module'):
             # mypy#2427
-            self.load_module = self._wrap_load_module(loader.load_module)  # type: ignore
-        if hasattr(loader, 'create_module'):
-            self.create_module = loader.create_module  # type: ignore
+            self.load_module = loader.load_module  # type: ignore
         self.old_module_name = old_module_name
         self.new_module_name = new_module_name
 
+    def create_module(self, spec: ModuleSpec) -> ModuleType:
+        return self.loader.create_module(spec)
     def module_repr(self, module: ModuleType) -> str:
         return self.loader.module_repr(module)
-    def _wrap_load_module(self, method: Any) -> Any:
-        def load_module(fullname: str) -> ModuleType:
-            assert fullname == self.old_module_name, (
-                f"DeprecatedModuleLoader for {self.old_module_name} was asked to "
-                f"load {fullname}"
-            )
-            if self.new_module_name in sys.modules:
-                sys.modules[self.old_module_name] = sys.modules[self.new_module_name]
-                return sys.modules[self.old_module_name]
-            method(self.new_module_name)
-            assert self.new_module_name in sys.modules, (
-                f"Wrapped loader {self.loader} was "
-                f"expected to insert "
-                f"{self.new_module_name} in sys.modules "
-                f"but it did not."
-            )
-            sys.modules[self.old_module_name] = sys.modules[self.new_module_name]
-            return sys.modules[self.old_module_name]
-        return load_module
 
     def _wrap_exec_module(self, method: Any) -> Any:
         def exec_module(module: ModuleType) -> None:
