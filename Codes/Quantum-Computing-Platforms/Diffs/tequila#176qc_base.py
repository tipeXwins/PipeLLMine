146,147c146
<         lines = [l for l in geometry.split("\n") if l]
<         for line in lines:
---
>         for line in geometry.split('\n'):
149,150c148
<             if len(words) < 4:
<                 words += [0.0] * (4 - len(words))
---
>             if len(words) != 4:  break
