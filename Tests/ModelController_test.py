import unittest


from Pipeline.Calls import HFCodeGenController, HFCodeT5Controller, HFIncoderController, HFPlBartController


class ModelControllerTest(unittest.TestCase):

    def test_Bart_LoadModelInConstructor(self):

        aLLM = HFPlBartController()
        self.assertTrue(aLLM.tokenizer != None)
        print("tokenizer", aLLM.tokenizer )
        self.assertTrue(aLLM.model != None)
        print("model", aLLM.model)

    def test_Codet5_LoadModelInConstructor(self):

        aLLM = HFCodeT5Controller()
        self.assertTrue(aLLM.tokenizer != None)
        print("tokenizer", aLLM.tokenizer )
        self.assertTrue(aLLM.model != None)
        print("model", aLLM.model)

    def test_CodeGen_LoadModelInConstructor(self):

        aLLM = HFCodeGenController()
        self.assertTrue(aLLM.tokenizer != None)
        print("tokenizer", aLLM.tokenizer )
        self.assertTrue(aLLM.model != None)
        print("model", aLLM.model)
    
    def test_Incoder_LoadModelInConstructor(self):

        aLLM = HFIncoderController()
        self.assertTrue(aLLM.tokenizer != None)
        print("tokenizer", aLLM.tokenizer )
        self.assertTrue(aLLM.model != None)
        print("model", aLLM.model)

    def test_Bart_Model(self):

        f = open('Tests/resources/inputs/plbartQuery.py', "r")
        queryBart = f.read()
        f.close()

        comunicatorBart = HFPlBartController()  # Return full code one string
        output = comunicatorBart.callToModelWithTransformers("".join(queryBart))

        with open('Tests/resources/outputs/outputBart.txt', 'w') as file:
            file.writelines(output)

        # TODO ADD assessment

        self.assertEqual(True, True)  # add assertion here
    
    def test_Codet5_Model(self):

        f = open('Tests/resources/inputs/codet5Query.py', "r")
        queryCodet5 = f.read()
        f.close()

        comunicatorCodet5 = HFCodeT5Controller()  # Return full code one string
        output = comunicatorCodet5.callToModelWithTransformers("".join(queryCodet5))

        with open('Tests/resources/outputs/outputCodeT5.txt', 'w') as file:
            file.writelines(output)

        # TODO ADD assessment

        self.assertEqual(True, True)  # add assertion here
    
    def test_CodeGen_Model(self):

        f = open('Tests/resources/inputs/codegenQuery.py', "r")
        queryCodetGen = f.read()
        f.close()

        comunicatorCodeGen= HFCodeGenController()  # Return full code one string
        output = comunicatorCodeGen.callToModelWithTransformers("".join(queryCodeGen))

        with open('Tests/resources/outputs/outputCodeGen.txt', 'w') as file:
            file.writelines(output)

        # TODO ADD assessment

        self.assertEqual(True, True)  # add assertion here

    def test_Incoder_Model(self):

        f = open('Tests/resources/inputs/incoderQuery.py', "r")
        queryIncoder = f.read()
        f.close()

        comunicatorIncoder= HFIncoderController()  # Return full code one string
        output = comunicatorIncoder.callToModelWithTransformers("".join(queryIncoder))

        with open('Tests/resources/outputs/outputIncoder.txt', 'w') as file:
            file.writelines(output)

        # TODO ADD assessment

        self.assertEqual(True, True)  # add assertion here

    

if __name__ == '__main__':
    unittest.main()
