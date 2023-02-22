--- strawberryfields/strawberryfields#611/after/tdmprogram.py	2022-01-10 16:02:54.000000000 +0000
+++ strawberryfields/strawberryfields#611/before/tdmprogram.py	2022-01-10 16:02:54.000000000 +0000
@@ -18,6 +18,7 @@
 # pylint: disable=too-many-instance-attributes,attribute-defined-outside-init
 
 from operator import itemgetter
+from math import ceil
 from collections.abc import Iterable
 
 import numpy as np
@@ -71,7 +72,7 @@
         raise ValueError("Gate-parameter lists must be of equal length.")
 
 
-def _get_mode_order(num_of_values, modes, N):
+def _get_mode_order(num_of_values, modes, N, timebins):
     """Get the order in which the modes were measured.
 
     The mode order is determined by the circuit and the mode-shifting occurring in
@@ -86,7 +87,6 @@
 
     """
     all_modes = []
-    mode_order = []
     for i, _ in enumerate(N):
         timebin_modes = list(range(sum(N[:i]), sum(N[: i + 1])))
         # shift the timebin_modes if the measured mode isn't the first in the
@@ -96,10 +96,11 @@
 
         # extend the modes by duplicating the list so that the measured mode
         # orders in all bands have the same length
-        extended_modes = timebin_modes * (1 + num_of_values // len(timebin_modes))
-        all_modes.append(extended_modes[:num_of_values])
+        extended_modes = timebin_modes * ceil(1 + timebins // len(timebin_modes))
+        all_modes.append(extended_modes[:timebins])
 
-        mode_order = [i for j in zip(*all_modes) for i in j]
+    mode_order = [i for j in zip(*all_modes) for i in j]
+    mode_order *= ceil(1 + num_of_values / len(mode_order))
     return mode_order[:num_of_values]
 
 
@@ -162,7 +163,7 @@
     """
     # calculate the total number of samples and the order in which they were measured
     num_of_values = len([i for j in all_samples.values() for i in j])
-    mode_order = _get_mode_order(num_of_values, modes, N)
+    mode_order = _get_mode_order(num_of_values, modes, N, timebins)
     idx_tracker = {i: 0 for i in mode_order}
 
     # iterate backwards through all_samples and add them into the correct mode
@@ -372,16 +373,17 @@
             self.N = [N]
         else:
             self.N = N
-        self._concurr_modes = sum(self.N)
+        self.concurr_modes = sum(self.N)
 
-        super().__init__(num_subsystems=self._concurr_modes, name=name)
+        super().__init__(num_subsystems=self.concurr_modes, name=name)
 
+        self.type = "tdm"
         self.is_unrolled = False
         self._is_space_unrolled = False
 
-        self._timebins = 0
-        self._spatial_modes = 0
-        self._measured_modes = set()
+        self.timebins = 0
+        self.spatial_modes = 0
+        self.measured_modes = []
         self.rolled_circuit = None
         # `unrolled_circuit` contains the unrolled single-shot circuit, reusing previously measured
         # modes (doesn't work with Fock measurements)
@@ -389,7 +391,7 @@
         # `space_unrolled_circuit` contains the space-unrolled single-shot circuit, instead adding
         # new modes for each new measurement (works with Fock measurements)
         self.space_unrolled_circuit = None
-        self._num_added_subsystems = 0
+        self.num_added_subsystems = 0
         self.run_options = {}
         """dict[str, Any]: dictionary of default run options, to be passed to the engine upon
         execution of the program. Note that if the ``run_options`` dictionary is passed
@@ -397,26 +399,6 @@
         here.
         """
 
-    @property
-    def measured_modes(self):
-        """The number of measured modes in the program returned as a list."""
-        return list(self._measured_modes)
-
-    @property
-    def timebins(self):
-        """The number of timebins in the program."""
-        return self._timebins
-
-    @property
-    def spatial_modes(self):
-        """The number of spatial modes in the program."""
-        return self._spatial_modes
-
-    @property
-    def concurr_modes(self):
-        """The number of concurrent modes in the program."""
-        return self._concurr_modes
-
     # pylint: disable=arguments-differ, invalid-overridden-method
     def context(self, *args, shift="default"):
         input_check(args)
@@ -448,9 +430,8 @@
             Program: compiled program
         """
         alt_compilers = ("gaussian", "passive")
-        if compiler != "TDM":
-            if compiler in alt_compilers or getattr(device, "default_compiler") in alt_compilers:
-                return super().compile(device=device, compiler=compiler)
+        if compiler in alt_compilers or getattr(device, "default_compiler") in alt_compilers:
+            return super().compile(device=device, compiler=compiler)
 
         if device is not None:
             device_layout = bb.loads(device.layout)
@@ -556,10 +537,10 @@
         super().__exit__(ex_type, ex_value, ex_tb)
 
         if ex_type is None:
-            self._timebins = len(self.tdm_params[0])
+            self.timebins = len(self.tdm_params[0])
             self.rolled_circuit = self.circuit.copy()
 
-            self._spatial_modes = len(self.N)
+            self.spatial_modes = len(self.N)
 
     @property
     def parameters(self):
@@ -572,10 +553,10 @@
         self.is_unrolled = False
         self.circuit = self.rolled_circuit
         if self._is_space_unrolled:
-            if self._num_added_subsystems > 0:
-                self._delete_subsystems(self.register[-self._num_added_subsystems :])
-                self.init_num_subsystems -= self._num_added_subsystems
-                self._num_added_subsystems = 0
+            if self.num_added_subsystems > 0:
+                self._delete_subsystems(self.register[-self.num_added_subsystems :])
+                self.init_num_subsystems -= self.num_added_subsystems
+                self.num_added_subsystems = 0
 
             self._is_space_unrolled = False
         return self
@@ -595,7 +576,7 @@
         """
         self.is_unrolled = True
         if self.unrolled_circuit is not None:
-            self.circuit = self.unrolled_circuit
+            self.circuit = self.unrolled_circuit * shots
             return self
 
         if self._is_space_unrolled:
@@ -621,16 +602,16 @@
         """
         self.is_unrolled = True
         if self.space_unrolled_circuit is not None:
-            self.circuit = self.space_unrolled_circuit
+            self.circuit = self.space_unrolled_circuit * shots
             return self
 
-        self._num_added_subsystems = self._timebins - self.init_num_subsystems
-        if self._num_added_subsystems > 0:
-            self._add_subsystems(self._num_added_subsystems)
-
-            self.init_num_subsystems += self._num_added_subsystems
+        self.num_added_subsystems = self.timebins - self.init_num_subsystems
+        if self.num_added_subsystems > 0:
+            self._add_subsystems(self.num_added_subsystems)
 
+            self.init_num_subsystems += self.num_added_subsystems
         self._is_space_unrolled = True
+
         return self._unroll_program(shots)
 
     def _unroll_program(self, shots):
@@ -668,39 +649,38 @@
         # q[sm[2]] as concurrent modes of spatial mode C
         # q[sm[3]] as concurrent modes of spatial mode D.
 
-        for _ in range(shots):
-            previous_mode_index = dict()
+        previous_mode_index = dict()
 
+        for cmd in self.rolled_circuit:
+            previous_mode_index[cmd] = 0
+            if isinstance(cmd.op, ops.Measurement):
+                self.measured_modes.append(cmd.reg[0].ind)
+        for i in range(self.timebins):
             for cmd in self.rolled_circuit:
-                previous_mode_index[cmd] = 0
-                if isinstance(cmd.op, ops.Measurement):
-                    self._measured_modes.add(cmd.reg[0].ind)
-
-            for i in range(self.timebins):
-                for cmd in self.rolled_circuit:
-                    modes = get_modes(cmd, q)
-                    has_looped_back = any(m.ind < previous_mode_index[cmd] for m in modes)
-                    valid_application = not self._is_space_unrolled or not has_looped_back
-                    if valid_application:
-                        self.apply_op(cmd, modes, i)
-                        previous_mode_index[cmd] = min(m.ind for m in modes)
-
-                if self._is_space_unrolled:
-                    q = shift_by(q, 1)
-                elif self.shift == "default":
-                    q_aux = list(q)
-                    for j, _ in enumerate(self.N):
-                        q_aux[sm[j]] = shift_by(q_aux[sm[j]], 1)
-                    q = tuple(q_aux)
+                modes = get_modes(cmd, q)
+                has_looped_back = any(m.ind < previous_mode_index[cmd] for m in modes)
+                valid_application = not self._is_space_unrolled or not has_looped_back
+                if valid_application:
+                    self.apply_op(cmd, modes, i)
+                    previous_mode_index[cmd] = min(m.ind for m in modes)
+
+            if self._is_space_unrolled:
+                q = shift_by(q, 1)
+            elif self.shift == "default":
+                q_aux = list(q)
+                for j, _ in enumerate(self.N):
+                    q_aux[sm[j]] = shift_by(q_aux[sm[j]], 1)
+                q = tuple(q_aux)
 
-                elif isinstance(self.shift, int):
-                    q = shift_by(q, self.shift)  # shift at end of each time bin
+            elif isinstance(self.shift, int):
+                q = shift_by(q, self.shift)  # shift at end of each time bin
 
         # Unrolling the circuit for the first time: storing a copy of the unrolled circuit
         if self._is_space_unrolled:
             self.space_unrolled_circuit = self.circuit.copy()
         else:
             self.unrolled_circuit = self.circuit.copy()
+        self.circuit = self.circuit * shots
 
         return self
 
