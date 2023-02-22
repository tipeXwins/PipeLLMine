--- pyquil/pyquil#174/after/setup.py	2022-01-10 16:02:54.000000000 +0000
+++ pyquil/pyquil#174/before/setup.py	2022-01-10 16:02:54.000000000 +0000
@@ -25,7 +25,7 @@
     author_email="softapps@rigetti.com",
     description="A Python library to generate Quantum Instruction Language (Quil) Programs.",
     url="https://github.com/rigetticomputing/pyquil.git",
-    packages=['pyquil', 'pyquil._parser', 'pyquil.setup'],
+    packages=['pyquil', 'pyquil.setup'],
     license="LICENSE",
     install_requires=[
         'requests >= 2.4.2',
