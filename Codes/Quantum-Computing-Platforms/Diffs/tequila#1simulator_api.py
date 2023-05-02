5,6d4
< import pkg_resources
< from pkg_resources import DistributionNotFound
13,14c11,12
< SUPPORTED_BACKENDS = ["qulacs_gpu", "qulacs", "qiskit", "cirq", "pyquil", "symbolic"]
< SUPPORTED_NOISE_BACKENDS = ["qiskit", 'cirq', 'pyquil', 'qulacs', "qulacs_gpu"]
---
> SUPPORTED_BACKENDS = ["qulacs", "qiskit", "cirq", "pyquil", "symbolic"]
> SUPPORTED_NOISE_BACKENDS = ["qiskit", 'cirq', 'pyquil', 'qulacs']
73d70
<     pkg_resources.require("qulacs")
94c91
< except (ImportError, DistributionNotFound):
---
> except ImportError:
97,110d93
< try:
<     pkg_resources.require("qulacs-gpu")
<     import qulacs
<     from tequila.simulators.simulator_qulacs_gpu import BackendCircuitQulacsGpu, BackendExpectationValueQulacsGpu
< 
<     HAS_QULACS_GPU = True
<     INSTALLED_SIMULATORS["qulacs_gpu"] = BackendTypes(CircType=BackendCircuitQulacsGpu,
<                                                   ExpValueType=BackendExpectationValueQulacsGpu)
<     INSTALLED_SAMPLERS["qulacs_gpu"] = BackendTypes(CircType=BackendCircuitQulacsGpu,
<                                                 ExpValueType=BackendExpectationValueQulacsGpu)
<     INSTALLED_NOISE_SAMPLERS["qulacs_gpu"] = BackendTypes(CircType=BackendCircuitQulacsGpu,
<                                                       ExpValueType=BackendExpectationValueQulacsGpu)
< except (ImportError, DistributionNotFound):
<     HAS_QULACS_GPU = False
111a95
> from shutil import which
152c136
< def pick_backend(backend: str = None, samples: int = None, noise: NoiseModel = None, device: str = None,
---
> def pick_backend(backend: str = None, samples: int = None, noise: NoiseModel = None,
166,167d149
<     if backend is None and device is not None:
<         raise TequilaException('device use requires backend specification!')
179,181d160
<             if samples is None:
<                 raise TequilaException(
<                     "Noise requires sampling; please provide a positive, integer value for samples")
183,184c162,164
<                 if noise == 'device':
<                     raise TequilaException('device noise requires a device, which requires a named backend!')
---
>                 if samples is None:
>                     raise TequilaException(
>                         "Noise requires sampling; please provide a positive, integer value for samples")
186,189c166,167
<                     return f
<             raise TequilaException(
<                             'Could not find any installed sampler!')
< 
---
>                     if f in INSTALLED_NOISE_SAMPLERS:
>                         return f
195,196d172
<         if device is not None:
<             raise TequilaException('cannot ask for a random backend and a specific device!')
219,223d194
<     if device is not None and samples is None:
<         raise TequilaException('Use of a device requires sampling!')
<     if noise == 'device' and device is None:
<         raise TequilaException('Use of device noise requires a device!')
< 
227c198,200
<     elif noise is False and samples is None and backend not in INSTALLED_SIMULATORS.keys():
---
>     if noise is False and samples is None and backend not in INSTALLED_SIMULATORS:
>         raise TequilaException("Backend {backend} not installed ".format(backend=backend))
>     elif noise is False and samples is not None and backend not in INSTALLED_SAMPLERS:
229,231c202
<     elif noise is False and samples is not None and backend not in INSTALLED_SAMPLERS.keys():
<         raise TequilaException("Backend {backend} not installed or sampling not supported".format(backend=backend))
<     elif noise is not False and samples is not None and backend not in INSTALLED_NOISE_SAMPLERS.keys():
---
>     elif noise is not False and samples is not None and backend not in INSTALLED_NOISE_SAMPLERS:
242d212
<                       device: str = None,
268c238
<     backend = pick_backend(backend=backend, samples=samples, noise=noise, device=device)
---
>     backend = pick_backend(backend=backend, samples=samples, noise=noise)
302c272
<                 compiled_expval = ExpValueType(arg, variables=variables, noise=noise, device=device)
---
>                 compiled_expval = ExpValueType(arg, variables, noise)
325d294
<                     device: str = None,
350c319
<         pick_backend(backend=backend, samples=samples, noise=noise, device=device)].CircType
---
>         pick_backend(backend=backend, samples=samples, noise=noise)].CircType
374c343
<     return CircType(abstract_circuit=abstract_circuit, variables=variables, noise=noise, device=device)
---
>     return CircType(abstract_circuit=abstract_circuit, variables=variables, noise=noise)
382d350
<              device: str = None,
409,410d376
<     device: str:
<         a string (or iff using cirq, a cirq.Device object) upon which (or in emulation of which) to sample
435c401
<                                  noise=noise,device=device, *args, **kwargs)
---
>                                  noise=noise, *args, **kwargs)
504d469
<             device: str = None,
529c494
<     noise: NoiseModel : (Default value = None) :
---
>     noise: NoiseModel : (Default value =None) :
531,532d495
<     device: str: (Default value = None) :
<         a device on which (or in emulation of which) to sample the circuit.
539c502
<     backend = pick_backend(backend=backend, noise=noise, samples=samples, device=device)
---
>     backend = pick_backend(backend=backend, noise=noise, samples=samples)
558c521
<         return compile_objective(objective=objective, samples=samples, variables=variables, backend=backend, noise=noise, device=device)
---
>         return compile_objective(objective=objective, variables=variables, backend=backend, noise=noise)
560,561c523,524
<         return compile_circuit(abstract_circuit=objective, variables=variables, backend=backend,samples=samples,
<                                noise=noise, device=device, *args, **kwargs)
---
>         return compile_circuit(abstract_circuit=objective, variables=variables, backend=backend,
>                                noise=noise, *args, **kwargs)
