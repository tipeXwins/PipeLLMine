--- qiskit-terra/qiskit-terra#3900/after/assemble_schedules.py	2022-01-10 16:02:54.000000000 +0000
+++ qiskit-terra/qiskit-terra#3900/before/assemble_schedules.py	2022-01-10 16:02:54.000000000 +0000
@@ -99,11 +99,11 @@
     user_pulselib = {}
     experiments = []
     for idx, schedule in enumerate(schedules):
-        qobj_instructions, max_memory_slot = _assemble_instructions(
+        qobj_instructions, user_pulses, max_memory_slot = _assemble_instructions(
             schedule,
             instruction_converter,
-            run_config,
-            user_pulselib)
+            run_config)
+        user_pulselib.update(user_pulses)
 
         # TODO: add other experimental header items (see circuit assembler)
         qobj_experiment_header = QobjExperimentHeader(
@@ -144,9 +144,8 @@
 def _assemble_instructions(
         schedule: Schedule,
         instruction_converter: InstructionToQobjConverter,
-        run_config: RunConfig,
-        user_pulselib: Dict[str, Command]
-) -> Tuple[List[PulseQobjInstruction], int]:
+        run_config: RunConfig
+) -> Tuple[List[PulseQobjInstruction], Dict[str, Command], int]:
     """Assembles the instructions in a schedule into a list of PulseQobjInstructions and returns
     related metadata that will be assembled into the Qobj configuration.
 
@@ -155,7 +154,6 @@
         instruction_converter: A converter instance which can convert PulseInstructions to
                                PulseQobjInstructions.
         run_config: Configuration of the runtime environment.
-        user_pulselib: User pulse library from previous schedule.
 
     Returns:
         A list of converted instructions, the user pulse library dictionary (from pulse name to
@@ -163,6 +161,7 @@
     """
     max_memory_slot = 0
     qobj_instructions = []
+    user_pulselib = {}
 
     acquire_instruction_map = defaultdict(list)
     for time, instruction in schedule.instructions:
@@ -210,7 +209,7 @@
                     time, instructions[0],
                     qubits=qubits, memory_slot=mem_slots, register_slot=reg_slots))
 
-    return qobj_instructions, max_memory_slot
+    return qobj_instructions, user_pulselib, max_memory_slot
 
 
 def _validate_meas_map(instruction_map: Dict[Tuple[int, Acquire], List[AcquireInstruction]],
