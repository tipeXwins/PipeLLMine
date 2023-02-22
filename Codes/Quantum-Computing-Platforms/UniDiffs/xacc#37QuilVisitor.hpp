--- xacc/xacc#37/after/QuilVisitor.hpp	2022-01-10 16:02:54.000000000 +0000
+++ xacc/xacc#37/before/QuilVisitor.hpp	2022-01-10 16:02:54.000000000 +0000
@@ -59,7 +59,6 @@
 	 */
 	std::string classicalAddresses;
 
-	std::map<int, int> qubitToClassicalBitIndex;
 	int numAddresses = 0;
 public:
 
@@ -102,7 +101,6 @@
 		quilStr += "MEASURE " + std::to_string(m.bits()[0]) + " [" + std::to_string(classicalBitIdx) + "]\n";
 		classicalAddresses += std::to_string(classicalBitIdx) + ", ";
 		numAddresses++;
-		qubitToClassicalBitIndex.insert(std::make_pair(m.bits()[0], classicalBitIdx));
 	}
 
 	/**
@@ -110,8 +108,7 @@
 	 */
 	void visit(ConditionalFunction& c) {
 		auto visitor = std::make_shared<QuilVisitor>();
-		auto classicalBitIdx = qubitToClassicalBitIndex[c.getConditionalQubit()];
-		quilStr += "JUMP-UNLESS @" + c.getName() + " [" + std::to_string(classicalBitIdx) + "]\n";
+		quilStr += "JUMP-UNLESS @" + c.getName() + " [" + std::to_string(c.getConditionalQubit()) + "]\n";
 		for (auto inst : c.getInstructions()) {
 			inst->accept(visitor);
 		}
