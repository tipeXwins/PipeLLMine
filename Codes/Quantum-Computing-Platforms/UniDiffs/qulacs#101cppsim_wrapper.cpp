--- qulacs/qulacs#101/after/cppsim_wrapper.cpp	2022-01-10 16:02:54.000000000 +0000
+++ qulacs/qulacs#101/before/cppsim_wrapper.cpp	2022-01-10 16:02:54.000000000 +0000
@@ -52,7 +52,7 @@
         .def("add_single_Pauli", &PauliOperator::add_single_Pauli)
         .def("get_expectation_value", &PauliOperator::get_expectation_value)
         .def("get_transition_amplitude", &PauliOperator::get_transition_amplitude)
-        .def("copy", &PauliOperator::copy, pybind11::return_value_policy::take_ownership)
+        .def("copy", &PauliOperator::copy, pybind11::return_value_policy::automatic_reference)
         ;
 
     py::class_<GeneralQuantumOperator>(m, "GeneralQuantumOperator")
@@ -64,18 +64,15 @@
         .def("get_qubit_count", &GeneralQuantumOperator::get_qubit_count)
         .def("get_state_dim", &GeneralQuantumOperator::get_state_dim)
         .def("get_term_count", &GeneralQuantumOperator::get_term_count)
-        //.def("get_term", &GeneralQuantumOperator::get_term, pybind11::return_value_policy::take_ownership)
-        .def("get_term",[](const GeneralQuantumOperator& quantum_operator, const unsigned int index) {
-            return quantum_operator.get_term(index)->copy();
-        }, pybind11::return_value_policy::take_ownership)
+        .def("get_term", &GeneralQuantumOperator::get_term, pybind11::return_value_policy::automatic_reference)
         .def("get_expectation_value", &GeneralQuantumOperator::get_expectation_value)
         .def("get_transition_amplitude", &GeneralQuantumOperator::get_transition_amplitude)
         //.def_static("get_split_GeneralQuantumOperator", &(GeneralQuantumOperator::get_split_observable));
         ;
     auto mquantum_operator = m.def_submodule("quantum_operator");
-    mquantum_operator.def("create_quantum_operator_from_openfermion_file", &quantum_operator::create_general_quantum_operator_from_openfermion_file, pybind11::return_value_policy::take_ownership);
-    mquantum_operator.def("create_quantum_operator_from_openfermion_text", &quantum_operator::create_general_quantum_operator_from_openfermion_text, pybind11::return_value_policy::take_ownership);
-    mquantum_operator.def("create_split_quantum_operator", &quantum_operator::create_split_general_quantum_operator, pybind11::return_value_policy::take_ownership);
+    mquantum_operator.def("create_quantum_operator_from_openfermion_file", &quantum_operator::create_general_quantum_operator_from_openfermion_file, pybind11::return_value_policy::automatic_reference);
+    mquantum_operator.def("create_quantum_operator_from_openfermion_text", &quantum_operator::create_general_quantum_operator_from_openfermion_text, pybind11::return_value_policy::automatic_reference);
+    mquantum_operator.def("create_split_quantum_operator", &quantum_operator::create_split_general_quantum_operator, pybind11::return_value_policy::automatic_reference);
 
     py::class_<HermitianQuantumOperator, GeneralQuantumOperator>(m, "Observable")
         .def(py::init<unsigned int>())
@@ -85,10 +82,7 @@
         .def("get_qubit_count", &HermitianQuantumOperator::get_qubit_count)
         .def("get_state_dim", &HermitianQuantumOperator::get_state_dim)
         .def("get_term_count", &HermitianQuantumOperator::get_term_count)
