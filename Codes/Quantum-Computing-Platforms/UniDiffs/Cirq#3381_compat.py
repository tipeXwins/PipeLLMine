--- Cirq/Cirq#3381/after/_compat.py	2022-01-10 16:02:54.000000000 +0000
+++ Cirq/Cirq#3381/before/_compat.py	2022-01-10 16:02:54.000000000 +0000
@@ -15,7 +15,7 @@
 """Workarounds for compatibility issues between versions and libraries."""
 import functools
 import warnings
-from typing import Any, Callable, Optional, Dict, Tuple, Type
+from typing import Any, Callable, Optional, Dict, Tuple
 from types import ModuleType
 
 import numpy as np
@@ -120,27 +120,6 @@
         return decorated_func
 
     return decorator
-def deprecated_class(*, deadline: str, fix: str,
-                     name: Optional[str] = None) -> Callable[[Type], Type]:
-    def decorator(clazz: Type) -> Type:
-        clazz_new = clazz.__new__
-        def patched_new(cls, *args, **kwargs):
-            qualname = (clazz.__qualname__ if name is None else name)
-            print(f"HELLO {qualname}")
-            warnings.warn(
-                f'{qualname} was used but is deprecated.\n'
-                f'It will be removed in cirq {deadline}.\n'
-                f'{fix}\n',
-                DeprecationWarning,
-                stacklevel=2)
-            return clazz_new(cls)
-        setattr(clazz, '__new__', patched_new)
-        clazz.__doc__ = (f'THIS CLASS IS DEPRECATED.\n\n'
-                         f'IT WILL BE REMOVED IN `cirq {deadline}`.\n\n'
-                         f'{fix}\n\n'
-                         f'{clazz.__doc__ or ""}')
-        return clazz
-    return decorator
 
 
 def deprecated_parameter(
