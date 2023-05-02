451,456d450
<             assert setting.in_operator.coefficient == 1, 'in_operator should specify a state and ' \
<                                                          'therefore cannot have a coefficient'
<             coeff = complex(setting.out_operator.coefficient)
<             if not np.isclose(coeff.imag, 0):
<                 raise ValueError(f"{setting}'s out_operator has a complex coefficient.")
<             coeff = coeff.real
461c455
<                     expectation=coeff,
---
>                     expectation=1.0,
464a459,464
>             assert setting.in_operator.coefficient == 1, 'in_operator should specify a state and ' \
>                                                          'therefore cannot have a coefficient'
>             coeff = complex(setting.out_operator.coefficient)
>             if not np.isclose(coeff.imag, 0):
>                 raise ValueError(f"{setting}'s out_operator has a complex coefficient.")
>             coeff = coeff.real
