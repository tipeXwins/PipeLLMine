299,327c299,314
< ANGLE_TOLERANCE = 1e-10
< class NoisyGateUndefined(Exception):
<     params = tuple(params)
<     if gate_name == "I":
<         assert params == ()
<         return np.eye(2), "NOISY-I"
<     if gate_name == "RX":
<         angle, = params
<         if np.isclose(angle, np.pi / 2, atol=ANGLE_TOLERANCE):
<             return (np.array([[1, -1j],
<                               [-1j, 1]]) / np.sqrt(2),
<                     "NOISY-RX-PLUS-90")
<         elif np.isclose(angle, -np.pi / 2, atol=ANGLE_TOLERANCE):
<             return (np.array([[1, 1j],
<                               [1j, 1]]) / np.sqrt(2),
<                     "NOISY-RX-MINUS-90")
<         elif np.isclose(angle, np.pi, atol=ANGLE_TOLERANCE):
<             return (np.array([[0, -1j],
<                               [-1j, 0]]),
<                     "NOISY-RX-PLUS-180")
<         elif np.isclose(angle, -np.pi, atol=ANGLE_TOLERANCE):
<             return (np.array([[0, 1j],
<                               [1j, 0]]),
<                     "NOISY-RX-MINUS-180")
<     elif gate_name == "CZ":
<         assert params == ()
<         return np.diag([1, 1, 1, -1]), "NOISY-CZ"
<     raise NoisyGateUndefined("Undefined gate and params: {}{}\n"
<                              "Please restrict yourself to I, RX(+/-pi), RX(+/-pi/2), CZ")
---
> NOISY_GATES = {
>     ("I", ()): (np.eye(2), "NOISY-I"),
>     ("RX", (np.pi / 2,)): (np.array([[1, -1j],
>                                      [-1j, 1]]) / np.sqrt(2),
>                            "NOISY-RX-PLUS-90"),
>     ("RX", (-np.pi / 2,)): (np.array([[1, 1j],
>                                       [1j, 1]]) / np.sqrt(2),
>                             "NOISY-RX-MINUS-90"),
>     ("RX", (np.pi,)): (np.array([[0, -1j],
>                                  [-1j, 0]]),
>                        "NOISY-RX-PLUS-180"),
>     ("RX", (-np.pi,)): (np.array([[0, 1j],
>                                   [1j, 0]]),
>                         "NOISY-RX-MINUS-180"),
>     ("CZ", ()): (np.diag([1, 1, 1, -1]), "NOISY-CZ"),
> }
400c387,393
<         matrix, _ = get_noisy_gate(g.name, g.params)
---
>         if key in NOISY_GATES:
>             matrix, _ = NOISY_GATES[key]
>             if len(targets) == 1:
>                 noisy_I = noisy_identities_1q[targets[0]]
>             else:
>                 if len(targets) != 2:
>                     raise ValueError("Noisy gates on more than 2Q not currently supported")
402,403c395,396
<         if len(targets) == 1:
<             noisy_I = noisy_identities_1q[targets[0]]
---
>                 noisy_I = tensor_kraus_maps(noisy_identities_2q[targets[1]],
>                                             noisy_identities_2q[targets[0]])
405,408c398,399
<             if len(targets) != 2:
<                 raise ValueError("Noisy gates on more than 2Q not currently supported")
<             noisy_I = tensor_kraus_maps(noisy_identities_2q[targets[1]],
<                                         noisy_identities_2q[targets[0]])
---
>             raise ValueError("Cannot create noisy version of {}. ".format(g) +
>                              "Please restrict yourself to CZ, RX(+/-pi/2), I, RZ(theta)")
444c435
<             ideal_gate, new_name = get_noisy_gate(k.gate, tuple(k.params))
---
>             ideal_gate, new_name = NOISY_GATES[k.gate, tuple(k.params)]
450c441
<         except NoisyGateUndefined:
---
>         except KeyError:
478,479c469,471
<             try:
<                 _, new_name = get_noisy_gate(i.name, tuple(i.params))
---
>             key = (i.name, tuple(i.params))
>             if key in NOISY_GATES:
>                 _, new_name = NOISY_GATES[key]
481c473
<             except NoisyGateUndefined:
---
>             else:
