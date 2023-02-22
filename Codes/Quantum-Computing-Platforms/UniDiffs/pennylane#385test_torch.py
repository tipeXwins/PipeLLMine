--- pennylane/pennylane#385/after/test_torch.py	2022-01-10 16:02:54.000000000 +0000
+++ pennylane/pennylane#385/before/test_torch.py	2022-01-10 16:02:54.000000000 +0000
@@ -535,30 +535,25 @@
 ]
 
 
-@pytest.mark.usefixtures("skip_if_no_torch_support")
-class TestTorchGradients:
+dev = qml.device("default.qubit", wires=2)
+
 
-    @pytest.fixture
-    def qnodes(self):
-        """Two QNodes to be used for the gradient tests"""
-        dev = qml.device("default.qubit", wires=2)
-
-        @qml.qnode(dev, interface="torch")
-        def f(x):
-            qml.RX(x, wires=0)
-            return qml.expval(qml.PauliZ(0))
-
-        @qml.qnode(dev, interface="torch")
-        def g(y):
-            qml.RY(y, wires=0)
-            return qml.expval(qml.PauliX(0))
+@qml.qnode(dev, interface="torch")
+def f(x):
+    qml.RX(x, wires=0)
+    return qml.expval(qml.PauliZ(0))
 
-        return f, g
+
+@qml.qnode(dev, interface="torch")
+def g(y):
+    qml.RY(y, wires=0)
+    return qml.expval(qml.PauliX(0))
+@pytest.mark.usefixtures("skip_if_no_torch_support")
+class TestTorchGradients:
 
     @pytest.mark.parametrize("x, y", gradient_test_data)
-    def test_addition_qnodes_gradient(self, qnodes, x, y):
+    def test_addition_qnodes_gradient(self, x, y):
         """Test the gradient of addition of two QNode circuits"""
-        f, g = qnodes
 
         def add(a, b):
             return a + b
@@ -585,9 +580,8 @@
         assert a.grad == 2.0
 
     @pytest.mark.parametrize("x, y", gradient_test_data)
-    def test_subtraction_qnodes_gradient(self, qnodes, x, y):
+    def test_subtraction_qnodes_gradient(self, x, y):
         """Test the gradient of subtraction of two QNode circuits"""
-        f, g = qnodes
 
         def subtract(a, b):
             return a - b
@@ -606,9 +600,8 @@
         assert b.grad == -1.0
 
     @pytest.mark.parametrize("x, y", gradient_test_data)
-    def test_multiplication_qnodes_gradient(self, qnodes, x, y):
+    def test_multiplication_qnodes_gradient(self, x, y):
         """Test the gradient of multiplication of two QNode circuits"""
-        f, g = qnodes
 
         def mult(a, b):
             return a * b
@@ -632,9 +625,8 @@
         b.retain_grad()
 
     @pytest.mark.parametrize("x, y", gradient_test_data)
-    def test_division_qnodes_gradient(self, qnodes, x, y):
+    def test_division_qnodes_gradient(self, x, y):
         """Test the gradient of division of two QNode circuits"""
-        f, g = qnodes
 
         def div(a, b):
             return a / b
@@ -654,9 +646,8 @@
         assert b.grad == -a / b ** 2
 
     @pytest.mark.parametrize("x, y", gradient_test_data)
-    def test_composition_qnodes_gradient(self, qnodes, x, y):
+    def test_composition_qnodes_gradient(self, x, y):
         """Test the gradient of composition of two QNode circuits"""
-        f, g = qnodes
 
         def compose(f, x):
             return f(x)
