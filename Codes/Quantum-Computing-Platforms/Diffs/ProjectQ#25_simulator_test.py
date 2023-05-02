34,46c34
< def test_is_cpp_simulator_present():
<     import projectq.backends._sim._cppsim
<     assert projectq.backends._sim._cppsim
< def get_available_simulators():
<     result = ["py_simulator"]
<     try:
<         import projectq.backends._sim._cppsim as _
<         result.append("cpp_simulator")
<     except ImportError:
<         # The C++ simulator was either not installed or is misconfigured. Skip.
<         pass
<     return result
< @pytest.fixture(params=get_available_simulators())
---
> @pytest.fixture(params=["cpp_simulator", "py_simulator"])
