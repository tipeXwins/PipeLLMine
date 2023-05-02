25c25
< from cirq._compat import proper_repr, deprecated_class
---
> from cirq._compat import deprecated, proper_repr
326,328c326
< @deprecated_class(deadline='v0.11',
<                   fix='Use cirq.Result instead.',
<                   name="cirq.TrialResult")
---
> @deprecated(deadline='v0.11', fix='Use cirq.Result instead.')
