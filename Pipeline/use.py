import os
from Calls import OAICommunicationController
from Comparison import Comparer, ComparerNLTKCodeBleu
from Diff_Info_extraction import obtainInfoLines
from Filtering import Filter
from Query_Creation import OAIHintQuery, OAIStandardQuery
from CodeInformation import CodeInformation

from dotenv import load_dotenv
load_dotenv()

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-d","--dataset", type=str, help="specify the dataset you want to uset")
parser.add_argument("-f","--filter", type=str, help="specify the filter you want to uset")
parser.add_argument("-m","--model", type=str, help="specify the model you want to uset")
parser.add_argument("-q","--query", type=str, help="specify the query you want to uset")
parser.add_argument("-e","--evaluationmetric",type=str, help="specify the evaluation metric you want to uset")

args = parser.parse_args()
if args.verbosity:
    print("verbosity turned on")


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


if __name__ == '__main__':

    #print(IterateDirectoryFiles("/home/tipex/TFG/TFG-LMBugFixing/Codes/QuixBugs/BuggyCodes/")) # returns name of file only
    #Path with the codes

    ###CREATE RELATIVE PATHS
    dir_path_buggy_codes = "../Codes/QuixBugs/BuggyCodes" #pasar por parametro
    dir_path_correct_codes = "../Codes/QuixBugs/CorrectCodes" # esto igual   # mirar librerias para hacer unified diffs y  librerias que te leen los difss directamente
    dir_path_unidiffs = "../PruebasUse/Unidiffs"
    buggyCodes = []
    correctCodes = []
    totalCorreclyRepair = totalIncorrectlyRepair = 0

    #filesNamesBuggyCode = IterateDirectoryFiles(dir_path_buggy_codes)
    #filesNamesCorrectCode = IterateDirectoryFiles(dir_path_correct_codes)
    filesNamesUniDiffs = IterateDirectoryFiles(dir_path_unidiffs)

    maxModifiedLines = 10
    maxAddedLines = 10
    maxRemovedLines = 10

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

    OAIStandardQueryCreator = OAIStandardQuery()
    OAIHintQueryCreator = OAIHintQuery()
    #OAIHintQueryCreator.setHint("Something Wrong Happened")
    Codes = []


    for acceptedCodeName in acceptedCodes:
        acceptedCodePath = createFullPath(dir_path_buggy_codes, acceptedCodeName[0])
        correctCodePath = createFullPath(dir_path_correct_codes, acceptedCodeName[0])
        buggyCodeContent = readFile(dir_path_buggy_codes, acceptedCodeName[0]).copy()
        correctCodeContent = readFile(dir_path_correct_codes, acceptedCodeName[0]).copy()
        acceptedCodeInformation = CodeInformation(buggyCodeContent, correctCodeContent)
        contentQuery1 = buggyCodeContent.copy()
        contentQuery2 =buggyCodeContent.copy()
        acceptedCodeInformation.addQuery(OAIStandardQueryCreator.createQuery(contentQuery1))
        OAIHintQueryCreator.setLinesAddHint(acceptedCodeName[1][0][1])
        acceptedCodeInformation.addQuery(OAIHintQueryCreator.createQuery(contentQuery2))

        Codes.append(acceptedCodeInformation)



        ###MAKE CALLS

        OAICommunicator = OAICommunicationController()
        print(os.getenv("OAIKey"),"bones")
        OAICommunicator.setApiKey(os.getenv("OAIKey"))
        #OAICommunicator.setApiKey("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")
        #hyperparameters = []
        #OAICommunicator.setHyperparameters(hyperparameters)
        #OAICommunicator.setModel("")
        for codeInformation in Codes:
                for query in codeInformation.queries:

                    acceptedCodeInformation.addResponse(OAICommunicator.callToModel("".join(query)))

        ###MAKE COMPARISONS

        comparer = ComparerNLTKCodeBleu()
        for codeInformation in Codes:
                correctCodeContent = codeInformation.correctCodeContent
                for response in codeInformation.responses:
                     print("ojito", response)
                     print(comparer.compare(response, correctCodeContent))
