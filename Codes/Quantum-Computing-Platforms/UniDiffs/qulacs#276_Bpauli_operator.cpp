--- qulacs/qulacs#276_B/after/pauli_operator.cpp	2022-01-10 16:02:54.000000000 +0000
+++ qulacs/qulacs#276_B/before/pauli_operator.cpp	2022-01-10 16:02:54.000000000 +0000
@@ -92,11 +92,6 @@
 }
 
 CPPCTYPE PauliOperator::get_expectation_value(const QuantumStateBase* state) const {
-    if (state->qubit_count < this->get_qubit_count()) {
-        std::cerr << "Error: PauliOperator::get_expectation_value(QuantumStateBase*) : The number of qubit in PauliOperator is greater than QuantumState. PauliOperator: " 
-               << this -> get_qubit_count() << " QuantumState: " << state -> qubit_count << std::endl;
-        return CPPCTYPE(std::nan(""), std::nan(""));
-    }
 	if(state->is_state_vector()){
 #ifdef _USE_GPU
 		if (state->get_device_name() == "gpu") {
@@ -110,6 +105,15 @@
 				state->device_number
 			);
 		}
+		else {
+			return _coef * expectation_value_multi_qubit_Pauli_operator_partial_list(
+				this->get_index_list().data(),
+				this->get_pauli_id_list().data(),
+				(UINT)this->get_index_list().size(),
+				state->data_c(),
+				state->dim
+			);
+		}
 #else
 		return _coef * expectation_value_multi_qubit_Pauli_operator_partial_list(
 			this->get_index_list().data(),
