--- pyquil/pyquil#384/after/noise.py	2022-01-10 16:02:54.000000000 +0000
+++ pyquil/pyquil#384/before/noise.py	2022-01-10 16:02:54.000000000 +0000
@@ -296,35 +296,22 @@
 
 # You can only apply gate-noise to non-parametrized gates or parametrized gates at fixed parameters.
 NO_NOISE = ["RZ"]
-ANGLE_TOLERANCE = 1e-10
-class NoisyGateUndefined(Exception):
-    params = tuple(params)
-    if gate_name == "I":
-        assert params == ()
-        return np.eye(2), "NOISY-I"
-    if gate_name == "RX":
-        angle, = params
-        if np.isclose(angle, np.pi / 2, atol=ANGLE_TOLERANCE):
-            return (np.array([[1, -1j],
-                              [-1j, 1]]) / np.sqrt(2),
-                    "NOISY-RX-PLUS-90")
-        elif np.isclose(angle, -np.pi / 2, atol=ANGLE_TOLERANCE):
-            return (np.array([[1, 1j],
-                              [1j, 1]]) / np.sqrt(2),
-                    "NOISY-RX-MINUS-90")
-        elif np.isclose(angle, np.pi, atol=ANGLE_TOLERANCE):
-            return (np.array([[0, -1j],
-                              [-1j, 0]]),
-                    "NOISY-RX-PLUS-180")
-        elif np.isclose(angle, -np.pi, atol=ANGLE_TOLERANCE):
-            return (np.array([[0, 1j],
-                              [1j, 0]]),
-                    "NOISY-RX-MINUS-180")
-    elif gate_name == "CZ":
-        assert params == ()
-        return np.diag([1, 1, 1, -1]), "NOISY-CZ"
-    raise NoisyGateUndefined("Undefined gate and params: {}{}\n"
-                             "Please restrict yourself to I, RX(+/-pi), RX(+/-pi/2), CZ")
+NOISY_GATES = {
+    ("I", ()): (np.eye(2), "NOISY-I"),
+    ("RX", (np.pi / 2,)): (np.array([[1, -1j],
+                                     [-1j, 1]]) / np.sqrt(2),
+                           "NOISY-RX-PLUS-90"),
+    ("RX", (-np.pi / 2,)): (np.array([[1, 1j],
+                                      [1j, 1]]) / np.sqrt(2),
+                            "NOISY-RX-MINUS-90"),
+    ("RX", (np.pi,)): (np.array([[0, -1j],
+                                 [-1j, 0]]),
+                       "NOISY-RX-PLUS-180"),
+    ("RX", (-np.pi,)): (np.array([[0, 1j],
+                                  [1j, 0]]),
+                        "NOISY-RX-MINUS-180"),
+    ("CZ", ()): (np.diag([1, 1, 1, -1]), "NOISY-CZ"),
+}
 
 
 def _get_program_gates(prog):
@@ -397,15 +384,19 @@
         key = (g.name, tuple(g.params))
         if g.name in NO_NOISE:
             continue
-        matrix, _ = get_noisy_gate(g.name, g.params)
+        if key in NOISY_GATES:
+            matrix, _ = NOISY_GATES[key]
+            if len(targets) == 1:
+                noisy_I = noisy_identities_1q[targets[0]]
+            else:
+                if len(targets) != 2:
+                    raise ValueError("Noisy gates on more than 2Q not currently supported")
 
-        if len(targets) == 1:
-            noisy_I = noisy_identities_1q[targets[0]]
+                noisy_I = tensor_kraus_maps(noisy_identities_2q[targets[1]],
+                                            noisy_identities_2q[targets[0]])
         else:
-            if len(targets) != 2:
-                raise ValueError("Noisy gates on more than 2Q not currently supported")
-            noisy_I = tensor_kraus_maps(noisy_identities_2q[targets[1]],
-                                        noisy_identities_2q[targets[0]])
+            raise ValueError("Cannot create noisy version of {}. ".format(g) +
+                             "Please restrict yourself to CZ, RX(+/-pi/2), I, RZ(theta)")
         kraus_maps.append(KrausModel(g.name, tuple(g.params), targets,
                                      combine_kraus_maps(noisy_I, [matrix]),
                                      # FIXME (Nik): compute actual avg gate fidelity for this simple
@@ -441,13 +432,13 @@
 
         # obtain ideal gate matrix and new, noisy name by looking it up in the NOISY_GATES dict
         try:
-            ideal_gate, new_name = get_noisy_gate(k.gate, tuple(k.params))
+            ideal_gate, new_name = NOISY_GATES[k.gate, tuple(k.params)]
 
             # if ideal version of gate has not yet been DEFGATE'd, do this
             if new_name not in defgates:
                 p.defgate(new_name, ideal_gate)
                 defgates.add(new_name)
-        except NoisyGateUndefined:
+        except KeyError:
             print("WARNING: Could not find ideal gate definition for gate {}".format(k.gate),
                   file=sys.stderr)
             new_name = k.gate
@@ -475,10 +466,11 @@
     new_prog = _noise_model_program_header(noise_model)
     for i in prog:
         if isinstance(i, Gate):
-            try:
-                _, new_name = get_noisy_gate(i.name, tuple(i.params))
+            key = (i.name, tuple(i.params))
+            if key in NOISY_GATES:
+                _, new_name = NOISY_GATES[key]
                 new_prog += Gate(new_name, [], i.qubits)
-            except NoisyGateUndefined:
+            else:
                 new_prog += i
         else:
             new_prog += i
