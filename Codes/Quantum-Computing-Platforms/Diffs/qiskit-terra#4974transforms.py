218c218
<                                                      discriminator=inst.discriminator)
---
>                                                      discriminator=inst.discriminator) << time
220c220
<                     new_schedule.insert(time, explicit_inst, inplace=True)
---
>                     new_schedule |= explicit_inst
223c223
<                     new_schedule.insert(time, explicit_inst, inplace=True)
---
>                     new_schedule |= explicit_inst
226c226
<             new_schedule.insert(time, inst, inplace=True)
---
>             new_schedule |= inst << time
303,307c303,304
<                     new_schedule.insert(time,
<                                         instructions.Play(identical_pulse,
<                                                           inst.channel,
<                                                           inst.name),
<                                         inplace=True)
---
>                     new_schedule |= instructions.Play(
>                         identical_pulse, inst.channel, inst.name) << time
310c307
<                     new_schedule.insert(time, inst, inplace=True)
---
>                     new_schedule |= inst << time
312c309
<                 new_schedule.insert(time, inst, inplace=True)
---
>                 new_schedule |= inst << time
