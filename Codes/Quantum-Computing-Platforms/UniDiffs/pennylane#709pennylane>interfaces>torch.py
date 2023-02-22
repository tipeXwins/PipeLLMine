--- pennylane/pennylane#709/after/pennylane>interfaces>torch.py	2022-01-10 16:02:54.000000000 +0000
+++ pennylane/pennylane#709/before/pennylane>interfaces>torch.py	2022-01-10 16:02:54.000000000 +0000
@@ -212,7 +212,7 @@
 
             # evaluate the Jacobian matrix of the QNode
             jacobian = qnode.jacobian(ctx.args, ctx.kwargs)
-            jacobian = torch.as_tensor(jacobian, dtype=grad_output.dtype).to(grad_output)
+            jacobian = torch.as_tensor(jacobian, dtype=grad_output.dtype)
 
             vjp = torch.transpose(grad_output.view(-1, 1), 0, 1) @ jacobian
             vjp = vjp.flatten()
