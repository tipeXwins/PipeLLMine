--- qiskit-terra/qiskit-terra#4974/after/transforms.py	2022-01-10 16:02:54.000000000 +0000
+++ qiskit-terra/qiskit-terra#4974/before/transforms.py	2022-01-10 16:02:54.000000000 +0000
@@ -215,15 +215,15 @@
                                                      chans.AcquireChannel(i),
                                                      mem_slot=chans.MemorySlot(i),
                                                      kernel=inst.kernel,
-                                                     discriminator=inst.discriminator)
+                                                     discriminator=inst.discriminator) << time
                 if time not in acquire_map:
-                    new_schedule.insert(time, explicit_inst, inplace=True)
+                    new_schedule |= explicit_inst
                     acquire_map = {time: {i}}
                 elif i not in acquire_map[time]:
-                    new_schedule.insert(time, explicit_inst, inplace=True)
+                    new_schedule |= explicit_inst
                     acquire_map[time].add(i)
         else:
-            new_schedule.insert(time, inst, inplace=True)
+            new_schedule |= inst << time
 
     return new_schedule
 
@@ -300,16 +300,13 @@
                 if inst.pulse in existing_pulses:
                     idx = existing_pulses.index(inst.pulse)
                     identical_pulse = existing_pulses[idx]
-                    new_schedule.insert(time,
-                                        instructions.Play(identical_pulse,
-                                                          inst.channel,
-                                                          inst.name),
-                                        inplace=True)
+                    new_schedule |= instructions.Play(
+                        identical_pulse, inst.channel, inst.name) << time
                 else:
                     existing_pulses.append(inst.pulse)
-                    new_schedule.insert(time, inst, inplace=True)
+                    new_schedule |= inst << time
             else:
-                new_schedule.insert(time, inst, inplace=True)
+                new_schedule |= inst << time
 
         new_schedules.append(new_schedule)
 
