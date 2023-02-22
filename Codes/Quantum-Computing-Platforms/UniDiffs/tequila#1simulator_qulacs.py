--- tequila/tequila#1/after/simulator_qulacs.py	2022-01-10 16:02:54.000000000 +0000
+++ tequila/tequila#1/before/simulator_qulacs.py	2022-01-10 16:02:54.000000000 +0000
@@ -4,7 +4,6 @@
 from tequila.utils.bitstrings import BitNumbering, BitString, BitStringLSB
 from tequila.wavefunction.qubit_wavefunction import QubitWaveFunction
 from tequila.simulators.simulator_base import BackendCircuit, BackendExpectationValue, QCircuit, change_basis
-from tequila.utils.keymap import KeyMapRegisterToSubregister
 
 """
 Developer Note:
@@ -100,19 +99,30 @@
                 result._state[converted_key] += 1
             else:
                 result._state[converted_key] = 1
-        if hasattr(self, "measurements"):
-            mqubits = self.measurements
-            keymap = KeyMapRegisterToSubregister(subregister=mqubits, register=[i for i in range(self.n_qubits)])
-            result = result.apply_keymap(keymap=keymap)
         return result
 
     def do_sample(self, samples, circuit, noise_model=None, initial_state=0, *args, **kwargs) -> QubitWaveFunction:
         state = self.initialize_state(self.n_qubits)
         lsb = BitStringLSB.from_int(initial_state, nbits=self.n_qubits)
         state.set_computational_basis(BitString.from_binary(lsb.binary).integer)
-        circuit.update_quantum_state(state)
-        sampled = state.sampling(samples)
-        return self.convert_measurements(backend_result=sampled)
+        self.circuit.update_quantum_state(state)
+        if hasattr(self, "measurements"):
+            result = {}
+            for sample in range(samples):
+                sample_result = {}
+                for t, m in self.measurements.items():
+                    m.update_quantum_state(state)
+                    sample_result[t] = state.get_classical_value(t)
+                sample_result = dict(sorted(sample_result.items(), key=lambda x: x[0]))
+                binary = BitString.from_array(sample_result.values())
+                if binary in result:
+                    result[binary] += 1
+                else:
+                    result[binary] = 1
+            return QubitWaveFunction(state=result)
+        else:
+            result = state.sampling(samples)
+        return self.convert_measurements(backend_result=result)
 
     def fast_return(self, abstract_circuit):
         return False
@@ -166,10 +176,14 @@
         circuit.add_gate(qulacs_gate)
 
     def add_measurement(self, gate, circuit, *args, **kwargs):
+        measurements = {t: qulacs.gate.Measurement(t, t) for t in gate.target}
         if hasattr(self, "measurements"):
-            raise TequilaQulacsException("Measurement on qubit {} was given twice".format(key))
+            for key in measurements:
+                if key in self.measurements:
+                    raise TequilaQulacsException("Measurement on qubit {} was given twice".format(key))
+            self.measurements = {**self.measurements, **measurements}
         else:
-            self.measurements = gate.target
+            self.measurements = measurements
 
 
     def add_noise_to_circuit(self,noise_model):
@@ -205,22 +219,6 @@
                                                                                                 max_block_size))
         return circuit
 
-    def sample_all_z_hamiltonian(self, samples, hamiltonian, *args, **kwargs):
-        qubits = [q for q in hamiltonian.qubits if q in self.abstract_qubit_map]
-        if len(qubits) == 0:
-            return sum([ps.coeff for ps in hamiltonian.paulistrings])
-        all_qubit_counts = self.do_sample(samples=samples, circuit=self.circuit, *args, **kwargs)
-        E = 0.0
-        for paulistring in hamiltonian.paulistrings:
-            n_samples = 0
-            Etmp = 0.0
-            for key, count in all_qubit_counts.items():
-                parity = [k for i,k in enumerate(key.array) if i in paulistring._data].count(1)
-                sign = (-1) ** parity
-                Etmp += sign * count
-                n_samples += count
-            E += Etmp / samples * paulistring.coeff
-        return E
 
 class BackendExpectationValueQulacs(BackendExpectationValue):
     BackendCircuitType = BackendCircuitQulacs
@@ -306,43 +304,40 @@
         result = []
         for H in self._abstract_hamiltonians:
             E = 0.0
-            if H.is_all_z():
-                E = self.U.sample_all_z_hamiltonian(samples=samples, hamiltonian=H, *args, **kwargs)
-            else:
-                for ps in H.paulistrings:
-                    bc = QCircuit()
-                    zero_string = False
-                    for idx, p in ps.items():
+            for ps in H.paulistrings:
+                bc = QCircuit()
+                zero_string = False
+                for idx, p in ps.items():
+                    if idx not in self.U.qubit_map:
+                        if p.upper() != "Z":
+                            zero_string = True
+                    else:
+                        bc += change_basis(target=idx, axis=p)
+
+                if zero_string:
+                    continue
+
+                qbc = self.U.create_circuit(abstract_circuit=bc, variables=None)
+                Esamples = []
+                for sample in range(samples):
+                    if self.U.has_noise:
+                        state = self.U.initialize_state()
+                        self.U.circuit.update_quantum_state(state)
+                        state_tmp = state
+                    else:
+                        state_tmp = state.copy()
+                    if len(bc.gates) > 0:  # otherwise there is no basis change (empty qulacs circuit does not work out)
+                        qbc.update_quantum_state(state_tmp)
+                    ps_measure = 1.0
+                    for idx in ps.keys():
                         if idx not in self.U.qubit_map:
-                            if p.upper() != "Z":
-                                zero_string = True
-                        else:
-                            bc += change_basis(target=idx, axis=p)
-
-                    if zero_string:
-                        continue
-
-                    qbc = self.U.create_circuit(abstract_circuit=bc, variables=None)
-                    Esamples = []
-                    for sample in range(samples):
-                        if self.U.has_noise:
-                            state = self.U.initialize_state()
-                            self.U.circuit.update_quantum_state(state)
-                            state_tmp = state
+                            continue  # means its 1 or Z and <0|Z|0> = 1 anyway
                         else:
-                            state_tmp = state.copy()
-                        if len(bc.gates) > 0:  # otherwise there is no basis change (empty qulacs circuit does not work out)
-                            qbc.update_quantum_state(state_tmp)
-                        ps_measure = 1.0
-                        for idx in ps.keys():
-                            if idx not in self.U.qubit_map:
-                                continue  # means its 1 or Z and <0|Z|0> = 1 anyway
-                            else:
-                                M = qulacs.gate.Measurement(self.U.qubit_map[idx], self.U.qubit_map[idx])
-                                M.update_quantum_state(state_tmp)
-                                measured = state_tmp.get_classical_value(self.U.qubit_map[idx])
-                                ps_measure *= (-2.0 * measured + 1.0)  # 0 becomes 1 and 1 becomes -1
-                        Esamples.append(ps_measure)
-                    E += ps.coeff * sum(Esamples) / len(Esamples)
+                            M = qulacs.gate.Measurement(self.U.qubit_map[idx], self.U.qubit_map[idx])
+                            M.update_quantum_state(state_tmp)
+                            measured = state_tmp.get_classical_value(self.U.qubit_map[idx])
+                            ps_measure *= (-2.0 * measured + 1.0)  # 0 becomes 1 and 1 becomes -1
+                    Esamples.append(ps_measure)
+                E += ps.coeff * sum(Esamples) / len(Esamples)
             result.append(E)
         return numpy.asarray(result)
