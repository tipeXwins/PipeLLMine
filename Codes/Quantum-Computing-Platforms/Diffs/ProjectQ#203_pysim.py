354d353
<         mask = self._get_control_mask(ctrlids)
363c362
<                     self._apply_term(t, ids)
---
>                     self._apply_term(t, ids, ctrlids)
369,371c368
<                 for i in range(len(update)):
<                     if (i & mask) == mask:
<                         output_state[i] += update[i]
---
>                 output_state += update
374,376c371
<             for i in range(len(update)):
<                 if (i & mask) == mask:
<                     output_state[i] *= correction
---
>             output_state *= correction
