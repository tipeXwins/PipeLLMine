import unittest

from Pipeline.Calls import HFPlBartController


class ModelControllerTest(unittest.TestCase):

    def testLoadModelInConstructor(self):

        aLLM = HFPlBartController()
        self.assertTrue(aLLM.tokenizer != None)
        print("tokenizer", aLLM.tokenizer )
        self.assertTrue(aLLM.model != None)
        print("model", aLLM.model)

    def test_Model(self):

        #TO BE REFACTORED
        ## This is for testing this pipeline module

        f = open('../Tests/plbartQuery.py', "r")
        queryBart = f.read()
        f.close()

        ### Do the calls with the respective query
        # Output will be writed on outputHFModel.txt on Test folder

        comunicatorBart = HFPlBartController()  # Return full code one string
        print("Bart", comunicatorBart.callToModelWithTransformers("".join(queryBart)))

        # TODO ADD assessment

        self.assertEqual(True, False)  # add assertion here

    def otherToRefactor(self):
        # TODO: one test per Model

        ### READ QUERIES


        f = open('../Tests/codet5Query.py', "r")
        queryCodeT5 = f.read()
        f.close()

        f = open('../Tests/codegenQuery.py', "r")
        queryCodeGen = f.read()
        f.close()

        f = open('../Tests/incoderQuey.py', "r")
        queryInCoder = f.read()
        f.close()



        """
        comunicatorCodeT5 =  HFCodeT5Controller() # return only snipets of code where specified and vector of string with lines
        print("CodeT5",comunicatorCodeT5.callToModelWithTransformers("".join(queryCodeT5)))

        comunicatorIncoder =  HFIncoderController() # Complexx queries and vectors of full results but strange ones
        print("Incoder",comunicatorIncoder.callToModelWithTransformers("".join(queryInCoder)))

        comunicatorCodeGen =  HFCodeGenController() #gives 4 responses with full code try to se if every output is a result
        print("CodeGen",comunicatorCodeGen.callToModelWithTransformers("".join(queryCodeGen)))

        """

if __name__ == '__main__':
    unittest.main()
