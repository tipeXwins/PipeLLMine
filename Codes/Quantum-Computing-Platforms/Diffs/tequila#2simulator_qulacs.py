149,152c149
<             for key in gate.target:
<                 if key in self.measurements:
<                     raise TequilaQulacsException("Measurement on qubit {} was given twice".format(key))
<             self.measurements += gate.target
---
>             raise TequilaQulacsException("Measurement on qubit {} was given twice".format(key))
