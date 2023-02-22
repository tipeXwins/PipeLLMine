--- qulacs/qulacs#251/after/general_quantum_operator.cpp	2022-01-10 16:02:54.000000000 +0000
+++ qulacs/qulacs#251/before/general_quantum_operator.cpp	2022-01-10 16:02:54.000000000 +0000
@@ -48,7 +48,6 @@
         this->_is_hermitian = false;
     }
 	this->add_operator(_mpt);
-    delete _mpt;
 }
 
 CPPCTYPE GeneralQuantumOperator::get_expectation_value(const QuantumStateBase* state) const {
