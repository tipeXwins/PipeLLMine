--- OpenQL/OpenQL#375/after/visualizer_internal.h	2022-01-10 16:02:54.000000000 +0000
+++ OpenQL/OpenQL#375/before/visualizer_internal.h	2022-01-10 16:02:54.000000000 +0000
@@ -25,17 +25,15 @@
 enum BitType {CLASSICAL, QUANTUM};
 
 struct Position4 {
-    long x0;
-    long y0;
-    long x1;
-    long y1;
-    Position4() = delete;
+    long x0 = 0;
+    long y0 = 0;
+    long x1 = 0;
+    long y1 = 0;
 };
 
 struct Position2 {
-    long x;
-    long y;
-    Position2() = delete;
+    long x = 0;
+    long y = 0;
 };
 
 struct Cell {
@@ -56,8 +54,8 @@
 };
 
 struct GateOperand {
-    BitType bitType;
-    int index;
+    BitType bitType = QUANTUM;
+    int index = 0;
 
     friend bool operator<(const GateOperand &lhs, const GateOperand &rhs) {
         if (lhs.bitType == QUANTUM && rhs.bitType == CLASSICAL) return true;
@@ -68,29 +66,24 @@
     friend bool operator>(const GateOperand &lhs, const GateOperand &rhs) {return operator<(rhs, lhs);}
     friend bool operator<=(const GateOperand &lhs, const GateOperand &rhs) {return !operator>(lhs, rhs);}
     friend bool operator>=(const GateOperand &lhs, const GateOperand &rhs) {return !operator<(lhs, rhs);}
-
-    GateOperand() = delete;
 };
 
 struct GateProperties {
     std::string name;
     std::vector<int> operands;
     std::vector<int> creg_operands;
-    int duration;
-    int cycle;
-    gate_type_t type;
+    int duration = 0;
+    int cycle = 0;
+    gate_type_t type = __custom_gate__;
     std::vector<int> codewords;
     std::string visual_type;
-
-    GateProperties() = delete;
 };
 
 struct Cycle {
-    int index;
-    bool empty;
-    bool cut;
+    int index = 0;
+    bool empty = false;
+    bool cut = false;
     std::vector<std::vector<std::reference_wrapper<GateProperties>>> gates;
-    Cycle() = delete;
 };
 
 enum LineSegmentType {FLAT, PULSE, CUT};
@@ -155,7 +148,7 @@
 
     CircuitData(std::vector<GateProperties> &gates, const Layout layout, const int cycleDuration);
 
-    Cycle getCycle(const size_t index) const;
+    Cycle getCycle(const int index) const;
     int getAmountOfCycles() const;
     bool isCycleCut(const int cycleIndex) const;
     bool isCycleFirstInCutRange(const int cycleIndex) const;
@@ -199,7 +192,7 @@
     int getCircuitBotY() const;
 
     Dimensions getCellDimensions() const;
-    Position4 getCellPosition(const size_t column, const size_t row, const BitType bitType) const;
+    Position4 getCellPosition(const int column, const int row, const BitType bitType) const;
     std::vector<std::pair<EndPoints, bool>> getBitLineSegments() const;
 
     void printProperties() const;
@@ -248,4 +241,4 @@
 
 } // namespace ql
 
-#endif //WITH_VISUALIZER
+#endif //WITH_VISUALIZER
\ No newline at end of file
