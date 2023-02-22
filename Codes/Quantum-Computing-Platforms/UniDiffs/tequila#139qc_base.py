--- tequila/tequila#139/after/qc_base.py	2022-01-10 16:02:54.000000000 +0000
+++ tequila/tequila#139/before/qc_base.py	2022-01-10 16:02:54.000000000 +0000
@@ -1300,27 +1300,27 @@
                         partner = None
                     else:
                         spin_indices.append([2 * key[0] + 1, 2 * key[1] + 1, 2 * key[2], 2 * key[3]])
-                        #spin_indices.append([2 * key[0], 2 * key[1], 2 * key[2] + 1, 2 * key[3] + 1])
+                        spin_indices.append([2 * key[0], 2 * key[1], 2 * key[2] + 1, 2 * key[3] + 1])
                         if key[0] != key[2] and key[1] != key[3]:
                             spin_indices.append([2 * key[0], 2 * key[1], 2 * key[2], 2 * key[3]])
-                            #spin_indices.append([2 * key[0] + 1, 2 * key[1] + 1, 2 * key[2] + 1, 2 * key[3] + 1])
+                            spin_indices.append([2 * key[0] + 1, 2 * key[1] + 1, 2 * key[2] + 1, 2 * key[3] + 1])
                         partner = tuple([key[2], key[1], key[0], key[3]])  # taibj -> tbiaj
                     for idx in spin_indices:
                         idx = [(idx[2 * i], idx[2 * i + 1]) for i in range(len(idx) // 2)]
                         indices.append(idx)
 
                     if parametrized:
-                        variables.append(2.0*Variable(name=key))  # abab
-                        #variables.append(Variable(name=key))  # baba
+                        variables.append(Variable(name=key))  # abab
+                        variables.append(Variable(name=key))  # baba
                         if partner is not None and key[0] != key[1] and key[2] != key[3]:
-                            variables.append(2.0*(Variable(name=key) - Variable(partner))) # aaaa
-                            #variables.append(Variable(name=key) - Variable(partner))  # bbbb
+                            variables.append(Variable(name=key) - Variable(partner))  # aaaa
+                            variables.append(Variable(name=key) - Variable(partner))  # bbbb
                     else:
-                        variables.append(2.0*t)
-                        #variables.append(t)
+                        variables.append(t)
+                        variables.append(t)
                         if partner is not None and key[0] != key[1] and key[2] != key[3]:
-                            variables.append(2.0*(t - amplitudes[partner]))
-                            #variables.append(t - amplitudes[partner])
+                            variables.append(t - amplitudes[partner])
+                            variables.append(t - amplitudes[partner])
                 else:
                     indices.append(spin_indices)
                     if parametrized:
