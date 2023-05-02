35,37d34
< class classproperty(property):
<     def __get__(self, obj, objtype=None):
<         return super(classproperty, self).__get__(objtype)
43,46c40
<     @classproperty
<     def default_solver(cls):
<         return dict(supported_problem_types__contains='bqm',
<                     order_by='-properties.version')
---
>     def __init__(self, solver=None, connection_close=True, **config):
48c42
<     def __init__(self, **config):
---
>         # we want a Hybrid solver by default, but allow override
51c45,46
<         config.setdefault('connection_close', True)
---
>         if solver is None:
>             solver = {}
53,58c48,56
<         defaults = config.setdefault('defaults', {})
<         if not isinstance(defaults, abc.Mapping):
<             raise TypeError("mapping expected for 'defaults'")
<         defaults.update(solver=self.default_solver)
< 
<         self.client = Client.from_config(**config)
---
>         if isinstance(solver, abc.Mapping):
>             if solver.setdefault('category', 'hybrid') != 'hybrid':
>                 raise ValueError("the only 'category' this sampler supports is 'hybrid'")
>             if solver.setdefault('supported_problem_types__contains', 'bqm') != 'bqm':
>                 raise ValueError("the only problem type this sampler supports is 'bqm'")
> 
>             solver.setdefault('order_by', '-properties.version')
>         self.client = Client.from_config(
>             solver=solver, connection_close=connection_close, **config)
198,203c196
<     @classproperty
<     def default_solver(self):
<         return dict(supported_problem_types__contains='dqm',
<                     order_by='-properties.version')
< 
<     def __init__(self, **config):
---
>     def __init__(self, solver=None, connection_close=True, **config):
207c200,210
<         config.setdefault('connection_close', True)
---
>         if solver is None:
>             solver = {}
> 
>         if isinstance(solver, abc.Mapping):
>             if solver.setdefault('category', 'hybrid') != 'hybrid':
>                 raise ValueError("the only 'category' this sampler supports is 'hybrid'")
>             if solver.setdefault('supported_problem_types__contains', 'dqm') != 'dqm':
>                 raise ValueError("the only problem type this sampler supports is 'dqm'")
> 
>             # prefer the latest version, but allow kwarg override
>             solver.setdefault('order_by', '-properties.version')
209,212c212,213
<         defaults = config.setdefault('defaults', {})
<         if not isinstance(defaults, abc.Mapping):
<             raise TypeError("mapping expected for 'defaults'")
<         defaults.update(solver=self.default_solver)
---
>         self.client = Client.from_config(
>             solver=solver, connection_close=connection_close, **config)
214d214
<         self.client = Client.from_config(**config)
