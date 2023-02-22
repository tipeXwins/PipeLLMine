--- ProjectQ/ProjectQ#203/after/_pysim.py	2022-01-10 16:02:54.000000000 +0000
+++ ProjectQ/ProjectQ#203/before/_pysim.py	2022-01-10 16:02:54.000000000 +0000
@@ -351,7 +351,6 @@
         s = int(op_nrm + 1.)
         correction = _np.exp(-1j * time * tr / float(s))
         output_state = _np.copy(self._state)
-        mask = self._get_control_mask(ctrlids)
         for i in range(s):
             j = 0
             nrm_change = 1.
@@ -360,20 +359,16 @@
                 current_state = _np.copy(self._state)
                 update = 0j
                 for t, c in terms_dict:
-                    self._apply_term(t, ids)
+                    self._apply_term(t, ids, ctrlids)
                     self._state *= c
                     update += self._state
                     self._state = _np.copy(current_state)
                 update *= coeff
                 self._state = update
-                for i in range(len(update)):
-                    if (i & mask) == mask:
-                        output_state[i] += update[i]
+                output_state += update
                 nrm_change = _np.linalg.norm(update)
                 j += 1
-            for i in range(len(update)):
-                if (i & mask) == mask:
-                    output_state[i] *= correction
+            output_state *= correction
             self._state = _np.copy(output_state)
 
     def apply_controlled_gate(self, m, ids, ctrlids):
