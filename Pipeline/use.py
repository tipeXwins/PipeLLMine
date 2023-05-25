import os
from Calls import HFCodeGenController, HFCodeT5Controller, HFIncoderController, HFPlBartController, OAICommunicationController
from Comparison import Comparer, ComparerNLTKCodeBleu
from Diff_Info_extraction import obtainInfoLines
from Filtering import Filter
from Query_Creation import HFHintQuery, HFStandardQuery, OAIHintQuery, OAIStandardQuery
from CodeInformation import CodeInformation

from dotenv import load_dotenv
load_dotenv()

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-d","--dataset", type=str, help="specify the dataset you want to use")
parser.add_argument("-b","--buggy", type=str, help="specify the path of the buggy codes")
parser.add_argument("-c","--correct", type=str, help="specify the path of the correct codes")
parser.add_argument("-u","--unidiffs", type=str, help="specify the path of the uniDiffs")
parser.add_argument("-fm","--filtermod", type=str, help="specify the max number of lines modified for filter codes from uniDiffs")
parser.add_argument("-fa","--filteradd", type=str, help="specify the max number of lines added for filter codes from uniDiffs")
parser.add_argument("-fr","--filterrem", type=str, help="specify the max number of lines removed for filter codes from uniDiffs")
parser.add_argument("-m","--model", type=str, help="specify the model you want to use")
parser.add_argument("-q","--query", type=str, help="specify the query you want to use")
parser.add_argument("-e","--evaluationmetric",type=str, help="specify the evaluation metric you want to use")

args = parser.parse_args()

def createFullPath(dirPath,file):
    fullPath = dirPath +  "/" + file
    return fullPath
def IterateDirectoryFiles(dirPath):
    files = []
    for path in os.listdir(dirPath):
        # check if current path is a file
        if os.path.isfile(os.path.join(dirPath, path)):
            files.append(path)
    return files
def readFiles(dirPath,filesNames):
    filesContent = []
    for file in filesNames :
        fullPath = createFullPath(dirPath,file)
        f = open(fullPath, "r")
        text = f.read()
        filesContent.append([fullPath,text])
        f.close()
    return filesContent
def readFile(dirPath,fileName):
    fullPath = createFullPath(dirPath,fileName)
    f = open(fullPath, "r")
    text = f.readlines()
    
    f.close()
    return text
#Models available
OpenAI = "OpenAI"
PlBart = "PlBart"
CodeT5 = "CodeT5"
CodeGen = "CodeGen"
Incoder = "Incoder"

#Query Strategies
Standard = "Standard"
Hint = "Hint"
def noModelsSelected():
    print("No models specified, models available on pipeline:")
    print(OpenAI)
    print(PlBart)
    print(CodeT5)
    print(CodeGen)
    print(Incoder)


