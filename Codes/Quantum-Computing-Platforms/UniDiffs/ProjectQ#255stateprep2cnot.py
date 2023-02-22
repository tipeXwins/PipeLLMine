--- ProjectQ/ProjectQ#255/after/stateprep2cnot.py	2022-01-10 16:02:54.000000000 +0000
+++ ProjectQ/ProjectQ#255/before/stateprep2cnot.py	2022-01-10 16:02:54.000000000 +0000
@@ -66,11 +66,7 @@
                 for block in range(2**(len(qureg)-target_qubit-1)):
                     a0 = abs_of_blocks[2*block]
                     a1 = abs_of_blocks[2*block+1]
-                    if a0 == 0 and a1 == 0:
-                        angles.append(0)
-                    else:
-                        angles.append(
-                            -2. * math.acos(a0 / math.sqrt(a0**2 + a1**2)))
+                    angles.append(-2. * math.acos(a0/math.sqrt(a0**2 + a1**2)))
                     abs_of_next_blocks.append(math.sqrt(a0**2 + a1**2))
                 UniformlyControlledRy(angles) | (qureg[(target_qubit+1):],
                                                  qureg[target_qubit])
