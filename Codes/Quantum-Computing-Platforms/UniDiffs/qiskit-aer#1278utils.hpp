--- qiskit-aer/qiskit-aer#1278/after/utils.hpp	2022-01-10 16:02:54.000000000 +0000
+++ qiskit-aer/qiskit-aer#1278/before/utils.hpp	2022-01-10 16:02:54.000000000 +0000
@@ -19,7 +19,6 @@
 #include <sstream>
 #include <cmath>
 #include <limits>
-#include <string>
 
 #include "framework/avx2_detect.hpp"
 #include "framework/types.hpp"
@@ -28,16 +27,6 @@
 #include <intrin.h>
 #endif
 
-#if defined(__linux__) || defined(__APPLE__)
-#include <unistd.h>
-#elif defined(_WIN64) || defined(_WIN32)
-// This is needed because windows.h redefine min()/max() so interferes with
-// std::min/max
-#define NOMINMAX
-#include <windows.h>
-#endif
-
-
 namespace AER {
 namespace Utils {
 
@@ -1273,23 +1262,6 @@
 #endif
 
 
-size_t get_system_memory_mb() 
-{
-  size_t total_physical_memory = 0;
-#if defined(__linux__) || defined(__APPLE__)
-  size_t pages = (size_t)sysconf(_SC_PHYS_PAGES);
-  size_t page_size = (size_t)sysconf(_SC_PAGE_SIZE);
-  total_physical_memory = pages * page_size;
-#elif defined(_WIN64) || defined(_WIN32)
-  MEMORYSTATUSEX status;
-  status.dwLength = sizeof(status);
-  GlobalMemoryStatusEx(&status);
-  total_physical_memory = status.ullTotalPhys;
-#endif
-  return total_physical_memory >> 20;
-}
-
-
 //------------------------------------------------------------------------------
 } // end namespace Utils
 //------------------------------------------------------------------------------
