import unittest

from Pipeline.Comparison import ComparerNLTKCodeBleu, MultipleComparerNLTKCodeBleu
class Comparison(unittest.TestCase):
    def test_CodeBleuNLTK(self):
        references = ['\n', 'def bitcount(n):\n', '    count = 0\n', '    while n:\n', '        n ^= n - 1\n',
                      '        count += 1\n', '    return count\n']
        hypotheses = ['\n', 'def bitcount(n):\n', '    count = 0\n', '    while n:\n', '        n &= n - 1\n',
                      '        count += 1\n', '    return count\n']
        comparer = ComparerNLTKCodeBleu()
        code_bleu = comparer.compare(references, hypotheses)
        print(f"CodeBleu score: {code_bleu}")

        self.assertAlmostEqual(0.82, code_bleu, delta=0.05 )  # add assertion here
    def test_Multiple_CodeBleuNLTK(self):
        reference = ['\n', 'def bitcount(n):\n', '    count = 0\n', '    while n:\n', '        n ^= n - 1\n',
                      '        count += 1\n', '    return count\n']
        hypotheses = [['\n', 'def bitcount(n):\n', '    count = 0\n', '    while n:\n', '        n &= n - 1\n',
                      '        count += 1\n', '    return count\n'],['\n', 'def bitcount(n):\n', '    count = 0\n', '    while n:\n', '        n ^= n - 1\n',
                      '        count += 1\n', '    return count\n']]
        multipleComparer = MultipleComparerNLTKCodeBleu(1)
        metric = multipleComparer.compareMultipleOutputs(hypotheses,reference)
        self.assertEqual(metric, 1)  
        multipleComparer.setCodeBleuRef(0.8)
        metric = multipleComparer.compareMultipleOutputs(hypotheses,reference)
        self.assertEqual(metric, 2)  


if __name__ == '__main__':
    unittest.main()
