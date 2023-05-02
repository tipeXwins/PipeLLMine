175c175,177
<             exponent = str(abs(self.exponent_pos))
---
>             exponent = str(abs(self.exponent_pos * 2))
>             if abs(self.exponent_relative) == 1:
>                 exponent = ''
