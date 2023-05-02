215c215
<             jacobian = torch.as_tensor(jacobian, dtype=grad_output.dtype).to(grad_output)
---
>             jacobian = torch.as_tensor(jacobian, dtype=grad_output.dtype)
