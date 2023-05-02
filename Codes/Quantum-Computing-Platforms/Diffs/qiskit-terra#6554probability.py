25c25
<     _bitstring_regex = re.compile(r"^[01]+$")
---
>     bitstring_regex = re.compile(r"^[01]+$")
57c57
<                 elif self._bitstring_regex.search(first_key):
---
>                 elif self.bitstring_regex.search(first_key):
70c70
<     def binary_probabilities(self, num_bits=None):
---
>     def binary_probabilities(self):
77,78c77
<         n = len(bin(max(self.keys(), default=0))) - 2 if num_bits is None else num_bits
<         return {format(key, "b").zfill(n): value for key, value in self.items()}
---
>         return {bin(key)[2:]: value for key, value in self.items()}
