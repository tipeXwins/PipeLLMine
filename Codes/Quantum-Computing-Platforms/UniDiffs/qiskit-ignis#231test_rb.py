--- qiskit-ignis/qiskit-ignis#231/after/test_rb.py	2022-01-10 16:02:54.000000000 +0000
+++ qiskit-ignis/qiskit-ignis#231/before/test_rb.py	2022-01-10 16:02:54.000000000 +0000
@@ -171,7 +171,7 @@
                             # correct sub-sequences, as specified by vec_len
                             # and rb_opts
                             self.assertTrue(
-                                all(x.index in rb_opts['rb_pattern'][pat_index]
+                                all(x[1] in rb_opts['rb_pattern'][pat_index]
                                     for x in ops[op_index][1]),
                                 "Error: operation acts on incorrect qubits")
                             op_index += 1
@@ -227,7 +227,7 @@
                     while original_ops[original_op_index][0].name != 'barrier':
                         gate = original_ops[original_op_index][0].name
                         for x in original_ops[original_op_index][1]:
-                            gate += ' ' + str(x.index)
+                            gate += ' ' + str(x[1])
                         original_gate_list.append(gate)
                         original_op_index += 1
                     original_op_index += 1
@@ -238,7 +238,7 @@
                             != 'barrier':
                         gate = interleaved_ops[interleaved_op_index][0].name
                         for x in interleaved_ops[interleaved_op_index][1]:
-                            gate += ' ' + str(x.index)
+                            gate += ' ' + str(x[1])
                         compared_gate_list.append(gate)
                         interleaved_op_index += 1
                     interleaved_op_index += 1
@@ -258,7 +258,7 @@
                             'barrier':
                         gate = interleaved_ops[interleaved_op_index][0].name
                         for x in interleaved_ops[interleaved_op_index][1]:
-                            gate += ' ' + str(x.index)
+                            gate += ' ' + str(x[1])
                         interleaved_gatelist.append(gate)
                         interleaved_op_index += 1
                     interleaved_op_index += 1
