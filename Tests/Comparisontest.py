import unittest

from Pipeline.Comparison import ComparerNLTKCodeBleu
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


if __name__ == '__main__':
    unittest.main()
