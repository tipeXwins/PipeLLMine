import unittest
from Pipeline.OutputReconstructor import ReconstructorPatch

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
        resultReconstructor = reconstructor.reconstruct(queryCodet5,returnedCodet5,"<extra_id_0>")
        reconstructionExpected = "def bitcount(n):\
            count = 0\
            while n:\
                n = n.\
                count += 1\
            return count"
        print(resultReconstructor)
        self.assertEqual(reconstructionExpected, resultReconstructor)

if __name__ == '__main__':
    unittest.main()