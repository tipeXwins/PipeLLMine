67a68
>     cal_circuits = []
69a71,74
>     # create classical bit registers
>     if cr is None:
>         cr = ClassicalRegister(nqubits)
> 
73,74c78,90
<     cal_circuits, _ = tensored_meas_cal([qubit_list],
<                                         qr, cr, circlabel)
---
>     for basis_state in state_labels:
>         qc_circuit = QuantumCircuit(qr, cr,
>                                     name='%scal_%s' % (circlabel, basis_state))
>         for qind, _ in enumerate(basis_state):
>             if int(basis_state[nqubits-qind-1]):
>                 # the index labeling of the label is backwards with
>                 # the list
>                 qc_circuit.x(qr[qubit_list[qind]])
> 
>             # add measurements
>             qc_circuit.measure(qr[qubit_list[qind]], cr[qind])
> 
>         cal_circuits.append(qc_circuit)
