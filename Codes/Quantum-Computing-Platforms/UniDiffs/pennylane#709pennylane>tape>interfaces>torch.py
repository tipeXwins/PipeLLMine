--- pennylane/pennylane#709/after/pennylane>tape>interfaces>torch.py	2022-01-10 16:02:54.000000000 +0000
+++ pennylane/pennylane#709/before/pennylane>tape>interfaces>torch.py	2022-01-10 16:02:54.000000000 +0000
@@ -73,7 +73,7 @@
         jacobian = tape.jacobian(device, params=ctx.args, **tape.jacobian_options)
         tape.set_parameters(ctx.all_params, trainable_only=False)
 
-        jacobian = torch.as_tensor(jacobian, dtype=grad_output.dtype).to(grad_output)
+        jacobian = torch.as_tensor(jacobian, dtype=grad_output.dtype)
 
         vjp = grad_output.view(1, -1) @ jacobian
         grad_input_list = torch.unbind(vjp.flatten())
