--- amazon-braket-sdk-python/amazon-braket-sdk-python#167/after/circuit.py	2022-01-10 16:02:54.000000000 +0000
+++ amazon-braket-sdk-python/amazon-braket-sdk-python#167/before/circuit.py	2022-01-10 16:02:54.000000000 +0000
@@ -111,7 +111,6 @@
         self._result_types: List[ResultType] = []
         self._qubit_observable_mapping: Dict[Union[int, Circuit._ALL_QUBITS], Observable] = {}
         self._qubit_target_mapping: Dict[int, List[int]] = {}
-        self._qubit_observable_set = set()
 
         if addable is not None:
             self.add(addable, *args, **kwargs)
@@ -185,13 +184,12 @@
 
     @property
     def qubit_count(self) -> int:
-        all_qubits = self._moments.qubits.union(self._qubit_observable_set)
-        return len(all_qubits)
+        return self._moments.qubit_count
 
     @property
     def qubits(self) -> QubitSet:
         """QubitSet: Get a copy of the qubits for this circuit."""
-        return QubitSet(self._moments.qubits.union(self._qubit_observable_set))
+        return QubitSet(self._moments.qubits)
 
     def add_result_type(
         self,
@@ -261,9 +259,8 @@
             result_type_to_add = result_type.copy(target=target)
 
         if result_type_to_add not in self._result_types:
-            self._add_to_qubit_observable_mapping(result_type_to_add)
+            self._add_to_qubit_observable_mapping(result_type)
             self._result_types.append(result_type_to_add)
-            self._add_to_qubit_observable_set(result_type_to_add)
         return self
 
     def _add_to_qubit_observable_mapping(self, result_type: ResultType) -> None:
@@ -300,10 +297,6 @@
         if not result_type.target:
             self._qubit_observable_mapping[Circuit._ALL_QUBITS] = observable
 
-    def _add_to_qubit_observable_set(self, result_type: ResultType) -> None:
-        if isinstance(result_type, ObservableResultType) and result_type.target:
-            self._qubit_observable_set.update(result_type.target)
-
     def add_instruction(
         self,
         instruction: Instruction,