-        //.def("get_term", &HermitianQuantumOperator::get_term, pybind11::return_value_policy::take_ownership)
-        .def("get_term",[](const HermitianQuantumOperator& quantum_operator, const unsigned int index) {
-            return quantum_operator.get_term(index)->copy();
-        }, pybind11::return_value_policy::take_ownership)
+        .def("get_term", &HermitianQuantumOperator::get_term, pybind11::return_value_policy::automatic_reference)
         // .def("get_expectation_value", &HermitianQuantumOperator::get_expectation_value)
         .def("get_expectation_value", [](const HermitianQuantumOperator& observable, const QuantumStateBase* state) {
                                           double res = observable.get_expectation_value(state).real();
@@ -97,9 +91,9 @@
         //.def_static("get_split_Observable", &(HermitianQuantumOperator::get_split_observable));
         ;
     auto mobservable = m.def_submodule("observable");
-    mobservable.def("create_observable_from_openfermion_file", &observable::create_observable_from_openfermion_file, pybind11::return_value_policy::take_ownership);
-    mobservable.def("create_observable_from_openfermion_text", &observable::create_observable_from_openfermion_text, pybind11::return_value_policy::take_ownership);
-    mobservable.def("create_split_observable", &observable::create_split_observable, pybind11::return_value_policy::take_ownership);
+    mobservable.def("create_observable_from_openfermion_file", &observable::create_observable_from_openfermion_file, pybind11::return_value_policy::automatic_reference);
+    mobservable.def("create_observable_from_openfermion_text", &observable::create_observable_from_openfermion_text, pybind11::return_value_policy::automatic_reference);
+    mobservable.def("create_split_observable", &observable::create_split_observable, pybind11::return_value_policy::automatic_reference);
 
 
     py::class_<QuantumStateBase>(m, "QuantumStateBase");
@@ -177,7 +171,7 @@
 
     py::class_<QuantumGateBase>(m, "QuantumGateBase")
         .def("update_quantum_state", &QuantumGateBase::update_quantum_state)
-        .def("copy",&QuantumGateBase::copy, pybind11::return_value_policy::take_ownership)
+        .def("copy",&QuantumGateBase::copy, pybind11::return_value_policy::automatic_reference)
         .def("to_string", &QuantumGateBase::to_string)
 
         .def("get_matrix", [](const QuantumGateBase& gate) {
@@ -192,7 +186,7 @@
         .def("update_quantum_state", &QuantumGateMatrix::update_quantum_state)
         .def("add_control_qubit", &QuantumGateMatrix::add_control_qubit)
         .def("multiply_scalar", &QuantumGateMatrix::multiply_scalar)
-        .def("copy", &QuantumGateMatrix::copy, pybind11::return_value_policy::take_ownership)
+        .def("copy", &QuantumGateMatrix::copy, pybind11::return_value_policy::automatic_reference)
         .def("to_string", &QuantumGateMatrix::to_string)
 
         .def("get_matrix", [](const QuantumGateMatrix& gate) {
@@ -204,43 +198,43 @@
         ;
 
     auto mgate = m.def_submodule("gate");
-    mgate.def("Identity", &gate::Identity, pybind11::return_value_policy::take_ownership);
-    mgate.def("X", &gate::X, pybind11::return_value_policy::take_ownership);
-    mgate.def("Y", &gate::Y, pybind11::return_value_policy::take_ownership);
-    mgate.def("Z", &gate::Z, pybind11::return_value_policy::take_ownership);
-    mgate.def("H", &gate::H, pybind11::return_value_policy::take_ownership);
-    mgate.def("S", &gate::S, pybind11::return_value_policy::take_ownership);
-    mgate.def("Sdag", &gate::Sdag, pybind11::return_value_policy::take_ownership);
-    mgate.def("T", &gate::T, pybind11::return_value_policy::take_ownership);
-    mgate.def("Tdag", &gate::Tdag, pybind11::return_value_policy::take_ownership);
-    mgate.def("sqrtX", &gate::sqrtX, pybind11::return_value_policy::take_ownership);
-    mgate.def("sqrtXdag", &gate::sqrtXdag, pybind11::return_value_policy::take_ownership);
-    mgate.def("sqrtY", &gate::sqrtY, pybind11::return_value_policy::take_ownership);
-    mgate.def("sqrtYdag", &gate::sqrtYdag, pybind11::return_value_policy::take_ownership);
-    mgate.def("P0", &gate::P0, pybind11::return_value_policy::take_ownership);
-    mgate.def("P1", &gate::P1, pybind11::return_value_policy::take_ownership);
-
-    mgate.def("U1", &gate::U1, pybind11::return_value_policy::take_ownership);
-    mgate.def("U2", &gate::U2, pybind11::return_value_policy::take_ownership);
-    mgate.def("U3", &gate::U3, pybind11::return_value_policy::take_ownership);
-
-    mgate.def("RX", &gate::RX, pybind11::return_value_policy::take_ownership);
-    mgate.def("RY", &gate::RY, pybind11::return_value_policy::take_ownership);
-    mgate.def("RZ", &gate::RZ, pybind11::return_value_policy::take_ownership);
-
-    mgate.def("CNOT", &gate::CNOT, pybind11::return_value_policy::take_ownership);
-    mgate.def("CZ", &gate::CZ, pybind11::return_value_policy::take_ownership);
-    mgate.def("SWAP", &gate::SWAP, pybind11::return_value_policy::take_ownership);
+    mgate.def("Identity", &gate::Identity, pybind11::return_value_policy::automatic_reference);
+    mgate.def("X", &gate::X, pybind11::return_value_policy::automatic_reference);
+    mgate.def("Y", &gate::Y, pybind11::return_value_policy::automatic_reference);
+    mgate.def("Z", &gate::Z, pybind11::return_value_policy::automatic_reference);
+    mgate.def("H", &gate::H, pybind11::return_value_policy::automatic_reference);
+    mgate.def("S", &gate::S, pybind11::return_value_policy::automatic_reference);
+    mgate.def("Sdag", &gate::Sdag, pybind11::return_value_policy::automatic_reference);
+    mgate.def("T", &gate::T, pybind11::return_value_policy::automatic_reference);
+    mgate.def("Tdag", &gate::Tdag, pybind11::return_value_policy::automatic_reference);
+    mgate.def("sqrtX", &gate::sqrtX, pybind11::return_value_policy::automatic_reference);
+    mgate.def("sqrtXdag", &gate::sqrtXdag, pybind11::return_value_policy::automatic_reference);
+    mgate.def("sqrtY", &gate::sqrtY, pybind11::return_value_policy::automatic_reference);
+    mgate.def("sqrtYdag", &gate::sqrtYdag, pybind11::return_value_policy::automatic_reference);
+    mgate.def("P0", &gate::P0, pybind11::return_value_policy::automatic_reference);
+    mgate.def("P1", &gate::P1, pybind11::return_value_policy::automatic_reference);
+
+    mgate.def("U1", &gate::U1, pybind11::return_value_policy::automatic_reference);
+    mgate.def("U2", &gate::U2, pybind11::return_value_policy::automatic_reference);
+    mgate.def("U3", &gate::U3, pybind11::return_value_policy::automatic_reference);
+
+    mgate.def("RX", &gate::RX, pybind11::return_value_policy::automatic_reference);
+    mgate.def("RY", &gate::RY, pybind11::return_value_policy::automatic_reference);
+    mgate.def("RZ", &gate::RZ, pybind11::return_value_policy::automatic_reference);
+
+    mgate.def("CNOT", &gate::CNOT, pybind11::return_value_policy::automatic_reference);
+    mgate.def("CZ", &gate::CZ, pybind11::return_value_policy::automatic_reference);
+    mgate.def("SWAP", &gate::SWAP, pybind11::return_value_policy::automatic_reference);
 
-    mgate.def("Pauli", &gate::Pauli, pybind11::return_value_policy::take_ownership);
-    mgate.def("PauliRotation", &gate::PauliRotation, pybind11::return_value_policy::take_ownership);
+    mgate.def("Pauli", &gate::Pauli, pybind11::return_value_policy::automatic_reference);
+    mgate.def("PauliRotation", &gate::PauliRotation, pybind11::return_value_policy::automatic_reference);
 
     QuantumGateMatrix*(*ptr1)(unsigned int, ComplexMatrix) = &gate::DenseMatrix;
     QuantumGateMatrix*(*ptr2)(std::vector<unsigned int>, ComplexMatrix) = &gate::DenseMatrix;
-    mgate.def("DenseMatrix", ptr1, pybind11::return_value_policy::take_ownership);
-    mgate.def("DenseMatrix", ptr2, pybind11::return_value_policy::take_ownership);
+    mgate.def("DenseMatrix", ptr1, pybind11::return_value_policy::automatic_reference);
+    mgate.def("DenseMatrix", ptr2, pybind11::return_value_policy::automatic_reference);
 
-	mgate.def("RandomUnitary", &gate::RandomUnitary, pybind11::return_value_policy::take_ownership);
+	mgate.def("RandomUnitary", &gate::RandomUnitary, pybind11::return_value_policy::automatic_reference);
 	
 	mgate.def("BitFlipNoise", &gate::BitFlipNoise);
     mgate.def("DephasingNoise", &gate::DephasingNoise);
@@ -249,22 +243,22 @@
     mgate.def("Measurement", &gate::Measurement);
 
     QuantumGateMatrix*(*ptr3)(const QuantumGateBase*, const QuantumGateBase*) = &gate::merge;
-    mgate.def("merge", ptr3, pybind11::return_value_policy::take_ownership);
+    mgate.def("merge", ptr3, pybind11::return_value_policy::automatic_reference);
 
     QuantumGateMatrix*(*ptr4)(std::vector<const QuantumGateBase*>) = &gate::merge;
-    mgate.def("merge", ptr4, pybind11::return_value_policy::take_ownership);
+    mgate.def("merge", ptr4, pybind11::return_value_policy::automatic_reference);
 
     QuantumGateMatrix*(*ptr5)(const QuantumGateBase*, const QuantumGateBase*) = &gate::add;
-    mgate.def("add", ptr5, pybind11::return_value_policy::take_ownership);
+    mgate.def("add", ptr5, pybind11::return_value_policy::automatic_reference);
 
     QuantumGateMatrix*(*ptr6)(std::vector<const QuantumGateBase*>) = &gate::add;
-    mgate.def("add", ptr6, pybind11::return_value_policy::take_ownership);
+    mgate.def("add", ptr6, pybind11::return_value_policy::automatic_reference);
 
-    mgate.def("to_matrix_gate", &gate::to_matrix_gate, pybind11::return_value_policy::take_ownership);
-    mgate.def("Probabilistic", &gate::Probabilistic, pybind11::return_value_policy::take_ownership);
-    mgate.def("CPTP", &gate::CPTP, pybind11::return_value_policy::take_ownership);
-    mgate.def("Instrument", &gate::Instrument, pybind11::return_value_policy::take_ownership);
-    mgate.def("Adaptive", &gate::Adaptive, pybind11::return_value_policy::take_ownership);
+    mgate.def("to_matrix_gate", &gate::to_matrix_gate, pybind11::return_value_policy::automatic_reference);
+    mgate.def("Probabilistic", &gate::Probabilistic, pybind11::return_value_policy::automatic_reference);
+    mgate.def("CPTP", &gate::CPTP, pybind11::return_value_policy::automatic_reference);
+    mgate.def("Instrument", &gate::Instrument, pybind11::return_value_policy::automatic_reference);
+    mgate.def("Adaptive", &gate::Adaptive, pybind11::return_value_policy::automatic_reference);
 
 
     mgate.def("ParametricRX", &gate::ParametricRX);
@@ -275,12 +269,12 @@
 
     py::class_<QuantumCircuit>(m, "QuantumCircuit")
         .def(py::init<unsigned int>())
-        .def("copy", &QuantumCircuit::copy, pybind11::return_value_policy::take_ownership)
+        .def("copy", &QuantumCircuit::copy, pybind11::return_value_policy::automatic_reference)
         // In order to avoid double release, we force using add_gate_copy in python
         .def("add_gate_consume", (void (QuantumCircuit::*)(QuantumGateBase*))&QuantumCircuit::add_gate)
         .def("add_gate_consume", (void (QuantumCircuit::*)(QuantumGateBase*, unsigned int))&QuantumCircuit::add_gate)
-        .def("add_gate", (void (QuantumCircuit::*)(const QuantumGateBase*))&QuantumCircuit::add_gate_copy)
-        .def("add_gate", (void (QuantumCircuit::*)(const QuantumGateBase*, unsigned int))&QuantumCircuit::add_gate_copy)
+        .def("add_gate", (void (QuantumCircuit::*)(const QuantumGateBase&))&QuantumCircuit::add_gate_copy)
+        .def("add_gate", (void (QuantumCircuit::*)(const QuantumGateBase&, unsigned int))&QuantumCircuit::add_gate_copy)
         .def("remove_gate", &QuantumCircuit::remove_gate)
 
         .def("get_gate", [](const QuantumCircuit& circuit, unsigned int index) -> QuantumGateBase* { 
@@ -289,7 +283,7 @@
 			return NULL;
 		}
 		return circuit.gate_list[index]->copy(); 
-	    }, pybind11::return_value_policy::take_ownership)
+	    }, pybind11::return_value_policy::automatic_reference)
         .def("get_gate_count", [](const QuantumCircuit& circuit) -> unsigned int {return (unsigned int)circuit.gate_list.size(); })
 
         .def("update_quantum_state", (void (QuantumCircuit::*)(QuantumStateBase*))&QuantumCircuit::update_quantum_state)
@@ -337,11 +331,11 @@
 
     py::class_<ParametricQuantumCircuit, QuantumCircuit>(m, "ParametricQuantumCircuit")
         .def(py::init<unsigned int>())
-        .def("copy", &ParametricQuantumCircuit::copy, pybind11::return_value_policy::take_ownership)
+        .def("copy", &ParametricQuantumCircuit::copy, pybind11::return_value_policy::automatic_reference)
         .def("add_parametric_gate", (void (ParametricQuantumCircuit::*)(QuantumGate_SingleParameter* gate))  &ParametricQuantumCircuit::add_parametric_gate)
         .def("add_parametric_gate", (void (ParametricQuantumCircuit::*)(QuantumGate_SingleParameter* gate, UINT))  &ParametricQuantumCircuit::add_parametric_gate)
-        .def("add_gate", (void (ParametricQuantumCircuit::*)(const QuantumGateBase* gate))  &ParametricQuantumCircuit::add_gate_copy )
-        .def("add_gate", (void (ParametricQuantumCircuit::*)(const QuantumGateBase* gate, unsigned int))  &ParametricQuantumCircuit::add_gate_copy)
+        .def("add_gate", (void (ParametricQuantumCircuit::*)(QuantumGateBase* gate))  &ParametricQuantumCircuit::add_gate )
+        .def("add_gate", (void (ParametricQuantumCircuit::*)(QuantumGateBase* gate, unsigned int))  &ParametricQuantumCircuit::add_gate)
         .def("get_parameter_count", &ParametricQuantumCircuit::get_parameter_count)
         .def("get_parameter", &ParametricQuantumCircuit::get_parameter)
         .def("set_parameter", &ParametricQuantumCircuit::set_parameter)
@@ -362,7 +356,7 @@
     py::class_<QuantumCircuitOptimizer>(mcircuit, "QuantumCircuitOptimizer")
         .def(py::init<>())
         .def("optimize", &QuantumCircuitOptimizer::optimize)
-        .def("merge_all", &QuantumCircuitOptimizer::merge_all, pybind11::return_value_policy::take_ownership)
+        .def("merge_all", &QuantumCircuitOptimizer::merge_all, pybind11::return_value_policy::automatic_reference)
         ;
 
     py::class_<QuantumCircuitSimulator>(m, "QuantumCircuitSimulator")
