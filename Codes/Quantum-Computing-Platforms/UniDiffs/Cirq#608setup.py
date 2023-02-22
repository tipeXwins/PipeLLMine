--- Cirq/Cirq#608/after/setup.py	2022-01-10 16:02:54.000000000 +0000
+++ Cirq/Cirq#608/before/setup.py	2022-01-10 16:02:54.000000000 +0000
@@ -26,7 +26,6 @@
 requirements = open('runtime-requirements.txt').readlines()
 requirements = [r.strip() for r in requirements]
 
-cirq_packages = ['cirq.' + package for package in find_packages(where='cirq')]
 setup(
     name='cirq',
     version=__version__,
@@ -34,5 +33,5 @@
     author='The Cirq Developers',
     install_requires=requirements,
     license='Apache 2',
-    packages=cirq_packages,
+    packages=find_packages(),
     package_data={'cirq.api.google.v1': ['*.proto']})
