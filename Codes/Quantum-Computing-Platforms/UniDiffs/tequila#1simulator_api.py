--- tequila/tequila#1/after/simulator_api.py	2022-01-10 16:02:54.000000000 +0000
+++ tequila/tequila#1/before/simulator_api.py	2022-01-10 16:02:54.000000000 +0000
@@ -2,16 +2,14 @@
 import typing, warnings
 from numbers import Real as RealNumber
 from typing import Dict, Union, Hashable
-import pkg_resources
-from pkg_resources import DistributionNotFound
 
 from tequila.objective import Objective, Variable, assign_variable, format_variable_dictionary
 from tequila.utils.exceptions import TequilaException, TequilaWarning
 from tequila.simulators.simulator_base import BackendCircuit, BackendExpectationValue
 from tequila.circuit.noise import NoiseModel
 
-SUPPORTED_BACKENDS = ["qulacs_gpu", "qulacs", "qiskit", "cirq", "pyquil", "symbolic"]
-SUPPORTED_NOISE_BACKENDS = ["qiskit", 'cirq', 'pyquil', 'qulacs', "qulacs_gpu"]
+SUPPORTED_BACKENDS = ["qulacs", "qiskit", "cirq", "pyquil", "symbolic"]
+SUPPORTED_NOISE_BACKENDS = ["qiskit", 'cirq', 'pyquil', 'qulacs']
 BackendTypes = namedtuple('BackendTypes', 'CircType ExpValueType')
 INSTALLED_SIMULATORS = {}
 INSTALLED_SAMPLERS = {}
@@ -70,7 +68,6 @@
     HAS_CIRQ = False
 
 try:
-    pkg_resources.require("qulacs")
     import qulacs
     from tequila.simulators.simulator_qulacs import BackendCircuitQulacs, BackendExpectationValueQulacs
 
@@ -91,24 +88,11 @@
                                                 ExpValueType=BackendExpectationValueQulacs)
     INSTALLED_NOISE_SAMPLERS["qulacs"] = BackendTypes(CircType=BackendCircuitQulacs,
                                                       ExpValueType=BackendExpectationValueQulacs)
-except (ImportError, DistributionNotFound):
+except ImportError:
     HAS_QULACS = False
 
-try:
-    pkg_resources.require("qulacs-gpu")
-    import qulacs
-    from tequila.simulators.simulator_qulacs_gpu import BackendCircuitQulacsGpu, BackendExpectationValueQulacsGpu
-
-    HAS_QULACS_GPU = True
-    INSTALLED_SIMULATORS["qulacs_gpu"] = BackendTypes(CircType=BackendCircuitQulacsGpu,
-                                                  ExpValueType=BackendExpectationValueQulacsGpu)
-    INSTALLED_SAMPLERS["qulacs_gpu"] = BackendTypes(CircType=BackendCircuitQulacsGpu,
-                                                ExpValueType=BackendExpectationValueQulacsGpu)
-    INSTALLED_NOISE_SAMPLERS["qulacs_gpu"] = BackendTypes(CircType=BackendCircuitQulacsGpu,
-                                                      ExpValueType=BackendExpectationValueQulacsGpu)
-except (ImportError, DistributionNotFound):
-    HAS_QULACS_GPU = False
 HAS_PYQUIL = True
+from shutil import which
 
 try:
     from tequila.simulators.simulator_pyquil import BackendCircuitPyquil, BackendExpectationValuePyquil
@@ -149,7 +133,7 @@
                                                              str(k in INSTALLED_BACKENDS)))
 
 
