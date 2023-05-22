import unittest
#from Pipeline.Query_Creation import *
from Pipeline.use import readFile
from Pipeline.Query_Creation import HFHintQuery, HFPlBartStandardQuery, HFStandardQuery, OAIHintQuery

class QueryTestCase(unittest.TestCase):
    def test_HFHintQuery(self):
        queryGenerator = HFHintQuery("<mask>",[3],None,[3])
        f = open('Tests/resources/input.py', "r")
        text = f.readlines()
        f.close()
        resultQueryGenerated = queryGenerator.createQuery(text)
        print("Query", resultQueryGenerated)

        queryExpected = "<TODO>"  ## TODO: here to write the query that we expect

        self.assertEqual(queryExpected, resultQueryGenerated)

        self.assertEqual(True, False)  # add assertion here

    def test_HFStandardQuery(self):
        f = open('Tests/resources/input.py', "r")
        text = f.readlines()
        f.close()
        queryGenerator = HFStandardQuery()
        queryGenerator.setPlaceholder("<mask>")
        queryGenerator.setLinesAddPlaceholder([4])

        resultQueryGenerated = queryGenerator.createQuery(text)
        print("Query", resultQueryGenerated)

        queryExpected = "<TODO>" ## TODO: here to write the query that we expect

        self.assertEqual(queryExpected, resultQueryGenerated)
    
    def test_HFPlBartStandardQuery(self):
        f = open('Tests/resources/input.py', "r")
        text = f.readlines()
        f.close()
        queryGenerator = HFPlBartStandardQuery("<mask>",[4])

        resultQueryGenerated = queryGenerator.createQuery(text)
        print("Query", resultQueryGenerated)

        queryExpected = ['<s> def bitcount(n):\n', '    count = 0\n', '    while n:\n', '', '    <mask>', '    return count\n', '</s> Python'] 

        self.assertEqual(queryExpected, resultQueryGenerated)

    def test_OpenAIQuery(self):
        print("Init test")
        hola = OAIHintQuery()
        hola.setLinesAddHint([2, 3])

        #file = readFile('../Codes/QuixBugs/BuggyCodes/', 'bitcount.py')
        #queryGenerated = hola.createQuery(file)

    def test_init(self):
        print("init")

if __name__ == '__main__':
    unittest.main()


