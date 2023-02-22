--- pennylane/pennylane#481_B/after/_qubit_device.py	2022-01-10 16:02:54.000000000 +0000
+++ pennylane/pennylane#481_B/before/_qubit_device.py	2022-01-10 16:02:54.000000000 +0000
@@ -19,7 +19,6 @@
 # e.g. instead of expval(self, observable, wires, par) have expval(self, observable)
 # pylint: disable=arguments-differ, abstract-method, no-value-for-parameter,too-many-instance-attributes
 import abc
-import itertools
 
 import numpy as np
 
@@ -291,7 +290,7 @@
         """
         powers_of_two = 1 << np.arange(number_of_states)
         states_sampled_base_ten = samples[:, None] & powers_of_two
-        return (states_sampled_base_ten > 0).astype(int)[:, ::-1]
+        return (states_sampled_base_ten > 0).astype(int)
 
     @property
     def state(self):
@@ -338,15 +337,11 @@
         Returns:
             array[float]: array of the resulting marginal probabilities.
         """
-        if wires is None:
-            return prob
+        wires = list(wires or range(self.num_wires))
         wires = np.hstack(wires)
         inactive_wires = list(set(range(self.num_wires)) - set(wires))
         prob = prob.reshape([2] * self.num_wires)
-        prob = np.apply_over_axes(np.sum, prob, inactive_wires).flatten()
-        basis_states = np.array(list(itertools.product([0, 1], repeat=len(wires))))
-        perm = np.ravel_multi_index(basis_states[:, np.argsort(np.argsort(wires))].T, [2] * len(wires))
-        return prob[perm]
+        return np.apply_over_axes(np.sum, prob, inactive_wires).flatten()
 
     def expval(self, observable):
         wires = observable.wires
