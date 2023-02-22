--- ProjectQ/ProjectQ#25/after/_simulator_test.py	2022-01-10 16:02:54.000000000 +0000
+++ ProjectQ/ProjectQ#25/before/_simulator_test.py	2022-01-10 16:02:54.000000000 +0000
@@ -31,19 +31,7 @@
 from projectq.backends import Simulator
 
 
-def test_is_cpp_simulator_present():
-    import projectq.backends._sim._cppsim
-    assert projectq.backends._sim._cppsim
-def get_available_simulators():
-    result = ["py_simulator"]
-    try:
-        import projectq.backends._sim._cppsim as _
-        result.append("cpp_simulator")
-    except ImportError:
-        # The C++ simulator was either not installed or is misconfigured. Skip.
-        pass
-    return result
-@pytest.fixture(params=get_available_simulators())
+@pytest.fixture(params=["cpp_simulator", "py_simulator"])
 def sim(request):
     if request.param == "cpp_simulator":
         from projectq.backends._sim._cppsim import Simulator as CppSim
