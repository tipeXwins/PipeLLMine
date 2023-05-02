146,150d145
<     def adjoint(self):  # pylint: disable=arguments-differ
<         return qml.adjoint(qml.templates.MottonenStatePreparation)(
<             self.parameters[0], wires=self.wires
<         )
< 