-def pick_backend(backend: str = None, samples: int = None, noise: NoiseModel = None, device: str = None,
+def pick_backend(backend: str = None, samples: int = None, noise: NoiseModel = None,
                  exclude_symbolic: bool = True) -> str:
     """
     verifies if the backend is installed and picks one automatically if set to None
@@ -163,8 +147,6 @@
     if len(INSTALLED_SIMULATORS) == 0:
         raise TequilaException("No simulators installed on your system")
 
-    if backend is None and device is not None:
-        raise TequilaException('device use requires backend specification!')
     if backend is None:
         if noise is None:
             if samples is None:
@@ -176,24 +158,18 @@
                 for f in INSTALLED_SAMPLERS.keys():
                     return f
         else:
-            if samples is None:
-                raise TequilaException(
-                    "Noise requires sampling; please provide a positive, integer value for samples")
             for f in SUPPORTED_NOISE_BACKENDS:
-                if noise == 'device':
-                    raise TequilaException('device noise requires a device, which requires a named backend!')
+                if samples is None:
+                    raise TequilaException(
+                        "Noise requires sampling; please provide a positive, integer value for samples")
                 else:
-                    return f
-            raise TequilaException(
-                            'Could not find any installed sampler!')
-
+                    if f in INSTALLED_NOISE_SAMPLERS:
+                        return f
 
     if hasattr(backend, "lower"):
         backend = backend.lower()
 
     if backend == "random":
-        if device is not None:
-            raise TequilaException('cannot ask for a random backend and a specific device!')
         from numpy import random as random
         import time
         state = random.RandomState(int(str(time.process_time()).split('.')[-1]) % 2 ** 32)
@@ -216,19 +192,14 @@
                 backend = state.choice(list(INSTALLED_SIMULATORS.keys()), 1)[0]
         return backend
 
-    if device is not None and samples is None:
-        raise TequilaException('Use of a device requires sampling!')
-    if noise == 'device' and device is None:
-        raise TequilaException('Use of device noise requires a device!')
-
     if backend not in SUPPORTED_BACKENDS:
         raise TequilaException("Backend {backend} not supported ".format(backend=backend))
 
-    elif noise is False and samples is None and backend not in INSTALLED_SIMULATORS.keys():
+    if noise is False and samples is None and backend not in INSTALLED_SIMULATORS:
+        raise TequilaException("Backend {backend} not installed ".format(backend=backend))
+    elif noise is False and samples is not None and backend not in INSTALLED_SAMPLERS:
         raise TequilaException("Backend {backend} not installed ".format(backend=backend))
-    elif noise is False and samples is not None and backend not in INSTALLED_SAMPLERS.keys():
-        raise TequilaException("Backend {backend} not installed or sampling not supported".format(backend=backend))
-    elif noise is not False and samples is not None and backend not in INSTALLED_NOISE_SAMPLERS.keys():
+    elif noise is not False and samples is not None and backend not in INSTALLED_NOISE_SAMPLERS:
         raise TequilaException(
             "Backend {backend} not installed or else Noise has not been implemented".format(backend=backend))
 
@@ -239,7 +210,6 @@
                       variables: typing.Dict['Variable', 'RealNumber'] = None,
                       backend: str = None,
                       samples: int = None,
-                      device: str = None,
                       noise: NoiseModel = None,
                       *args,
                       **kwargs) -> Objective:
@@ -265,7 +235,7 @@
     :return: Compiled Objective
     """
 
-    backend = pick_backend(backend=backend, samples=samples, noise=noise, device=device)
+    backend = pick_backend(backend=backend, samples=samples, noise=noise)
 
     # dummy variables
     if variables is None:
@@ -299,7 +269,7 @@
     for arg in objective.args:
         if hasattr(arg, "H") and hasattr(arg, "U") and not isinstance(arg, BackendExpectationValue):
             if arg not in expectationvalues:
-                compiled_expval = ExpValueType(arg, variables=variables, noise=noise, device=device)
+                compiled_expval = ExpValueType(arg, variables, noise)
                 expectationvalues[arg] = compiled_expval
             else:
                 compiled_expval = expectationvalues[arg]
@@ -322,7 +292,6 @@
                     backend: str = None,
                     samples: int = None,
                     noise: NoiseModel = None,
-                    device: str = None,
                     *args,
                     **kwargs) -> BackendCircuit:
     """
@@ -347,7 +316,7 @@
     """
 
     CircType = INSTALLED_SIMULATORS[
-        pick_backend(backend=backend, samples=samples, noise=noise, device=device)].CircType
+        pick_backend(backend=backend, samples=samples, noise=noise)].CircType
 
     # dummy variables
     if variables is None:
@@ -371,7 +340,7 @@
         else:
             return abstract_circuit
 
-    return CircType(abstract_circuit=abstract_circuit, variables=variables, noise=noise, device=device)
+    return CircType(abstract_circuit=abstract_circuit, variables=variables, noise=noise)
 
 
 def simulate(objective: typing.Union['Objective', 'QCircuit'],
@@ -379,7 +348,6 @@
              samples: int = None,
              backend: str = None,
              noise: NoiseModel = None,
-             device: str = None,
              *args,
              **kwargs) -> Union[RealNumber, 'QubitWaveFunction']:
     """Simulate a tequila objective or circuit
@@ -406,8 +374,6 @@
         specify the backend or give None for automatic assignment
     noise: NoiseModel :
         specify a noise model to apply to simulation/sampling
-    device: str:
-        a string (or iff using cirq, a cirq.Device object) upon which (or in emulation of which) to sample
     *args :
     **kwargs :
 
@@ -432,7 +398,7 @@
                 objective.extract_variables()))
 
     compiled_objective = compile(objective=objective, samples=samples, variables=variables, backend=backend,
-                                 noise=noise,device=device, *args, **kwargs)
+                                 noise=noise, *args, **kwargs)
 
     return compiled_objective(variables=variables, samples=samples, *args, **kwargs)
 
@@ -501,7 +467,6 @@
             samples: int = None,
             backend: str = None,
             noise: NoiseModel = None,
-            device: str = None,
             *args,
             **kwargs) -> typing.Union['BackendCircuit', 'Objective']:
     """Compile a tequila objective or circuit to a backend
@@ -526,17 +491,15 @@
         if None a full wavefunction simulation is performed, otherwise a fixed number of samples is simulated
     backend : str : (Default value = None) :
         specify the backend or give None for automatic assignment
-    noise: NoiseModel : (Default value = None) :
+    noise: NoiseModel : (Default value =None) :
         the noise model to apply to the objective or QCircuit.
-    device: str: (Default value = None) :
-        a device on which (or in emulation of which) to sample the circuit.
     Returns
     -------
     simulators.BackendCircuit
         simulated/sampled objective or simulated/sampled wavefunction
     """
 
-    backend = pick_backend(backend=backend, noise=noise, samples=samples, device=device)
+    backend = pick_backend(backend=backend, noise=noise, samples=samples)
 
     if variables is None and not (len(objective.extract_variables()) == 0):
         variables = {key: 0.0 for key in objective.extract_variables()}
@@ -555,10 +518,10 @@
         variables = {assign_variable(k): v for k, v in variables.items()}
 
     if isinstance(objective, Objective) or hasattr(objective, "args"):
-        return compile_objective(objective=objective, samples=samples, variables=variables, backend=backend, noise=noise, device=device)
+        return compile_objective(objective=objective, variables=variables, backend=backend, noise=noise)
     elif hasattr(objective, "gates") or hasattr(objective, "abstract_circuit"):
-        return compile_circuit(abstract_circuit=objective, variables=variables, backend=backend,samples=samples,
-                               noise=noise, device=device, *args, **kwargs)
+        return compile_circuit(abstract_circuit=objective, variables=variables, backend=backend,
+                               noise=noise, *args, **kwargs)
     else:
         raise TequilaException(
             "Don't know how to compile object of type: {type}, \n{object}".format(type=type(objective),
