--- xacc/xacc#164/after/PulseScheduler.hpp	2022-01-10 16:02:54.000000000 +0000
+++ xacc/xacc#164/before/PulseScheduler.hpp	2022-01-10 16:02:54.000000000 +0000
@@ -21,7 +21,7 @@
 public:
   void schedule(std::shared_ptr<CompositeInstruction> program) override;
   const std::string name() const override {
-		return "pulse";
+		return "default";
 	}
 
 	const std::string description() const override{
