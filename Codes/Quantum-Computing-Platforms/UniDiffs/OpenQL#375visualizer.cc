--- OpenQL/OpenQL#375/after/visualizer.cc	2022-01-10 16:02:54.000000000 +0000
+++ OpenQL/OpenQL#375/before/visualizer.cc	2022-01-10 16:02:54.000000000 +0000
@@ -73,10 +73,10 @@
 // ======================================================= //
 
 CircuitData::CircuitData(std::vector<GateProperties> &gates, const Layout layout, const int cycleDuration) :
-    cycles(generateCycles(gates, cycleDuration)),
+    cycleDuration(cycleDuration),
     amountOfQubits(calculateAmountOfBits(gates, &GateProperties::operands)),
     amountOfClassicalBits(calculateAmountOfBits(gates, &GateProperties::creg_operands)),
-    cycleDuration(cycleDuration)
+    cycles(generateCycles(gates, cycleDuration))
 {
     if (layout.cycles.areCompressed())      compressCycles();
     if (layout.cycles.arePartitioned())     partitionCyclesWithOverlap();
@@ -224,8 +224,8 @@
                         const std::pair<GateOperand, GateOperand> edgeOperands1 = calculateEdgeOperands(getGateOperands(candidate), amountOfQubits);
                         for (const GateProperties &gateInChunk : chunk) {
                             const std::pair<GateOperand, GateOperand> edgeOperands2 = calculateEdgeOperands(getGateOperands(gateInChunk), amountOfQubits);
-                            if ((edgeOperands1.first >= edgeOperands2.first && edgeOperands1.first <= edgeOperands2.second) ||
-                                (edgeOperands1.second >= edgeOperands2.first && edgeOperands1.second <= edgeOperands2.second))
+                            if (edgeOperands1.first >= edgeOperands2.first && edgeOperands1.first <= edgeOperands2.second ||
+                                edgeOperands1.second >= edgeOperands2.first && edgeOperands1.second <= edgeOperands2.second)
                             {
                                 gateOverlaps = true;
                             }
@@ -326,7 +326,7 @@
     return rangesAboveThreshold;
 }
 
-Cycle CircuitData::getCycle(const size_t index) const {
+Cycle CircuitData::getCycle(const int index) const {
     if (index > cycles.size())
         FATAL("Requested cycle index " << index << " is higher than max cycle " << (cycles.size() - 1) << "!");
 
@@ -536,7 +536,7 @@
     return cellDimensions;
 }
 
-Position4 Structure::getCellPosition(const size_t column, const size_t row, const BitType bitType) const {
+Position4 Structure::getCellPosition(const int column, const int row, const BitType bitType) const {
     switch (bitType) {
         case CLASSICAL:
             if (layout.pulses.areEnabled())
