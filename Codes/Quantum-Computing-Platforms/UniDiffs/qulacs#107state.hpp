--- qulacs/qulacs#107/after/state.hpp	2022-01-10 16:02:54.000000000 +0000
+++ qulacs/qulacs#107/before/state.hpp	2022-01-10 16:02:54.000000000 +0000
@@ -301,7 +301,7 @@
      * @return double 
      */
     virtual double get_zero_probability(UINT target_qubit_index) const override {
-		if (target_qubit_index >= this->qubit_count) {
+		if (target_qubit_index < this->qubit_count) {
 			std::cerr << "Error: QuantumStateCpu::get_zero_probability(UINT): index of target qubit must be smaller than qubit_count" << std::endl;
 			return 0.;
 		}
