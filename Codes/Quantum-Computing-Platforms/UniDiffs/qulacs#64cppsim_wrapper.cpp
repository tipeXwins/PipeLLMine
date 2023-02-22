--- qulacs/qulacs#64/after/cppsim_wrapper.cpp	2022-01-10 16:02:54.000000000 +0000
+++ qulacs/qulacs#64/before/cppsim_wrapper.cpp	2022-01-10 16:02:54.000000000 +0000
@@ -255,7 +255,7 @@
         .def("add_parametric_gate", (void (ParametricQuantumCircuit::*)(QuantumGate_SingleParameter* gate))  &ParametricQuantumCircuit::add_parametric_gate)
         .def("add_parametric_gate", (void (ParametricQuantumCircuit::*)(QuantumGate_SingleParameter* gate, UINT))  &ParametricQuantumCircuit::add_parametric_gate)
         .def("add_gate", (void (ParametricQuantumCircuit::*)(QuantumGateBase* gate))  &ParametricQuantumCircuit::add_gate )
-        .def("add_gate", (void (ParametricQuantumCircuit::*)(QuantumGateBase* gate, unsigned int))  &ParametricQuantumCircuit::add_gate)
+        .def("add_gate", (void (ParametricQuantumCircuit::*)(QuantumGateBase* gate))  &ParametricQuantumCircuit::add_gate)
         .def("get_parameter_count", &ParametricQuantumCircuit::get_parameter_count)
         .def("get_parameter", &ParametricQuantumCircuit::get_parameter)
         .def("set_parameter", &ParametricQuantumCircuit::set_parameter)
