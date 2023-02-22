--- OpenQL/OpenQL#295/after/options.h	2022-01-10 16:02:54.000000000 +0000
+++ OpenQL/OpenQL#295/before/options.h	2022-01-10 16:02:54.000000000 +0000
@@ -82,7 +82,7 @@
           app->add_set_ignore_case("--optimize", opt_name2opt_val["optimize"], {"yes", "no"}, "optimize or not", true);
           app->add_set_ignore_case("--clifford_premapper", opt_name2opt_val["clifford_premapper"], {"yes", "no"}, "clifford optimize before mapping yes or not", true);
           app->add_set_ignore_case("--clifford_postmapper", opt_name2opt_val["clifford_postmapper"], {"yes", "no"}, "clifford optimize after mapping yes or not", true);
-          app->add_set_ignore_case("--decompose_toffoli", opt_name2opt_val["decompose_toffoli"], {"no", "NC", "AM"}, "Type of decomposition used for toffoli", true);
+          app->add_set_ignore_case("--decompose_toffoli", opt_name2opt_val["decompose_toffoli"], {"no", "NC", "MA"}, "Type of decomposition used for toffoli", true);
           app->add_set_ignore_case("--quantumsim", opt_name2opt_val["quantumsim"], {"no", "yes", "qsoverlay"}, "Produce quantumsim output, and of which kind", true);
           app->add_option("--backend_cc_map_input_file", opt_name2opt_val["backend_cc_map_input_file"], "Name of CC input map file", true);
           app->add_set_ignore_case("--cz_mode", opt_name2opt_val["cz_mode"], {"manual", "auto"}, "CZ mode", true);
