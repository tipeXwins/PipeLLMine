538,539c538,539
< @pytest.mark.usefixtures("skip_if_no_torch_support")
< class TestTorchGradients:
---
> dev = qml.device("default.qubit", wires=2)
> 
541,554c541,544
<     @pytest.fixture
<     def qnodes(self):
<         """Two QNodes to be used for the gradient tests"""
<         dev = qml.device("default.qubit", wires=2)
< 
<         @qml.qnode(dev, interface="torch")
<         def f(x):
<             qml.RX(x, wires=0)
<             return qml.expval(qml.PauliZ(0))
< 
<         @qml.qnode(dev, interface="torch")
<         def g(y):
<             qml.RY(y, wires=0)
<             return qml.expval(qml.PauliX(0))
---
> @qml.qnode(dev, interface="torch")
> def f(x):
>     qml.RX(x, wires=0)
>     return qml.expval(qml.PauliZ(0))
556c546,552
<         return f, g
---
> 
> @qml.qnode(dev, interface="torch")
> def g(y):
>     qml.RY(y, wires=0)
>     return qml.expval(qml.PauliX(0))
> @pytest.mark.usefixtures("skip_if_no_torch_support")
> class TestTorchGradients:
559c555
<     def test_addition_qnodes_gradient(self, qnodes, x, y):
---
>     def test_addition_qnodes_gradient(self, x, y):
561d556
<         f, g = qnodes
588c583
<     def test_subtraction_qnodes_gradient(self, qnodes, x, y):
---
>     def test_subtraction_qnodes_gradient(self, x, y):
590d584
<         f, g = qnodes
609c603
<     def test_multiplication_qnodes_gradient(self, qnodes, x, y):
---
>     def test_multiplication_qnodes_gradient(self, x, y):
611d604
<         f, g = qnodes
635c628
<     def test_division_qnodes_gradient(self, qnodes, x, y):
---
>     def test_division_qnodes_gradient(self, x, y):
637d629
<         f, g = qnodes
657c649
<     def test_composition_qnodes_gradient(self, qnodes, x, y):
---
>     def test_composition_qnodes_gradient(self, x, y):
659d650
<         f, g = qnodes
