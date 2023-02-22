--- qulacs/qulacs#138/after/parametric_gate.hpp	2022-01-10 16:02:54.000000000 +0000
+++ qulacs/qulacs#138/before/parametric_gate.hpp	2022-01-10 16:02:54.000000000 +0000
@@ -18,9 +18,6 @@
 #include <complex.h>
 #endif
 
-#ifdef _USE_GPU
-#include <gpusim/update_ops_cuda.h>
-#endif
 
 class QuantumGate_SingleParameter : public QuantumGateBase {
 protected:
@@ -38,24 +35,14 @@
 class QuantumGate_SingleParameterOneQubitRotation : public QuantumGate_SingleParameter {
 protected:
     typedef void (T_UPDATE_FUNC)(UINT, double, CTYPE*, ITYPE);
-	typedef void (T_GPU_UPDATE_FUNC)(UINT, double, void*, ITYPE);
-	T_UPDATE_FUNC* _update_func;
-	T_GPU_UPDATE_FUNC* _update_func_gpu;
+    T_UPDATE_FUNC* _update_func;
 
     QuantumGate_SingleParameterOneQubitRotation(double angle) : QuantumGate_SingleParameter(angle) {
         _angle = angle;
     };
 public:
     virtual void update_quantum_state(QuantumStateBase* state) override {
-#ifdef _USE_GPU
-		if (state->get_device_name() == "gpu") {
-			_update_func_gpu(this->_target_qubit_list[0].index(), _angle, state->data(), state->dim);
-		}
-		else {
-			_update_func(this->_target_qubit_list[0].index(), _angle, state->data_c(), state->dim);
-		}
-#else
-#endif
+        _update_func(this->_target_qubit_list[0].index(), _angle, state->data_c(), state->dim);
     };
 };
 
@@ -65,9 +52,6 @@
 	ClsParametricRXGate(UINT target_qubit_index, double angle) : QuantumGate_SingleParameterOneQubitRotation(angle) {
 		this->_name = "ParametricRX";
 		this->_update_func = RX_gate;
-#ifdef _USE_GPU
-		this->_update_func_gpu = RX_gate_host;
-#endif
 		this->_target_qubit_list.push_back(TargetQubitInfo(target_qubit_index, FLAG_X_COMMUTE));
 	}
 	virtual void set_matrix(ComplexMatrix& matrix) const override {
@@ -84,9 +68,6 @@
 	ClsParametricRYGate(UINT target_qubit_index, double angle) : QuantumGate_SingleParameterOneQubitRotation(angle) {
 		this->_name = "ParametricRY";
 		this->_update_func = RY_gate;
-#ifdef _USE_GPU
-		this->_update_func_gpu = RY_gate_host;
-#endif
 		this->_target_qubit_list.push_back(TargetQubitInfo(target_qubit_index, FLAG_Y_COMMUTE));
 	}
 	virtual void set_matrix(ComplexMatrix& matrix) const override {
@@ -103,9 +84,6 @@
 	ClsParametricRZGate(UINT target_qubit_index, double angle) : QuantumGate_SingleParameterOneQubitRotation(angle) {
 		this->_name = "ParametricRZ";
 		this->_update_func = RZ_gate;
-#ifdef _USE_GPU
-		this->_update_func_gpu = RZ_gate_host;
-#endif
 		this->_target_qubit_list.push_back(TargetQubitInfo(target_qubit_index, FLAG_Z_COMMUTE));
 	}
 	virtual void set_matrix(ComplexMatrix& matrix) const override {
@@ -143,22 +121,9 @@
     virtual void update_quantum_state(QuantumStateBase* state) override {
         auto target_index_list = _pauli->get_index_list();
         auto pauli_id_list = _pauli->get_pauli_id_list();
-#ifdef _USE_GPU
-		if (state->get_device_name() == "gpu") {
-			multi_qubit_Pauli_rotation_gate_partial_list_host(
-				target_index_list.data(), pauli_id_list.data(), (UINT)target_index_list.size(),
-				_angle, state->data(), state->dim);
-		}
-		else {
-			multi_qubit_Pauli_rotation_gate_partial_list(
-				target_index_list.data(), pauli_id_list.data(), (UINT)target_index_list.size(),
-				_angle, state->data_c(), state->dim);
-		}
-#else
         multi_qubit_Pauli_rotation_gate_partial_list(
             target_index_list.data(), pauli_id_list.data(), (UINT)target_index_list.size(),
             _angle, state->data_c(), state->dim);
-#endif
     };
     virtual QuantumGateBase* copy() const override {
         return new ClsParametricPauliRotationGate(_angle, _pauli->copy());
