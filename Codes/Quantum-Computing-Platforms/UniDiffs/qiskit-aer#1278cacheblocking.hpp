--- qiskit-aer/qiskit-aer#1278/after/cacheblocking.hpp	2022-01-10 16:02:54.000000000 +0000
+++ qiskit-aer/qiskit-aer#1278/before/cacheblocking.hpp	2022-01-10 16:02:54.000000000 +0000
@@ -92,7 +92,7 @@
 
   void put_nongate_ops(std::vector<Operations::Op>& out,std::vector<Operations::Op>& queue,std::vector<Operations::Op>& input,bool doSwap) const;
 
-  uint_t add_ops(std::vector<Operations::Op>& ops,std::vector<Operations::Op>& out,std::vector<Operations::Op>& queue,bool doSwap,bool first,bool crossQubitOnly) const;
+  uint_t add_ops(std::vector<Operations::Op>& ops,std::vector<Operations::Op>& out,std::vector<Operations::Op>& queue,bool doSwap,bool first) const;
 
   void restore_qubits_order(std::vector<Operations::Op>& ops) const;
 
@@ -217,6 +217,9 @@
       return;
     }
 
+    result.metadata.add(true, "cacheblocking", "enabled");
+    result.metadata.add(block_bits_, "cacheblocking", "block_bits");
+
     qubitMap_.resize(qubits_);
     qubitSwapped_.resize(qubits_);
 
@@ -226,11 +229,6 @@
     }
 
     blocking_enabled_ = block_circuit(circ,true);
-
-    if(blocking_enabled_){
-      result.metadata.add(true, "cacheblocking", "enabled");
-      result.metadata.add(block_bits_, "cacheblocking", "block_bits");
-    }
   }
 
   if(gpu_blocking_bits_ > 0){
@@ -309,7 +307,7 @@
   uint_t j,iq,jq;
 
   //only gate and matrix can be reordered
-  if(op.type != Operations::OpType::gate && op.type != Operations::OpType::matrix && op.type != Operations::OpType::diagonal_matrix){
+  if(op.type != Operations::OpType::gate && op.type != Operations::OpType::matrix){
     //except for reset for density matrix
     if(!density_matrix_ || op.type != Operations::OpType::reset){
       return false;
@@ -339,33 +337,24 @@
   std::vector<Operations::Op> out;
   std::vector<Operations::Op> queue;
   std::vector<Operations::Op> queue_next;
-  bool crossQubits = false;
 
-  n = add_ops(circ.ops,out,queue,doSwap,true,crossQubits);
+  n = add_ops(circ.ops,out,queue,doSwap,true);
   while(queue.size() > 0){
-    n = add_ops(queue,out,queue_next,doSwap,false,crossQubits);
-
+    n = add_ops(queue,out,queue_next,doSwap,false);
     queue = queue_next;
     queue_next.clear();
     if(n == 0){
-      if(queue.size() > 0 && crossQubits == false){
-        crossQubits = true;
-        continue;
-      }
       break;
     }
-    crossQubits = false;
   }
 
-  if(queue.size() > 0){
+  if(queue.size() > 0)
     return false;
-  }
 
   if(save_state_)
     restore_qubits_order(out);
 
   circ.ops = out;
-
   return true;
 }
 
@@ -467,7 +456,7 @@
   return false;
 }
 
-uint_t CacheBlocking::add_ops(std::vector<Operations::Op>& ops,std::vector<Operations::Op>& out,std::vector<Operations::Op>& queue,bool doSwap,bool first,bool crossQubitOnly) const
+uint_t CacheBlocking::add_ops(std::vector<Operations::Op>& ops,std::vector<Operations::Op>& out,std::vector<Operations::Op>& queue,bool doSwap,bool first) const
 {
   uint_t i,j,iq;
 
@@ -490,17 +479,12 @@
       }
     }
     else{
-      if(crossQubitOnly){
-        //add multi-qubits gate at first
-        define_blocked_qubits(ops,blockedQubits,true);
-
-        //not enough qubits are blocked, then add one qubit gate
-        if(blockedQubits.size() < block_bits_)
-          define_blocked_qubits(ops,blockedQubits,false);
-      }
-      else{
+      //add multi-qubits gate at first
+      define_blocked_qubits(ops,blockedQubits,true);
+
+      //not enough qubits are blocked, then add one qubit gate
+      if(blockedQubits.size() < block_bits_)
         define_blocked_qubits(ops,blockedQubits,false);
-      }
     }
 
     pos_begin = out.size();
