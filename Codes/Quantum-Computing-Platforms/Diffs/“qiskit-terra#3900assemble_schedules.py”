102c102
<         qobj_instructions, max_memory_slot = _assemble_instructions(
---
>         qobj_instructions, user_pulses, max_memory_slot = _assemble_instructions(
105,106c105,106
<             run_config,
<             user_pulselib)
---
>             run_config)
>         user_pulselib.update(user_pulses)
147,149c147,148
<         run_config: RunConfig,
<         user_pulselib: Dict[str, Command]
< ) -> Tuple[List[PulseQobjInstruction], int]:
---
>         run_config: RunConfig
> ) -> Tuple[List[PulseQobjInstruction], Dict[str, Command], int]:
158d156
<         user_pulselib: User pulse library from previous schedule.
165a164
>     user_pulselib = {}
213c212
<     return qobj_instructions, max_memory_slot
---
>     return qobj_instructions, user_pulselib, max_memory_slot
