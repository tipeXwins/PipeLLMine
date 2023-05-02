557,558c557,558
< @pytest.mark.usefixtures("skip_if_no_tf_support")
< class TestTFGradients:
---
> dev = qml.device("default.qubit", wires=2)
> 
560,572c560,563
<     @pytest.fixture
<     def qnodes(self):
<         dev = qml.device("default.qubit", wires=2)
< 
<         @qml.qnode(dev, interface="tf")
<         def f(x):
<             qml.RX(x, wires=0)
<             return qml.expval(qml.PauliZ(0))
< 
<         @qml.qnode(dev, interface="tf")
<         def g(y):
<             qml.RY(y, wires=0)
<             return qml.expval(qml.PauliX(0))
---
> @qml.qnode(dev, interface="tf")
> def f(x):
>     qml.RX(x, wires=0)
>     return qml.expval(qml.PauliZ(0))
574c565,571
<         return f, g
---
> 
> @qml.qnode(dev, interface="tf")
> def g(y):
>     qml.RY(y, wires=0)
>     return qml.expval(qml.PauliX(0))
> @pytest.mark.usefixtures("skip_if_no_tf_support")
> class TestTFGradients:
577c574
<     def test_addition_qnodes_gradient(self, qnodes, x, y):
---
>     def test_addition_qnodes_gradient(self, x, y):
579d575
<         f, g = qnodes
622c618
<     def test_subtraction_qnodes_gradient(self, qnodes, x, y):
---
>     def test_subtraction_qnodes_gradient(self, x, y):
624d619
<         f, g = qnodes
644c639
<     def test_multiplication_qnodes_gradient(self, qnodes, x, y):
---
>     def test_multiplication_qnodes_gradient(self, x, y):
646d640
<         f, g = qnodes
666c660
<     def test_division_qnodes_gradient(self, qnodes, x, y, tol):
---
>     def test_division_qnodes_gradient(self, x, y, tol):
668d661
<         f, g = qnodes
688c681
<     def test_composition_qnodes_gradient(self, qnodes, x, y):
---
>     def test_composition_qnodes_gradient(self, x, y):
690d682
<         f, g = qnodes
