--- dwave-system/dwave-system#418/after/setup.py	2022-01-10 16:02:54.000000000 +0000
+++ dwave-system/dwave-system#418/before/setup.py	2022-01-10 16:02:54.000000000 +0000
@@ -25,7 +25,7 @@
 exec(open(os.path.join(".", "dwave", "system", "package_info.py")).read())
 
 
-install_requires = ['dimod>=0.9.11,<0.11.0',
+install_requires = ['dimod[preprocessing]>=0.9.11,<0.11.0',
                     'dwave-cloud-client>=0.8.4,<0.9.0',
                     'dwave-networkx>=0.8.4',
                     'networkx>=2.0,<3.0',