if __name__ == '__main__':

    #print(IterateDirectoryFiles("/home/tipex/TFG/TFG-LMBugFixing/Codes/QuixBugs/BuggyCodes/")) # returns name of file only
    #Path with the codes
    dir_path_buggy_codes = ""
    dir_path_correct_codes = ""
    dir_path_unidiffs = ""
    if not args.dataset: 
        if args.buggy:
            dir_path_buggy_codes = args.buggy 
        else:
            dir_path_buggy_codes = "../Codes/QuixBugs/BuggyCodes"     
    
        if args.correct:
            dir_path_correct_codes = args.correct 
        else:
            dir_path_correct_codes = "../Codes/QuixBugs/CorrectCodes"   

        if args.unidiffs:
            dir_path_unidiffs =  args.unidiffs
        else:
            dir_path_unidiffs = "../PruebasUse/Unidiffs"
         
    else :
        if (args.dataset == "QuixBugs"):
            dir_path_buggy_codes = "../Codes/QuixBugs/BuggyCodes" 
            dir_path_correct_codes = "../Codes/QuixBugs/CorrectCodes" 
            dir_path_unidiffs = "../PruebasUse/Unidiffs"
        elif (args.dataset == "Quantum"):
            dir_path_buggy_codes = ""
            dir_path_correct_codes = ""
            dir_path_unidiffs = "../PruebasUse/Unidiffs"
        else:
            print("This Dataset does not exist in the Pipeline. Skipping")
        
              
         
    
    
    
    
    buggyCodes = []
    correctCodes = []
    totalCorreclyRepair = totalIncorrectlyRepair = 0

    #filesNamesBuggyCode = IterateDirectoryFiles(dir_path_buggy_codes)
    #filesNamesCorrectCode = IterateDirectoryFiles(dir_path_correct_codes)
    filesNamesUniDiffs = IterateDirectoryFiles(dir_path_unidiffs)

    maxModifiedLines = 10
    maxAddedLines = 10
    maxRemovedLines = 10
    if args.filtermod:
        maxModifiedLines = args.filtermod
    if args.filteradd:
        maxAddedLines = args.filteradd
    if args.filterrem:
        maxRemovedLines = args.filterrem

    
    

    filter = Filter()
    filter.setMaxLines(maxModifiedLines, maxAddedLines, maxRemovedLines)
    acceptedCodes = []
    for fileName in filesNamesUniDiffs:
        fullPath = createFullPath(dir_path_unidiffs, fileName)
        addedLines = obtainInfoLines(dirPath=fullPath,mode=1)
        removedLines = obtainInfoLines(dirPath=fullPath,mode=2)
        modifiedLines= obtainInfoLines(dirPath=fullPath,mode=3)
        if (filter.filter(modifiedLines, addedLines, removedLines)):
            acceptedCodes.append([fileName,modifiedLines])



    ###CREATE QUERIES
    QueryCreators = []
    if args.model:
        if args.model == OpenAI:
            if args.query:
                if args.query == Standard:
                    QueryCreators.append(OAIStandardQuery())
                elif args.query == Hint:
                    QueryCreators.append(OAIHintQuery())
            else:
                QueryCreators.append(OAIStandardQuery())
                QueryCreators.append(OAIHintQuery())
        elif args.model == PlBart:
            if args.query:
                if args.query == Standard:
                    StandardQuery = HFStandardQuery()
                    QueryCreators.append(StandardQuery)
                elif args.query == Hint:
                    HintQuery = HFHintQuery()
                    QueryCreators.append(HintQuery)
            else:
                StandardQuery = HFStandardQuery()
                QueryCreators.append(StandardQuery)
                HintQuery = HFHintQuery()
                QueryCreators.append(HintQuery)
        elif args.model == CodeT5:
            if args.query:
                if args.query == Standard:
                    StandardQuery = HFStandardQuery()
                    QueryCreators.append(StandardQuery)
                elif args.query == Hint:
                    HintQuery = HFHintQuery()
                    QueryCreators.append(HintQuery)
            else:
                StandardQuery = HFStandardQuery()
                QueryCreators.append(StandardQuery)
                HintQuery = HFHintQuery()
                QueryCreators.append(HintQuery)
        elif args.model == CodeGen:
            if args.query:
                if args.query == Standard:
                    StandardQuery = HFStandardQuery()
                    QueryCreators.append(StandardQuery)
                elif args.query == Hint:
                    HintQuery = HFHintQuery()
                    QueryCreators.append(HintQuery)
            else:
                StandardQuery = HFStandardQuery()
                QueryCreators.append(StandardQuery)
                HintQuery = HFHintQuery()
                QueryCreators.append(HintQuery)
        elif args.model == Incoder:
            if args.query:
                if args.query == Standard:
                    StandardQuery = HFStandardQuery()
                    QueryCreators.append(StandardQuery)
                elif args.query == Hint:
                    HintQuery = HFHintQuery()
                    QueryCreators.append(HintQuery)
            else:
                StandardQuery = HFStandardQuery()
                QueryCreators.append(StandardQuery)
                HintQuery = HFHintQuery()
                QueryCreators.append(HintQuery)



    else:
        noModelsSelected()
    Codes = []


    for acceptedCodeName in acceptedCodes:
        acceptedCodePath = createFullPath(dir_path_buggy_codes, acceptedCodeName[0])
        correctCodePath = createFullPath(dir_path_correct_codes, acceptedCodeName[0])
        buggyCodeContent = readFile(dir_path_buggy_codes, acceptedCodeName[0]).copy()
        correctCodeContent = readFile(dir_path_correct_codes, acceptedCodeName[0]).copy()
        acceptedCodeInformation = CodeInformation(buggyCodeContent, correctCodeContent)
        buggyCode = buggyCodeContent.copy()
        for QueryCreator in QueryCreators:
            acceptedCodeInformation.addQuery(QueryCreator.createQuery(buggyCode))

        Codes.append(acceptedCodeInformation)



        ###MAKE CALLS
        if args.model:
            if args.model == OpenAI:
                ModelCommunicator = OAICommunicationController()
                ModelCommunicator.setApiKey(os.getenv("OAIKey"))
            elif args.model == PlBart:
                if args.ret_seq:
                    ModelCommunicator = HFPlBartController(args.ret_seq)
                else:
                    ModelCommunicator = HFPlBartController()
            elif args.model == CodeT5:
                if args.ret_seq:
                    ModelCommunicator = HFCodeT5Controller(args.ret_seq)
                else:
                    ModelCommunicator = HFCodeT5Controller()
            elif args.model == CodeGen:
                if args.ret_seq:
                    ModelCommunicator = HFCodeGenController(args.ret_seq)
                else:
                    ModelCommunicator = HFCodeGenController()
            elif args.model == Incoder:
                if args.ret_seq:
                    ModelCommunicator = HFIncoderController(args.ret_seq)
                else:
                    ModelCommunicator = HFIncoderController()
        else: 
            noModelsSelected()


        
        for codeInformation in Codes:
                for query in codeInformation.queries:

                    acceptedCodeInformation.addResponse(ModelCommunicator.callToModel("".join(query)))

        ###MAKE COMPARISONS

        comparer = ComparerNLTKCodeBleu()
        for codeInformation in Codes:
                correctCodeContent = codeInformation.correctCodeContent
                for response in codeInformation.responses:
                     print(comparer.compare(response, correctCodeContent))
