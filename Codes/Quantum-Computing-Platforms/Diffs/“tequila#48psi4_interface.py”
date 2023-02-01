227c227,232
<         self.transformation = self._initialize_transformation(transformation=transformation, *args, **kwargs)
---
>     @property
>     def n_orbitals(self) -> int:
>         if self.active_space is not None:
>             return len(self.active_space.active_orbitals)
>         else:
>             return super().n_orbitals
613c618
<                 self._rdm2 = rdm2
---
>                 self._rdm2 = rdm2
\ No newline at end of file
