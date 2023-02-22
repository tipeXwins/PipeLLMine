--- ProjectQ/ProjectQ#203/after/simulator.hpp	2022-01-10 16:02:54.000000000 +0000
+++ ProjectQ/ProjectQ#203/before/simulator.hpp	2022-01-10 16:02:54.000000000 +0000
@@ -335,7 +335,6 @@
         unsigned s = std::abs(time) * op_nrm + 1.;
         complex_type correction = std::exp(-time * I * tr / (double)s);
         auto output_state = vec_;
-        auto ctrlmask = get_control_mask(ctrl);
         for (unsigned i = 0; i < s; ++i){
             calc_type nrm_change = 1.;
             for (unsigned k = 0; nrm_change > 1.e-12; ++k){
@@ -343,7 +342,7 @@
                 auto current_state = vec_;
                 auto update = StateVector(vec_.size(), 0.);
                 for (auto const& tup : td){
-                    apply_term(tup.first, ids, {});
+                    apply_term(tup.first, ids, ctrl);
                     #pragma omp parallel for schedule(static)
                     for (std::size_t j = 0; j < vec_.size(); ++j){
                         update[j] += vec_[j] * tup.second;
@@ -355,17 +354,14 @@
                 for (std::size_t j = 0; j < vec_.size(); ++j){
                     update[j] *= coeff;
                     vec_[j] = update[j];
-                    if ((j & ctrlmask) == ctrlmask){
-                        output_state[j] += update[j];
-                        nrm_change += std::norm(update[j]);
-                    }
+                    output_state[j] += update[j];
+                    nrm_change += std::norm(update[j]);
                 }
                 nrm_change = std::sqrt(nrm_change);
             }
             #pragma omp parallel for schedule(static)
             for (std::size_t j = 0; j < vec_.size(); ++j){
-                if ((j & ctrlmask) == ctrlmask)
-                    output_state[j] *= correction;
+                output_state[j] *= correction;
                 vec_[j] = output_state[j];
             }
         }
