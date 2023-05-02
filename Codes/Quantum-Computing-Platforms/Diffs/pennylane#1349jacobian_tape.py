96,99d95
<     def copy(self, copy_operations=False, tape_cls=None):
<         copied_tape = super().copy(copy_operations=copy_operations, tape_cls=tape_cls)
<         copied_tape.jacobian_options = self.jacobian_options
<         return copied_tape
