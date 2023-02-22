--- pennylane/pennylane#1426/after/torch.py	2022-01-10 16:02:54.000000000 +0000
+++ pennylane/pennylane#1426/before/torch.py	2022-01-10 16:02:54.000000000 +0000
@@ -184,14 +184,7 @@
     def backward(ctx, dy):  # pragma: no cover
         """Implements the backwards pass QNode vector-Jacobian product"""
         ctx.dy = dy
-        dyv = dy.view(1, -1)
-        jac_res = ctx.jacobian.apply(ctx, *ctx.saved_tensors)
-        if dyv.is_cuda or jac_res.is_cuda:
-            if not dyv.is_cuda:
-                dyv = torch.as_tensor(dyv, device=jac_res.get_device())
-            if not jac_res.is_cuda:
-                jac_res = torch.as_tensor(jac_res, device=dyv.get_device())
-        vjp = dyv @ jac_res
+        vjp = dy.view(1, -1) @ ctx.jacobian.apply(ctx, *ctx.saved_tensors)
         vjp = torch.unbind(vjp.view(-1))
         return (None,) + tuple(vjp)
 
