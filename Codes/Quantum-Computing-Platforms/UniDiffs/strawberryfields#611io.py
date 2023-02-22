--- strawberryfields/strawberryfields#611/after/io.py	2022-01-10 16:02:54.000000000 +0000
+++ strawberryfields/strawberryfields#611/before/io.py	2022-01-10 16:02:54.000000000 +0000
@@ -24,7 +24,6 @@
 
 import blackbird
 import strawberryfields.program as sfp
-from strawberryfields.tdm.tdmprogram import TDMProgram
 import strawberryfields.parameters as sfpar
 from . import ops
 
@@ -94,7 +93,7 @@
                 op["args"].append(a)
 
 
-        if isinstance(prog, TDMProgram):
+        if prog.type == "tdm":
             for p in prog.loop_vars:
                 for i, ar in enumerate(op["args"]):
                     if str(p) == str(ar):
@@ -105,7 +104,7 @@
 
         bb._operations.append(op)
     # add the specific "tdm" metadata to the Blackbird program
-    if isinstance(prog, TDMProgram):
+    if prog.type == "tdm":
         bb._type["name"] = "tdm"
         bb._type["options"].update(
             {
@@ -184,6 +183,7 @@
 
 # pylint:disable=too-many-branches
 def _to_tdm_program(bb):
+    from strawberryfields.tdm.tdmprogram import TDMProgram
     prog = TDMProgram(max(bb.modes) + 1, name=bb.name)
 
     def is_free_param(param):
@@ -294,7 +294,7 @@
     """
     code_seq = ["import strawberryfields as sf", "from strawberryfields import ops\n"]
 
-    if isinstance(prog, TDMProgram):
+    if prog.type == "tdm":
         code_seq.append(f"prog = sf.TDMProgram(N={prog.N})")
     else:
         code_seq.append(f"prog = sf.Program({prog.num_subsystems})")
@@ -315,7 +315,7 @@
             else:
                 code_seq.append(f'eng = sf.Engine("{eng.backend_name}")')
 
-    if isinstance(prog, TDMProgram):
+    if prog.type == "tdm":
         # if the context arrays contain pi-values, factor out multiples of np.pi
         tdm_params = [f"[{_factor_out_pi(par)}]" for par in prog.tdm_params]
         code_seq.append("\nwith prog.context(" + ", ".join(tdm_params) + ") as (p, q):")
@@ -325,7 +325,7 @@
     # add the operations, and replace any free parameters with e.g. `p[0]`, `p[1]`
     for cmd in prog.circuit:
         name = cmd.op.__class__.__name__
-        if isinstance(prog, TDMProgram):
+        if prog.type == "tdm":
             format_dict = {k: f"p[{k[1:]}]" for k in prog.parameters.keys()}
             params_str = _factor_out_pi(cmd.op.p).format(**format_dict)
         else:
