--- qulacs/qulacs#73/after/observable.cpp	2022-01-10 16:02:54.000000000 +0000
+++ qulacs/qulacs#73/before/observable.cpp	2022-01-10 16:02:54.000000000 +0000
@@ -13,28 +13,69 @@
 #include <iostream>
 #include <utility>
 
-void HermitianQuantumOperator::add_operator(const PauliOperator* mpt){
-    if (std::abs(mpt->get_coef().imag()) > 0){
-        std::cerr << "Error: HermitianQuantumOperator::add_operator(const PauliOperator* mpt): PauliOperator must be Hermitian." << std::endl;
-        return;
+bool check_Pauli_operator(const Observable* observable, const PauliOperator* pauli_operator);
+bool check_Pauli_operator(const Observable* observable, const PauliOperator* pauli_operator) {
+	auto vec = pauli_operator->get_index_list();
+	UINT val = 0;
+	if (vec.size() > 0) {
+		val = std::max(val, *std::max_element(vec.begin(), vec.end()));
+	}
+	return val < (observable->get_qubit_count());
+}
+Observable::Observable(UINT qubit_count){
+    _qubit_count = qubit_count;
+}
+Observable::~Observable(){
+    for(auto& term : this->_operator_list){
+        delete term;
     }
-    GeneralQuantumOperator::add_operator(mpt);
 }
 
-void HermitianQuantumOperator::add_operator(CPPCTYPE coef, std::string pauli_string) {
-    if (std::abs(coef.imag()) > 0){
-        std::cerr << "Error: HermitianQuantumOperator::add_operator(const PauliOperator* mpt): PauliOperator must be Hermitian." << std::endl;
-        return;
+void Observable::add_operator(const PauliOperator* mpt){
+    PauliOperator* _mpt = mpt->copy();
+	if (!check_Pauli_operator(this, _mpt)) {
+		std::cerr << "Error: Observable::add_operator(const PauliOperator*): pauli_operator applies target qubit of which the index is larger than qubit_count" << std::endl;
+		return;
+	}
+    this->_operator_list.push_back(_mpt);
+}
+
+void Observable::add_operator(CPPCTYPE coef, std::string pauli_string) {
+	PauliOperator* _mpt = new PauliOperator(pauli_string, coef);
+	if (!check_Pauli_operator(this, _mpt)) {
+		std::cerr << "Error: Observable::add_operator(double,std::string): pauli_operator applies target qubit of which the index is larger than qubit_count" << std::endl;
+		return;
+	}
+	this->add_operator(_mpt);
+}
+
+CPPCTYPE Observable::get_expectation_value(const QuantumStateBase* state) const {
+	if (this->_qubit_count != state->qubit_count) {
+		std::cerr << "Error: Observable::get_expectation_value(const QuantumStateBase*): invalid qubit count" << std::endl;
+		return 0.;
+	}
+    CPPCTYPE sum = 0;
+    for (auto pauli : this->_operator_list) {
+        sum += pauli->get_expectation_value(state);
     }
-	GeneralQuantumOperator::add_operator(coef, pauli_string);
+    return sum;
 }
 
-CPPCTYPE HermitianQuantumOperator::get_expectation_value(const QuantumStateBase* state) const {
-    return GeneralQuantumOperator::get_expectation_value(state).real();
+CPPCTYPE Observable::get_transition_amplitude(const QuantumStateBase* state_bra, const QuantumStateBase* state_ket) const {
+	if (this->_qubit_count != state_bra->qubit_count || this->_qubit_count != state_ket->qubit_count) {
+		std::cerr << "Error: Observable::get_transition_amplitude(const QuantumStateBase*, const QuantumStateBase*): invalid qubit count" << std::endl;
+		return 0.;
+	}
+	
+	CPPCTYPE sum = 0;
+    for (auto pauli : this->_operator_list) {
+        sum += pauli->get_transition_amplitude(state_bra, state_ket);
+    }
+    return sum;
 }
 
 namespace observable{
-    HermitianQuantumOperator* create_observable_from_openfermion_file(std::string file_path){
+    Observable* create_observable_from_openfermion_file(std::string file_path){
         UINT qubit_count = 0;
         UINT imag_idx;
         UINT str_idx;
@@ -92,7 +133,7 @@
 		}
         ifs.close();
 
-        HermitianQuantumOperator* observable = new HermitianQuantumOperator(qubit_count);
+        Observable* observable = new Observable(qubit_count);
 
         for (UINT i = 0; i < ops.size(); ++i){
             observable->add_operator(new PauliOperator(ops[i].c_str(), coefs[i]));
@@ -101,7 +142,7 @@
         return observable;
     }
 
-    HermitianQuantumOperator* create_observable_from_openfermion_text(std::string text){
+    Observable* create_observable_from_openfermion_text(std::string text){
         UINT qubit_count = 0;
         UINT imag_idx;
         UINT str_idx;
@@ -149,7 +190,7 @@
             }
         }
 
-        HermitianQuantumOperator* observable = new HermitianQuantumOperator(qubit_count);
+        Observable* observable = new Observable(qubit_count);
 
         for (UINT i = 0; i < ops.size(); ++i){
             observable->add_operator(new PauliOperator(ops[i].c_str(), coefs[i]));
@@ -158,7 +199,7 @@
         return observable;
     }
 
-    std::pair<HermitianQuantumOperator*, HermitianQuantumOperator*> create_split_observable(std::string file_path){
+    std::pair<Observable*, Observable*> create_split_observable(std::string file_path){
         UINT qubit_count = 0;
         UINT imag_idx;
         UINT str_idx;
@@ -167,7 +208,7 @@
 
         if (!ifs){
             std::cerr << "ERROR: Cannot open file" << std::endl;
-			return std::make_pair((HermitianQuantumOperator*)NULL, (HermitianQuantumOperator*)NULL);
+			return std::make_pair((Observable*)NULL, (Observable*)NULL);
         }
 
         // loading lines and check qubit_count
@@ -212,12 +253,12 @@
         }
         if (!ifs.eof()){
             std::cerr << "ERROR: Invalid format" << std::endl;
-			return std::make_pair((HermitianQuantumOperator*)NULL, (HermitianQuantumOperator*)NULL);
+			return std::make_pair((Observable*)NULL, (Observable*)NULL);
 		}
         ifs.close();
 
-        HermitianQuantumOperator* observable_diag =  new HermitianQuantumOperator(qubit_count);
-        HermitianQuantumOperator* observable_non_diag =  new HermitianQuantumOperator(qubit_count);
+        Observable* observable_diag =  new Observable(qubit_count);
+        Observable* observable_non_diag =  new Observable(qubit_count);
 
         for (UINT i = 0; i < ops.size(); ++i){
             if (ops[i].find("X") != std::string::npos || ops[i].find("Y") != std::string::npos){
