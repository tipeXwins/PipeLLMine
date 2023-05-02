296,300d295
<             if isinstance(t, complex):
<                 raise ValueError("Beamsplitter transmittivity t must be a float.")
<             if isinstance(t, tf.Tensor):
<                 if t.dtype.is_complex:
<                     raise ValueError("Beamsplitter transmittivity t must be a float.")
