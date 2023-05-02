114d113
<         self._qubit_observable_set = set()
188,189c187
<         all_qubits = self._moments.qubits.union(self._qubit_observable_set)
<         return len(all_qubits)
---
>         return self._moments.qubit_count
194c192
<         return QubitSet(self._moments.qubits.union(self._qubit_observable_set))
---
>         return QubitSet(self._moments.qubits)
264c262
<             self._add_to_qubit_observable_mapping(result_type_to_add)
---
>             self._add_to_qubit_observable_mapping(result_type)
266d263
<             self._add_to_qubit_observable_set(result_type_to_add)
302,305d298
< 
<     def _add_to_qubit_observable_set(self, result_type: ResultType) -> None:
<         if isinstance(result_type, ObservableResultType) and result_type.target:
<             self._qubit_observable_set.update(result_type.target)
