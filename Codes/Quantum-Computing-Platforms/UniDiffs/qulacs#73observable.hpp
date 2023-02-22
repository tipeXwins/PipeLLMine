--- qulacs/qulacs#73/after/observable.hpp	2022-01-10 16:02:54.000000000 +0000
+++ qulacs/qulacs#73/before/observable.hpp	2022-01-10 16:02:54.000000000 +0000
@@ -1,5 +1,6 @@
 /**
  * @file Observable.hpp
+ * @brief Definition and basic functions for Observable
  */
 
 
@@ -10,16 +11,20 @@
 #include <vector>
 #include <utility>
 #include <string>
-#include "pauli_operator.hpp"
 
 class QuantumStateBase;
 class PauliOperator;
-class GeneralQuantumOperator;
 
 
-class DllExport HermitianQuantumOperator : public GeneralQuantumOperator {
+class DllExport Observable {
+private:
+    //! list of multi pauli term
+    std::vector<PauliOperator*> _operator_list;
+    //! the number of qubits
+    UINT _qubit_count;
 public:
-    using GeneralQuantumOperator::GeneralQuantumOperator;
+    Observable(UINT qubit_count);
+    virtual ~Observable();
 
     /**
      * \~japanese-en
@@ -38,11 +43,24 @@
      */
     void add_operator(CPPCTYPE coef, std::string pauli_string);
 
+    UINT get_qubit_count() const { return _qubit_count; }
+    ITYPE get_state_dim() const { return (1ULL) << _qubit_count; }
+    UINT get_term_count() const { return (UINT)_operator_list.size(); }
+    const PauliOperator* get_term(UINT index) const { 
+		if (index >= _operator_list.size()) {
+			std::cerr << "Error: PauliOperator::get_term(UINT): index out of range" << std::endl;
+			return NULL;
+		}
+		return _operator_list[index]; 
+	}
+    std::vector<PauliOperator*> get_terms() const { return _operator_list;}
+
     CPPCTYPE get_expectation_value(const QuantumStateBase* state) const ;
+    CPPCTYPE get_transition_amplitude(const QuantumStateBase* state_bra, const QuantumStateBase* state_ket) const;
 };
 
 namespace observable{
-    DllExport HermitianQuantumOperator* create_observable_from_openfermion_file(std::string file_path);
+    DllExport Observable* create_observable_from_openfermion_file(std::string file_path);
 
     /**
      * \~japanese-en
@@ -52,7 +70,7 @@
      * @param[in] filename OpenFermion形式のテキスト
      * @return Observableのインスタンス
      **/
-    DllExport HermitianQuantumOperator* create_observable_from_openfermion_text(std::string text);
+    DllExport Observable* create_observable_from_openfermion_text(std::string text);
 
     /**
      * \~japanese-en
@@ -60,6 +78,5 @@
      *
      * @param[in] filename OpenFermion形式のオブザーバブルのファイル名
      */
-    DllExport std::pair<HermitianQuantumOperator*, HermitianQuantumOperator*> create_split_observable(std::string file_path);
+    DllExport std::pair<Observable*, Observable*> create_split_observable(std::string file_path);
 }
-typedef HermitianQuantumOperator Observable;
