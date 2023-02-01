17a18
> from importlib.machinery import ModuleSpec
327,329c328
<             self.load_module = self._wrap_load_module(loader.load_module)  # type: ignore
<         if hasattr(loader, 'create_module'):
<             self.create_module = loader.create_module  # type: ignore
---
>             self.load_module = loader.load_module  # type: ignore
332a332,333
>     def create_module(self, spec: ModuleSpec) -> ModuleType:
>         return self.loader.create_module(spec)
335,353d335
<     def _wrap_load_module(self, method: Any) -> Any:
<         def load_module(fullname: str) -> ModuleType:
<             assert fullname == self.old_module_name, (
<                 f"DeprecatedModuleLoader for {self.old_module_name} was asked to "
<                 f"load {fullname}"
<             )
<             if self.new_module_name in sys.modules:
<                 sys.modules[self.old_module_name] = sys.modules[self.new_module_name]
<                 return sys.modules[self.old_module_name]
<             method(self.new_module_name)
<             assert self.new_module_name in sys.modules, (
<                 f"Wrapped loader {self.loader} was "
<                 f"expected to insert "
<                 f"{self.new_module_name} in sys.modules "
<                 f"but it did not."
<             )
<             sys.modules[self.old_module_name] = sys.modules[self.new_module_name]
<             return sys.modules[self.old_module_name]
<         return load_module
