45c45
<         circ, delta = get_ghz_mqc_para(qn)
---
>         circ, delta = get_ghz_mqc_para(qn, measure='full')
55c55
<         circ, params = get_ghz_po_para(qn)
---
>         circ, params = get_ghz_po_para(qn, measure='full')
59a60
>         gap_factor = 2.0/3
65,66c66,67
<         self.assertTrue(even_counts in (0, 16))
<         self.assertTrue(odd_counts in (0, 16))
---
>         self.assertTrue((even_counts > gap_factor*1024) or
>                         odd_counts > gap_factor*1024)
