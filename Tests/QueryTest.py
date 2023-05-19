import unittest
from Pipeline.Query_Creation import *
class QueryTestCase(unittest.TestCase):
    def test_HFHintQuery(self):
        queryGenerator = HFHintQuery()
        f = open('./resources/input.py', "r")
        text = f.readlines()
        f.close()
        queryGenerator.setPlaceholder("<mask>")
        queryGenerator.setLinesAddHint([3])
        resultQueryGenerated = queryGenerator.createQuery(text)
        print("Query", resultQueryGenerated)

        queryExpected = "<TODO>"  ## TODO: here to write the query that we expect

        self.assertEqual(queryExpected, resultQueryGenerated)

        self.assertEqual(True, False)  # add assertion here

    def test_HFStandardQuery(self):
        f = open('./resources/input.py', "r")
        text = f.readlines()
        f.close()
        queryGenerator = HFStandardQuery()
        queryGenerator.setPlaceholder("<mask>")
        queryGenerator.setLinesAddPlaceholder([4])

        resultQueryGenerated = queryGenerator.createQuery(text)
        print("Query", resultQueryGenerated)

        queryExpected = "<TODO>" ## TODO: here to write the query that we expect

        self.assertEqual(queryExpected, resultQueryGenerated)

if __name__ == '__main__':
    unittest.main()


