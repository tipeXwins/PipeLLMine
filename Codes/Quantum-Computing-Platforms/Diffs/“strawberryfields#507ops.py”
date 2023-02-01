597,598c597
<         np_args = [arg.numpy() if hasattr(arg, "numpy") else arg for arg in [r, phi]]
<         is_complex = any([np.iscomplexobj(np.real_if_close(arg)) for arg in np_args])
---
>         tf_complex = any(hasattr(arg, "numpy") and np.iscomplex(arg.numpy()) for arg in [r, phi])
600c599
<         if is_complex:
---
>         if (np.iscomplex([r, phi])).any() or tf_complex:
726,727c725,727
<         np_args = [arg.numpy() if hasattr(arg, "numpy") else arg for arg in p]
<         is_complex = any([np.iscomplexobj(np.real_if_close(arg)) for arg in np_args])
---
>         tf_complex = any(
>             hasattr(arg, "numpy") and np.iscomplex(arg.numpy()) for arg in [p[0], p[1], p[2], p[3]]
>         )
729c729
<         if is_complex:
---
>         if (np.iscomplex([p[0], p[1], p[2], p[3]])).any() or tf_complex:
1340,1341c1340
<         np_args = [arg.numpy() if hasattr(arg, "numpy") else arg for arg in [r, phi]]
<         is_complex = any([np.iscomplexobj(np.real_if_close(arg)) for arg in np_args])
---
>         tf_complex = any(hasattr(arg, "numpy") and np.iscomplex(arg.numpy()) for arg in [r, phi])
1343c1342
<         if is_complex:
---
>         if (np.iscomplex([r, phi])).any() or tf_complex:
