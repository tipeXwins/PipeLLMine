--- xacc/xacc#309/after/GateFusion.cpp	2022-01-10 16:02:54.000000000 +0000
+++ xacc/xacc#309/before/GateFusion.cpp	2022-01-10 16:02:54.000000000 +0000
@@ -27,11 +27,6 @@
 
         return result;
     }
-    std::vector<size_t> reverseBitIdx(const std::vector<size_t>& in_origBit) {
-        auto copy = in_origBit;
-        std::reverse(copy.begin(), copy.end());
-        return copy;
-    }
 }
 namespace xacc {
 namespace quantum {
@@ -132,7 +127,7 @@
                0, 1, 0, 0,
                0, 0, 0, 1,
                0, 0, 1, 0;
-    m_gates.emplace_back(cnotMat, reverseBitIdx(cnot.bits()));
+    m_gates.emplace_back(cnotMat, cnot.bits());
 }
 
 void GateFuser::visit(Rx& rx) 
@@ -205,14 +200,14 @@
                 0, 1, 0, 0,
                 0, 0, 0, -I,
                 0, 0, I, 0;
-    m_gates.emplace_back(cyMat, reverseBitIdx(cy.bits()));
+    m_gates.emplace_back(cyMat, cy.bits());
 }
 
 void GateFuser::visit(CZ& cz) 
 {
     Eigen::MatrixXcd czMat{ Eigen::MatrixXcd::Identity(4, 4) };
     czMat(3, 3) = -1;
-    m_gates.emplace_back(czMat, reverseBitIdx(cz.bits()));
+    m_gates.emplace_back(czMat, cz.bits());
 }
 
 void GateFuser::visit(CRZ& crz) 
@@ -225,7 +220,7 @@
             0, 1, 0, 0,
             0, 0, rzMat(0, 0), rzMat(0, 1),
             0, 0, rzMat(1, 0), rzMat(1, 1);
-    m_gates.emplace_back(crzMat, reverseBitIdx(crz.bits()));
+    m_gates.emplace_back(crzMat, crz.bits());
 }
 
 void GateFuser::visit(CH& ch) 
@@ -235,7 +230,7 @@
                 0, 1, 0, 0,
                 0, 0, 1 / std::sqrt(2.), 1 / std::sqrt(2.), 
                 0, 0, 1 / std::sqrt(2.), -1 / std::sqrt(2.);
-    m_gates.emplace_back(chMat, reverseBitIdx(ch.bits()));
+    m_gates.emplace_back(chMat, ch.bits());
 }
 
 void GateFuser::visit(Swap& s) 
@@ -254,7 +249,7 @@
     const double angle = InstructionParameterToDouble(cphase.getParameter(0));
     const std::complex<double> val = std::exp(I*angle);
     cphaseMat(3, 3) = val;
-    m_gates.emplace_back(cphaseMat, reverseBitIdx(cphase.bits()));
+    m_gates.emplace_back(cphaseMat, cphase.bits());
 }
 
 void GateFuser::visit(Measure& measure) 
