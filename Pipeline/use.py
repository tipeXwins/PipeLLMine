import os
from Calls import HFCodeGenController, HFCodeT5Controller, HFIncoderController, HFPlBartController, OAICommunicationController
from Comparison import Comparer, ComparerNLTKCodeBleu, MultipleComparerNLTKCodeBleu
from Diff_Info_extraction import obtainInfoLines
from Filtering import Filter
from OutputReconstructor import ReconstructorPatch
from Query_Creation import HFCodegenHintQuery, HFCodegenStandardQuery, HFHintQuery, HFPlBartHintQuery, HFPlBartStandardQuery, HFStandardQuery, OAIHintQuery, OAIStandardQuery
from CodeInformation import CodeInformation

from dotenv import load_dotenv
load_dotenv()

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-d","--dataset", type=str, help="specify the dataset you want to use")
parser.add_argument("-b","--buggy", type=str, help="specify the path of the buggy codes")
parser.add_argument("-c","--correct", type=str, help="specify the path of the correct codes")
parser.add_argument("-u","--unidiffs", type=str, help="specify the path of the uniDiffs")
parser.add_argument("-fm","--filtermod", type=int, help="specify the max number of lines modified for filter codes from uniDiffs")
parser.add_argument("-fa","--filteradd", type=int, help="specify the max number of lines added for filter codes from uniDiffs")
parser.add_argument("-fr","--filterrem", type=int, help="specify the max number of lines removed for filter codes from uniDiffs")
parser.add_argument("-m","--model", type=str, help="specify the model you want to use")
parser.add_argument("-q","--query", type=str, help="specify the query you want to use")
parser.add_argument("-e","--evalmet",type=str, help="specify the evaluation metric you want to use")
parser.add_argument("-rs","--retseq", type=int, help="specify the number of results expected to be returned from the model")

