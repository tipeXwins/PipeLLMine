20a21
> from math import ceil
74c75
< def _get_mode_order(num_of_values, modes, N):
---
> def _get_mode_order(num_of_values, modes, N, timebins):
89d89
<     mode_order = []
99,100c99,100
<         extended_modes = timebin_modes * (1 + num_of_values // len(timebin_modes))
<         all_modes.append(extended_modes[:num_of_values])
---
>         extended_modes = timebin_modes * ceil(1 + timebins // len(timebin_modes))
>         all_modes.append(extended_modes[:timebins])
102c102,103
<         mode_order = [i for j in zip(*all_modes) for i in j]
---
>     mode_order = [i for j in zip(*all_modes) for i in j]
>     mode_order *= ceil(1 + num_of_values / len(mode_order))
165c166
<     mode_order = _get_mode_order(num_of_values, modes, N)
---
>     mode_order = _get_mode_order(num_of_values, modes, N, timebins)
375c376
<         self._concurr_modes = sum(self.N)
---
>         self.concurr_modes = sum(self.N)
377c378
<         super().__init__(num_subsystems=self._concurr_modes, name=name)
---
>         super().__init__(num_subsystems=self.concurr_modes, name=name)
378a380
>         self.type = "tdm"
382,384c384,386
<         self._timebins = 0
<         self._spatial_modes = 0
<         self._measured_modes = set()
---
>         self.timebins = 0
>         self.spatial_modes = 0
>         self.measured_modes = []
392c394
<         self._num_added_subsystems = 0
---
>         self.num_added_subsystems = 0
400,419d401
<     @property
<     def measured_modes(self):
<         """The number of measured modes in the program returned as a list."""
<         return list(self._measured_modes)
< 
<     @property
<     def timebins(self):
<         """The number of timebins in the program."""
<         return self._timebins
< 
<     @property
<     def spatial_modes(self):
<         """The number of spatial modes in the program."""
<         return self._spatial_modes
< 
<     @property
<     def concurr_modes(self):
<         """The number of concurrent modes in the program."""
<         return self._concurr_modes
< 
451,453c433,434
<         if compiler != "TDM":
<             if compiler in alt_compilers or getattr(device, "default_compiler") in alt_compilers:
<                 return super().compile(device=device, compiler=compiler)
---
>         if compiler in alt_compilers or getattr(device, "default_compiler") in alt_compilers:
>             return super().compile(device=device, compiler=compiler)
559c540
<             self._timebins = len(self.tdm_params[0])
---
>             self.timebins = len(self.tdm_params[0])
562c543
<             self._spatial_modes = len(self.N)
---
>             self.spatial_modes = len(self.N)
575,578c556,559
<             if self._num_added_subsystems > 0:
<                 self._delete_subsystems(self.register[-self._num_added_subsystems :])
<                 self.init_num_subsystems -= self._num_added_subsystems
<                 self._num_added_subsystems = 0
---
>             if self.num_added_subsystems > 0:
>                 self._delete_subsystems(self.register[-self.num_added_subsystems :])
>                 self.init_num_subsystems -= self.num_added_subsystems
>                 self.num_added_subsystems = 0
598c579
<             self.circuit = self.unrolled_circuit
---
>             self.circuit = self.unrolled_circuit * shots
624c605
<             self.circuit = self.space_unrolled_circuit
---
>             self.circuit = self.space_unrolled_circuit * shots
627,631c608,610
<         self._num_added_subsystems = self._timebins - self.init_num_subsystems
<         if self._num_added_subsystems > 0:
<             self._add_subsystems(self._num_added_subsystems)
< 
<             self.init_num_subsystems += self._num_added_subsystems
---
>         self.num_added_subsystems = self.timebins - self.init_num_subsystems
>         if self.num_added_subsystems > 0:
>             self._add_subsystems(self.num_added_subsystems)
632a612
>             self.init_num_subsystems += self.num_added_subsystems
633a614
> 
671,672c652
<         for _ in range(shots):
<             previous_mode_index = dict()
---
>         previous_mode_index = dict()
673a654,658
>         for cmd in self.rolled_circuit:
>             previous_mode_index[cmd] = 0
>             if isinstance(cmd.op, ops.Measurement):
>                 self.measured_modes.append(cmd.reg[0].ind)
>         for i in range(self.timebins):
675,694c660,673
<                 previous_mode_index[cmd] = 0
<                 if isinstance(cmd.op, ops.Measurement):
<                     self._measured_modes.add(cmd.reg[0].ind)
< 
<             for i in range(self.timebins):
<                 for cmd in self.rolled_circuit:
<                     modes = get_modes(cmd, q)
<                     has_looped_back = any(m.ind < previous_mode_index[cmd] for m in modes)
<                     valid_application = not self._is_space_unrolled or not has_looped_back
<                     if valid_application:
<                         self.apply_op(cmd, modes, i)
<                         previous_mode_index[cmd] = min(m.ind for m in modes)
< 
<                 if self._is_space_unrolled:
<                     q = shift_by(q, 1)
<                 elif self.shift == "default":
<                     q_aux = list(q)
<                     for j, _ in enumerate(self.N):
<                         q_aux[sm[j]] = shift_by(q_aux[sm[j]], 1)
<                     q = tuple(q_aux)
---
>                 modes = get_modes(cmd, q)
>                 has_looped_back = any(m.ind < previous_mode_index[cmd] for m in modes)
>                 valid_application = not self._is_space_unrolled or not has_looped_back
>                 if valid_application:
>                     self.apply_op(cmd, modes, i)
>                     previous_mode_index[cmd] = min(m.ind for m in modes)
> 
>             if self._is_space_unrolled:
>                 q = shift_by(q, 1)
>             elif self.shift == "default":
>                 q_aux = list(q)
>                 for j, _ in enumerate(self.N):
>                     q_aux[sm[j]] = shift_by(q_aux[sm[j]], 1)
>                 q = tuple(q_aux)
696,697c675,676
<                 elif isinstance(self.shift, int):
<                     q = shift_by(q, self.shift)  # shift at end of each time bin
---
>             elif isinstance(self.shift, int):
>                 q = shift_by(q, self.shift)  # shift at end of each time bin
703a683
>         self.circuit = self.circuit * shots
