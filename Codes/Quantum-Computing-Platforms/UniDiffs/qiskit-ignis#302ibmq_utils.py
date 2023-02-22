--- qiskit-ignis/qiskit-ignis#302/after/ibmq_utils.py	2022-01-10 16:02:54.000000000 +0000
+++ qiskit-ignis/qiskit-ignis#302/before/ibmq_utils.py	2022-01-10 16:02:54.000000000 +0000
@@ -140,9 +140,9 @@
         else:
             _u2_group = (drive_ch, )
 
-        u2_fc1s = [parametrized_fc('P1', -np.pi/2, ch, 0)
+        u2_fc1s = [parametrized_fc('P1', np.pi/2, ch, 0)
                    for ch in _u2_group]
-        u2_fc2s = [parametrized_fc('P0', np.pi/2, ch, pulse_dur)
+        u2_fc2s = [parametrized_fc('P0', -np.pi/2, ch, pulse_dur)
                    for ch in _u2_group]
 
         # find channel dependency for u2
