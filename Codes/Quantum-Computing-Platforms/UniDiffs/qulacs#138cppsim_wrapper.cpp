--- qulacs/qulacs#138/after/cppsim_wrapper.cpp	2022-01-10 16:02:54.000000000 +0000
+++ qulacs/qulacs#138/before/cppsim_wrapper.cpp	2022-01-10 16:02:54.000000000 +0000
@@ -34,7 +34,6 @@
 #include <cppsim/state_gpu.hpp>
 #endif
 
-#include <vqcsim/parametric_gate.hpp>
 #include <vqcsim/parametric_gate_factory.hpp>
 #include <vqcsim/parametric_circuit.hpp>
 
@@ -323,11 +322,8 @@
     mgate.def("Instrument", &gate::Instrument, pybind11::return_value_policy::take_ownership);
     mgate.def("Adaptive", &gate::Adaptive, pybind11::return_value_policy::take_ownership);
 
-	py::class_<QuantumGate_SingleParameter, QuantumGateBase>(m, "QuantumGate_SingleParameter")
-		.def("get_parameter_value", &QuantumGate_SingleParameter::get_parameter_value)
-		.def("set_parameter_value", &QuantumGate_SingleParameter::set_parameter_value)
-		;
-	mgate.def("ParametricRX", &gate::ParametricRX);
+    py::class_<QuantumGate_SingleParameter, QuantumGateBase>(m, "QuantumGate_SingleParameter");
+    mgate.def("ParametricRX", &gate::ParametricRX);
     mgate.def("ParametricRY", &gate::ParametricRY);
     mgate.def("ParametricRZ", &gate::ParametricRZ);
     mgate.def("ParametricPauliRotation", &gate::ParametricPauliRotation);
