18c18
< from typing import Any, Callable, Optional, Dict, Tuple, Type
---
> from typing import Any, Callable, Optional, Dict, Tuple
122,142d121
<     return decorator
< def deprecated_class(*, deadline: str, fix: str,
<                      name: Optional[str] = None) -> Callable[[Type], Type]:
<     def decorator(clazz: Type) -> Type:
<         clazz_new = clazz.__new__
<         def patched_new(cls, *args, **kwargs):
<             qualname = (clazz.__qualname__ if name is None else name)
<             print(f"HELLO {qualname}")
<             warnings.warn(
<                 f'{qualname} was used but is deprecated.\n'
<                 f'It will be removed in cirq {deadline}.\n'
<                 f'{fix}\n',
<                 DeprecationWarning,
<                 stacklevel=2)
<             return clazz_new(cls)
<         setattr(clazz, '__new__', patched_new)
<         clazz.__doc__ = (f'THIS CLASS IS DEPRECATED.\n\n'
<                          f'IT WILL BE REMOVED IN `cirq {deadline}`.\n\n'
<                          f'{fix}\n\n'
<                          f'{clazz.__doc__ or ""}')
<         return clazz
