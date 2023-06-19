import unittest
#from Pipeline.Query_Creation import *
from Pipeline.Query_Creation import HFCodegenHintQuery, HFCodegenStandardQuery, HFHintQuery, HFPlBartHintQuery, HFPlBartStandardQuery, HFStandardQuery, OAIHintQuery

class QueryTestCase(unittest.TestCase):
    def test_HFHintQuery(self):
        queryGenerator = HFHintQuery("<mask>",[4],None,[4])
        f = open('Tests/resources/input.py', "r")
        text = f.readlines()
        f.close()
        resultQueryGenerated = queryGenerator.createQuery(text)
        print("Query", resultQueryGenerated)

        queryExpected = ['def bitcount(n):\n', '    count = 0\n', '    while n:\n', '        #buggy line:        count += 1\n', '        <mask>', '    return count\n']

        self.assertEqual(queryExpected, resultQueryGenerated)

    def test_HFHintQueryTruncation(self):
        queryGenerator = HFHintQuery("<mask>",[374],None,[374])
        f = open('Tests/resources/inputQuantum.py', "r")
        text = f.readlines()
        f.close()
        queryGenerator.setTruncation(True)
        resultQueryGenerated = queryGenerator.createQuery(text)
        print("Query", resultQueryGenerated)

        queryExpected = ['    def wires(self):\n', '        """Current wire values.\n', '\n', '        Fixed wires are returned as is, free wires represented by\n', '        :class:`~.variable.Variable` instances are replaced by their\n', '        current numerical value.\n', '\n', '        Returns:\n', '            list[int]: wire values\n', '        """\n', '        #buggy line:        w = [i.val if isinstance(i, Variable) else i for i in self._wires]\n', '        <mask>', '        self.check_wires(w)\n', '        return w\n', '\n', '    @property\n', '    def parameters(self):\n', '        """Current parameter values.\n', '\n', '        Fixed parameters are returned as is, free parameters represented by\n', '        :class:`~.variable.Variable` instances are replaced by their\n']

        self.assertEqual(queryExpected, resultQueryGenerated)

    def test_HFStandardQuery(self):
        f = open('Tests/resources/input.py', "r")
        text = f.readlines()
        f.close()
        queryGenerator = HFStandardQuery("<mask>",[4])

        resultQueryGenerated = queryGenerator.createQuery(text)
        print("Query", resultQueryGenerated)

        queryExpected = ['def bitcount(n):\n', '    count = 0\n', '    while n:\n', '        <mask>', '    return count\n']

        self.assertEqual(queryExpected, resultQueryGenerated)
    
    def test_HFStandardQueryTruncation(self):
        f = open('Tests/resources/inputQuantum.py', "r")
        text = f.readlines()
        f.close()
        queryGenerator = HFStandardQuery("<mask>",[374])
        queryGenerator.setTruncation(True)
        resultQueryGenerated = queryGenerator.createQuery(text)
        print("Query", resultQueryGenerated)

        queryExpected = ['    def wires(self):\n', '        """Current wire values.\n', '\n', '        Fixed wires are returned as is, free wires represented by\n', '        :class:`~.variable.Variable` instances are replaced by their\n', '        current numerical value.\n', '\n', '        Returns:\n', '            list[int]: wire values\n', '        """\n', '        <mask>', '        self.check_wires(w)\n', '        return w\n', '\n', '    @property\n', '    def parameters(self):\n', '        """Current parameter values.\n', '\n', '        Fixed parameters are returned as is, free parameters represented by\n', '        :class:`~.variable.Variable` instances are replaced by their\n', '        current numerical value.\n']

        self.assertEqual(queryExpected, resultQueryGenerated)
    
    def test_HFPlBartStandardQuery(self):
        f = open('Tests/resources/input.py', "r")
        text = f.readlines()
        f.close()
        queryGenerator = HFPlBartStandardQuery("<mask>",[4])

        resultQueryGenerated = queryGenerator.createQuery(text)
        print("Query", resultQueryGenerated)

        queryExpected = ['<s> def bitcount(n):\n', '    count = 0\n', '    while n:\n', '        <mask>', '    return count\n', '</s> Python'] 

        self.assertEqual(queryExpected, resultQueryGenerated)

    def test_HFPlBartStandardQueryTruncation(self):
        f = open('Tests/resources/inputQuantum.py', "r")
        text = f.readlines()
        f.close()
        queryGenerator = HFPlBartStandardQuery("<mask>",[374])
        queryGenerator.setTruncation(True)
        resultQueryGenerated = queryGenerator.createQuery(text)
        print("Query", resultQueryGenerated)

        queryExpected = ['<s>     def wires(self):\n', '        """Current wire values.\n', '\n', '        Fixed wires are returned as is, free wires represented by\n', '        :class:`~.variable.Variable` instances are replaced by their\n', '        current numerical value.\n', '\n', '        Returns:\n', '            list[int]: wire values\n', '        """\n', '        <mask>', '        self.check_wires(w)\n', '        return w\n', '\n', '    @property\n', '    def parameters(self):\n', '        """Current parameter values.\n', '\n', '        Fixed parameters are returned as is, free parameters represented by\n', '        :class:`~.variable.Variable` instances are replaced by their\n', '        current numerical value.\n', '</s> Python'] 

        self.assertEqual(queryExpected, resultQueryGenerated)


    def test_HFPlBartHintQuery(self):
        f = open('Tests/resources/input.py', "r")
        text = f.readlines()
        f.close()
        queryGenerator = HFPlBartHintQuery("<mask>",[4],None,[4])

        resultQueryGenerated = queryGenerator.createQuery(text)
        print("Query", resultQueryGenerated)

        queryExpected = ['<s> def bitcount(n):\n', '    count = 0\n', '    while n:\n', '        #buggy line:        count += 1\n', '        <mask>', '    return count\n', '</s> Python'] 

        self.assertEqual(queryExpected, resultQueryGenerated)

    def test_HFPlBartHintQueryTruncation(self):
        f = open('Tests/resources/inputQuantum.py', "r")
        text = f.readlines()
        f.close()
        queryGenerator = HFPlBartHintQuery("<mask>",[374],None,[374])
        queryGenerator.setTruncation(True)
        resultQueryGenerated = queryGenerator.createQuery(text)
        print("Query", resultQueryGenerated)

        queryExpected = ['<s>     def wires(self):\n', '        """Current wire values.\n', '\n', '        Fixed wires are returned as is, free wires represented by\n', '        :class:`~.variable.Variable` instances are replaced by their\n', '        current numerical value.\n', '\n', '        Returns:\n', '            list[int]: wire values\n', '        """\n', '        #buggy line:        w = [i.val if isinstance(i, Variable) else i for i in self._wires]\n', '        <mask>', '        self.check_wires(w)\n', '        return w\n', '\n', '    @property\n', '    def parameters(self):\n', '        """Current parameter values.\n', '\n', '        Fixed parameters are returned as is, free parameters represented by\n', '        :class:`~.variable.Variable` instances are replaced by their\n', '</s> Python']

        self.assertEqual(queryExpected, resultQueryGenerated)


    def test_HFCodeGenStandardQuery(self):
        f = open('Tests/resources/input.py', "r")
        text = f.readlines()
        f.close()
        queryGenerator = HFCodegenStandardQuery(4)

        resultQueryGenerated = queryGenerator.createQuery(text)
        print("Query", resultQueryGenerated)

        queryExpected = ['def bitcount(n):\n', '    count = 0\n', '    while n:\n']

        self.assertEqual(queryExpected, resultQueryGenerated)
    
    def test_HFCodeGenStandardQueryTruncation(self):
        f = open('Tests/resources/inputQuantum.py', "r")
        text = f.readlines()
        f.close()
        queryGenerator = HFCodegenStandardQuery(374)
        queryGenerator.setTruncation(True)
        resultQueryGenerated = queryGenerator.createQuery(text)
        print("Query", resultQueryGenerated)

        queryExpected = ['    def wires(self):\n', '        """Current wire values.\n', '\n', '        Fixed wires are returned as is, free wires represented by\n', '        :class:`~.variable.Variable` instances are replaced by their\n', '        current numerical value.\n', '\n', '        Returns:\n', '            list[int]: wire values\n', '        """\n']

        self.assertEqual(queryExpected, resultQueryGenerated)

    def test_HFCodeGenHintQuery(self):
        f = open('Tests/resources/input.py', "r")
        text = f.readlines()
        f.close()
        queryGenerator = HFCodegenHintQuery(4)

        resultQueryGenerated = queryGenerator.createQuery(text)
        print("Query", resultQueryGenerated)

        queryExpected = ['def bitcount(n):\n', '    count = 0\n', '    while n:\n', '        #buggy line:        count += 1\n']

        self.assertEqual(queryExpected, resultQueryGenerated)

    def test_HFCodeGenHintQueryTruncation(self):
        f = open('Tests/resources/inputQuantum.py', "r")
        text = f.readlines()
        f.close()
        queryGenerator = HFCodegenHintQuery(374)
        queryGenerator.setTruncation(True)
        resultQueryGenerated = queryGenerator.createQuery(text)
        print("Query", resultQueryGenerated)

        queryExpected = ['    def wires(self):\n', '        """Current wire values.\n', '\n', '        Fixed wires are returned as is, free wires represented by\n', '        :class:`~.variable.Variable` instances are replaced by their\n', '        current numerical value.\n', '\n', '        Returns:\n', '            list[int]: wire values\n', '        """\n', '        #buggy line:        w = [i.val if isinstance(i, Variable) else i for i in self._wires]\n']

        self.assertEqual(queryExpected, resultQueryGenerated)

if __name__ == '__main__':
    unittest.main()


