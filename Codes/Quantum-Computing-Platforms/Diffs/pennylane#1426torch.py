187,194c187
<         dyv = dy.view(1, -1)
<         jac_res = ctx.jacobian.apply(ctx, *ctx.saved_tensors)
<         if dyv.is_cuda or jac_res.is_cuda:
<             if not dyv.is_cuda:
<                 dyv = torch.as_tensor(dyv, device=jac_res.get_device())
<             if not jac_res.is_cuda:
<                 jac_res = torch.as_tensor(jac_res, device=dyv.get_device())
<         vjp = dyv @ jac_res
---
>         vjp = dy.view(1, -1) @ ctx.jacobian.apply(ctx, *ctx.saved_tensors)