args = parser.parse_args()
def listArgs():
    print("Args List:")
    if args.dataset:
        print("dataset: ", args.dataset)
    if args.buggy:
        print("buggy: ", args.buggy)
    if args.correct:
        print("correct: ", args.correct)
    if args.unidiffs:
        print("unidiffs: ", args.unidiffs)
    
    if args.filtermod:
        print("filtermod: ", args.filtermod)
    if args.filteradd:
        print("filteradd: ", args.filteradd)
    if args.correct:
        print("filterrem: ", args.filterrem)
    if args.model:
        print("model: ", args.model)
    if args.query:
        print("query: ", args.query)
    if args.evalmet:
        print("evalmet: ", args.evalmet)
    if args.retseq:
        print("retseq: ", args.retseq)
    


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
    listArgs()

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
            dir_path_buggy_codes = "../Codes/QuixBugsNo/BuggyCodes" 
            dir_path_correct_codes = "../Codes/QuixBugsNo/CorrectCodes" 
            dir_path_unidiffs = "../Codes/QuixBugsNo/UniDiffs"
        elif (args.dataset == "Quantum"):
            dir_path_buggy_codes = "../Codes/Quantum-Computing-Platforms/BuggyCodes"
            dir_path_correct_codes = "../Codes/Quantum-Computing-Platforms/CorrectCodes"
            dir_path_unidiffs = "../Codes/Quantum-Computing-Platforms/BuggyCodes"
        elif (args.dataset == "Tests"):
            dir_path_buggy_codes = "../Codes/QuixBugs/BuggyCodes"
            dir_path_correct_codes = "../Codes/QuixBugs/CorrectCodes" 
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
        if addedLines:
            numAddedLines = len(addedLines[0][1])
        else:
            numAddedLines = 0
        if removedLines:
            numRemovedLines = len(removedLines[0][1])
        else:
            numRemovedLines = 0
        if modifiedLines:
            numModifiedLines = len(modifiedLines[0][1])
        else:
            numModifiedLines = 0
            modifiedLines = [[args.dataset + "/"+fileName,[]]]

        
        print(fileName,numModifiedLines, numAddedLines, numRemovedLines)
        if (filter.filter( numModifiedLines, numAddedLines, numRemovedLines)):
            
            
            acceptedCodes.append([fileName,modifiedLines])
            #modifiedLines example: modified lines before assignation [['BuggyCodes/breadth_first_search.py', [32, 33, 11, 25, 28, 29, 30]]]



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
                    StandardQuery = HFPlBartStandardQuery("<mask>")
                    QueryCreators.append([StandardQuery,"hg"])
                elif args.query == Hint:
                    HintQuery = HFPlBartHintQuery("<mask>")
                    QueryCreators.append([HintQuery, "hgHint"])
            else:
                StandardQuery = HFPlBartStandardQuery("<mask>")
                QueryCreators.append([StandardQuery,"hg"])
                HintQuery = HFPlBartHintQuery("<mask>")
                QueryCreators.append([HintQuery, "hgHint"])
                
        elif args.model == CodeT5:
            if args.query:
                if args.query == Standard:
                    StandardQuery = HFStandardQuery("<extra_id_0>")
                    QueryCreators.append([StandardQuery,"hg"])
                elif args.query == Hint:
                    HintQuery = HFHintQuery("<extra_id_0>")
                    QueryCreators.append([HintQuery, "hgHint"])
            else:
                StandardQuery = HFStandardQuery("<extra_id_0>")
                QueryCreators.append([StandardQuery,"hg"])
                HintQuery = HFHintQuery("<extra_id_0>")
                QueryCreators.append([HintQuery, "hgHint"])
        elif args.model == CodeGen:
            if args.query:
                if args.query == Standard:
                    StandardQuery = HFCodegenStandardQuery()
                    QueryCreators.append([StandardQuery,"hgTail"])
                elif args.query == Hint:
                    HintQuery = HFCodegenHintQuery()
                    QueryCreators.append([HintQuery, "hgTail"])
            else:
                StandardQuery = HFCodegenStandardQuery()
                QueryCreators.append([StandardQuery,"hgTail"])
                HintQuery = HFCodegenHintQuery()
                QueryCreators.append([HintQuery, "hgTail"])
        elif args.model == Incoder:
            if args.query:
                if args.query == Standard:
                    StandardQuery = HFStandardQuery()
                    QueryCreators.append([StandardQuery,"hg"])
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


    for acceptedCodeNameInstance in acceptedCodes:
        acceptedCodeName = acceptedCodeNameInstance[:]
        acceptedCodePath = createFullPath(dir_path_buggy_codes, acceptedCodeName[0])
        correctCodePath = createFullPath(dir_path_correct_codes, acceptedCodeName[0])
        buggyCodeContent = readFile(dir_path_buggy_codes, acceptedCodeName[0]).copy()
        correctCodeContent = readFile(dir_path_correct_codes, acceptedCodeName[0]).copy()
        acceptedCodeInformation = CodeInformation(buggyCodeContent, correctCodeContent)
        buggyCode = buggyCodeContent.copy()
        
        

        for QueryCreator in QueryCreators:
            buggy = buggyCode[:]
            if QueryCreator[1] == "hg":
                QueryCreator[0].setLinesAddPlaceholder(acceptedCodeName[1][0][1])
            elif QueryCreator[1] == "hgHint": 
                QueryCreator[0].setLinesAddPlaceholder(acceptedCodeName[1][0][1])
                QueryCreator[0].setLinesAddHint(acceptedCodeName[1][0][1])
            elif QueryCreator[1] == "hgTail": 
                if len (acceptedCodeName[1][0][1])>0:
                    QueryCreator[0].setLineChanged(acceptedCodeName[1][0][1][0]) 
                else:
                    QueryCreator[0].setLineChanged(0)
            acceptedCodeInformation.addQuery(QueryCreator[0].createQuery(buggy))
        print("acceptedCode", acceptedCodeName[1][0])
        print("acceptedCodeName", acceptedCodeName[1][0][0])
        acceptedCodeInformation.setName(acceptedCodeName[1][0][0])
        #print("queries", acceptedCodeInformation.queries)
        Codes.append(acceptedCodeInformation)



    ###MAKE CALLS
    if args.model:
        if args.model == OpenAI:
            ModelCommunicator = [OAICommunicationController()]
            ModelCommunicator[0].setApiKey(os.getenv("OAIKey"))
        elif args.model == PlBart:
            if args.retseq:
                ModelCommunicator = [HFPlBartController(args.retseq)]
            else:
                ModelCommunicator = [HFPlBartController()]
        elif args.model == CodeT5:
            if args.retseq:
                ModelCommunicator = [HFCodeT5Controller(args.retseq),["patch","<extra_id_0>"]]
            else:
                ModelCommunicator = [HFCodeT5Controller(),["patch","<extra_id_0>"]]
        elif args.model == CodeGen:
            if args.retseq:
                ModelCommunicator = [HFCodeGenController(args.retseq)]
            else:
                ModelCommunicator = [HFCodeGenController()]
        elif args.model == Incoder:
            if args.retseq:
                ModelCommunicator = [HFIncoderController(args.retseq)]
            else:
                ModelCommunicator = [HFIncoderController()]
    else: 
        noModelsSelected()


    for codeInformation in Codes:
        for query in codeInformation.queries:
            queryResponse = query[:]
            if queryResponse !=  [] :
                print("query arrived in response", queryResponse)
                responses = ModelCommunicator[0].callToModel("".join(queryResponse))
                #print("first response before construction", responses[0])
                
                if len(ModelCommunicator) >1:
                    if ModelCommunicator[1][0] == "patch":
                        reconstructor = ReconstructorPatch()
                        responsesReconstructed =[]
                        for response in responses:
                            responsesReconstructed.append(reconstructor.reconstruct("".join(queryResponse),"".join(response),ModelCommunicator[1][1]))
                        responses = responsesReconstructed.copy()
                print("first response", responses[0])
                codeInformation.addResponse(responses)

    
        
    ###MAKE COMPARISONS

    comparer = MultipleComparerNLTKCodeBleu()
    count = 0
    for codeInformation in Codes:
        count += 1
        correctCodeContent = codeInformation.correctCodeContent
        countInner = 0
        query= ""
        if  args.query: 
            query = args.query
        for responses in codeInformation.responses:
            print("buenas", codeInformation.name.split("/")[1])
            countInner += 1
            if countInner == 1:
                query = Standard
            elif countInner == 2:
                query = Hint
            
            

            with open('../Results/Output/' + args.dataset + '/' + args.model +'/' + codeInformation.name.split("/")[1] +" Strategy: "+ query +".txt", 'w') as file:
                file.writelines(responses)
                
            with open('../Results/Metrics/' + args.dataset + '/' + args.model +'/'  + codeInformation.name.split("/")[1] +" Strategy: "+ query +".txt", 'w') as file:
                file.writelines("metrics \n" +str(comparer.compareMultipleOutputs(responses,correctCodeContent)))
            """
            for response in responses:
                print(comparer.compare(response, correctCodeContent))
            """
