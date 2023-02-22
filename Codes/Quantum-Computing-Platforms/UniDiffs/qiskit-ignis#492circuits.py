--- qiskit-ignis/qiskit-ignis#492/after/circuits.py	2022-01-10 16:02:54.000000000 +0000
+++ qiskit-ignis/qiskit-ignis#492/before/circuits.py	2022-01-10 16:02:54.000000000 +0000
@@ -440,8 +440,6 @@
             for (rb_pattern_index, rb_q_num) in enumerate(pattern_sizes):
 
                 for _ in range(length_multiplier[rb_pattern_index]):
-                    if rand_seed:
-                        rand_seed += (seed + 1)
                     new_elmnt = rb_group.random(rb_q_num, rand_seed)
                     Elmnts[rb_pattern_index] = rb_group.compose(
                         Elmnts[rb_pattern_index], new_elmnt)
