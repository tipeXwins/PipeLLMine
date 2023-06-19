import unittest
from Pipeline.OutputReconstructor import ReconstructorPatch, ReconstructorTruncate

class ReconstructorTestCase(unittest.TestCase):
    def test_ReconstructorPatch(self):
        queryCodet5 = "def bitcount(n):\
            count = 0\
            while n:\
                <extra_id_0>\
                count += 1\
            return count"
        returnedCodet5 = "n = n."

        reconstructor = ReconstructorPatch()
        reconstructor.setPlaceholder("<extra_id_0>")
        resultReconstructor = reconstructor.reconstruct(queryCodet5,returnedCodet5)
        reconstructionExpected = "def bitcount(n):\
            count = 0\
            while n:\
                n = n.\
                count += 1\
            return count"
        print(resultReconstructor)
        self.assertEqual(reconstructionExpected, resultReconstructor)


    def test_ReconstructorTruncate(self):
        f = open('Tests/resources/inputQuantum.py', "r")
        originalContent = f.readlines()
        f.close()
        returnedContent= ['    Fixed wires are returned as is:\n', '        "free wires represented by  Victor.\n', '\n', '        Fixed wires are returned as is, free wires represented by\n', '        :class:`~.variable.Variable` instances are replaced by their\n', '        current numerical value.\n', '\n', '        Returns:\n', '            list[int]: wire values\n', '        """\n', '        w = [i.val if isinstance(i, Variable) else i for i in self._wires]\n', '        self.check_wires(w)\n', '        return w\n', '\n', '    @property\n', '    def parameters(self):\n', '        """Current parameter values.\n', '\n', '        Fixed parameters are returned as is, free parameters represented by\n', '        :class:`~.variable.Variable` instances are replaced by their\n']

        reconstructor = ReconstructorTruncate(373)
        #resultReconstructor = reconstructor.reconstruct(originalContent,returnedCodet5)
        reconstructionExpected = "def bitcount(n):\
            count = 0\
            while n:\
                n = n.\
                count += 1\
            return count"
        reconstructor = ReconstructorTruncate(373,10,10)
        with open('Tests/resources/outputs/reconstructorTruncate.txt', 'w') as file:
            file.writelines(reconstructor.reconstruct(originalContent, returnedContent))
        #print(resultReconstructor)
        #self.assertEqual(reconstructionExpected, resultReconstructor)
if __name__ == '__main__':
    unittest.main()