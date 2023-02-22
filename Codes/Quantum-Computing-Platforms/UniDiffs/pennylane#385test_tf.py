--- pennylane/pennylane#385/after/test_tf.py	2022-01-10 16:02:54.000000000 +0000
+++ pennylane/pennylane#385/before/test_tf.py	2022-01-10 16:02:54.000000000 +0000
@@ -554,29 +554,25 @@
 ]
 
 
-@pytest.mark.usefixtures("skip_if_no_tf_support")
-class TestTFGradients:
+dev = qml.device("default.qubit", wires=2)
+
 
-    @pytest.fixture
-    def qnodes(self):
-        dev = qml.device("default.qubit", wires=2)
-
-        @qml.qnode(dev, interface="tf")
-        def f(x):
-            qml.RX(x, wires=0)
-            return qml.expval(qml.PauliZ(0))
-
-        @qml.qnode(dev, interface="tf")
-        def g(y):
-            qml.RY(y, wires=0)
-            return qml.expval(qml.PauliX(0))
+@qml.qnode(dev, interface="tf")
+def f(x):
+    qml.RX(x, wires=0)
+    return qml.expval(qml.PauliZ(0))
 
-        return f, g
+
+@qml.qnode(dev, interface="tf")
+def g(y):
+    qml.RY(y, wires=0)
+    return qml.expval(qml.PauliX(0))
+@pytest.mark.usefixtures("skip_if_no_tf_support")
+class TestTFGradients:
 
     @pytest.mark.parametrize("x, y", gradient_test_data)
-    def test_addition_qnodes_gradient(self, qnodes, x, y):
+    def test_addition_qnodes_gradient(self, x, y):
         """Test the gradient of addition of two QNode circuits"""
-        f, g = qnodes
 
         def add(a, b):
             return a + b
@@ -619,9 +615,8 @@
         assert grad[1].numpy() == 1.0
 
     @pytest.mark.parametrize("x, y", gradient_test_data)
-    def test_subtraction_qnodes_gradient(self, qnodes, x, y):
+    def test_subtraction_qnodes_gradient(self, x, y):
         """Test the gradient of subtraction of two QNode circuits"""
-        f, g = qnodes
 
         def subtract(a, b):
             return a - b
@@ -641,9 +636,8 @@
         assert grad[1].numpy() == -1.0
 
     @pytest.mark.parametrize("x, y", gradient_test_data)
-    def test_multiplication_qnodes_gradient(self, qnodes, x, y):
+    def test_multiplication_qnodes_gradient(self, x, y):
         """Test the gradient of multiplication of two QNode circuits"""
-        f, g = qnodes
 
         def mult(a, b):
             return a * b
@@ -663,9 +657,8 @@
         assert grad[1].numpy() == a.numpy()
 
     @pytest.mark.parametrize("x, y", gradient_test_data)
-    def test_division_qnodes_gradient(self, qnodes, x, y, tol):
+    def test_division_qnodes_gradient(self, x, y, tol):
         """Test the gradient of division of two QNode circuits"""
-        f, g = qnodes
 
         def div(a, b):
             return a / b
@@ -685,9 +678,8 @@
         assert np.allclose(grad[1].numpy(), -a.numpy() / b.numpy() ** 2, atol=tol, rtol=0)
 
     @pytest.mark.parametrize("x, y", gradient_test_data)
-    def test_composition_qnodes_gradient(self, qnodes, x, y):
+    def test_composition_qnodes_gradient(self, x, y):
         """Test the gradient of composition of two QNode circuits"""
-        f, g = qnodes
 
         xt = Variable(x)
         yt = Variable(y)
