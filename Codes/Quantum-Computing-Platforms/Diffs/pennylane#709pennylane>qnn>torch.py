333c333
<                 w = self.qnode_weights[arg].to(x)
---
>                 w = self.qnode_weights[arg]
352,355c352
<         kwargs = {
<             **{self.input_arg: x},
<             **{arg: weight.to(x) for arg, weight in self.qnode_weights.items()},
<         }
---
>         kwargs = {**{self.input_arg: x}, **self.qnode_weights}
