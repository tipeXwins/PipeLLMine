"""
class QueryCreator:
    def createQuery(self,originPath, finalPath):
        pass
    

class OAIStandardQuery(QueryCreator):
    def addOAILabels(self,content):
        
        #Add at file start the necessary content
        content.insert(0,"##### Fix bugs in the below function  \n")
        content.insert(1,"\n")
        content.insert(2,"### Buggy Python \n")

        #Add at the end the necesary content
        content.append("\n")
        content.append("### Fixed Python \n")
        content.append("\n")
        
    def createQuery(self,originPath, finalPath):
        file = open(originPath,'r')
        content = file.readlines()
        self.addOAILabels(content)
        file.close()
        file = open(finalPath,'w') # open as write mode and write the new content here
        file.writelines(content)
        file.close()

class OAIHintQuery(OAIStandardQuery):
    hint = "Buggy"
    linesAddHint= []

    def setHint(self,hint):
        self.hint = hint
    def setLinesAddHint(self,linesAdd):
        self.linesAddHint = linesAdd
    def includeHint(self,content,pointModified,hint):
        for point in pointModified:
            line = content[point]
            content[point] = line[:len(line)-1] +"#" + hint + "\n"
    def createQuery(self, originPath, finalPath): #before calling createQuery we have to set the lines
        file = open(originPath,'r')
        content = file.readlines()
        file.close()
        self.includeHint(content,self.linesAddHint,self.hint)
        self.addOAILabels(content)
        file = open(finalPath,'w') # open as write mode and write the new content here
        file.writelines(content)
        file.close()
        
  

        
        
hola = OAIHintQuery()
hola.setLinesAddHint([2,3])
hola.createQuery('/home/tipex/TFG/TFG-LMBugFixing/Codes/QuixBugs/BuggyCodes/bitcount.py','/home/tipex/TFG/TFG-LMBugFixing/bitcountmodification2.py')
"""


class QueryCreator:
    def createQuery(self,content):
        pass
    

class OAIStandardQuery(QueryCreator):
    def addOAILabels(self,content):
        
        #Add at file start the necessary content
        content.insert(0,"##### Fix bugs in the below function  \n")
        content.insert(1,"\n")
        content.insert(2,"### Buggy Python \n")

        #Add at the end the necesary content
        content.append("\n")
        content.append("### Fixed Python \n")
        content.append("\n")
        
    def createQuery(self,content):
        self.addOAILabels(content)
        return content
        
class OAIHintQuery(OAIStandardQuery):
    hint = "Buggy"
    linesAddHint= []

    def setHint(self,hint):
        self.hint = hint
    def setLinesAddHint(self,linesAdd):
        self.linesAddHint = linesAdd
    def includeHint(self,content,pointModified,hint):
        for point in pointModified:
            line = content[point]
            content[point] = line[:len(line)-1] +" #" + hint + "\n"
            
    def createQuery(self, content): #before calling createQuery we have to set the lines
        
        self.includeHint(content,self.linesAddHint,self.hint)
        self.addOAILabels(content)
        return content



class HFStandardQuery(QueryCreator):
    placeholder = ""
    linesAddPlaceholder = []
    def setPlaceholder(self,placeholder):
        self.placeholder = placeholder
    def setLinesAddPlaceholder(self,linesAdd):
        self.linesAddPlaceholder = linesAdd
    def deleteBuggyLines(self,content,pointModified):
        for point in pointModified:
            content[point-1] = "" #line behind
    def includePlaceholder(self,content,pointModified,placeholder):
        for point in pointModified:
            buggyline = content[point-1]
            print("buggy",buggyline)
            print(len(buggyline))
            print(buggyline.strip())
            indentation = buggyline[:len(buggyline)-len(buggyline.strip())-5]
            content.insert(point,indentation + placeholder) #line behind
    def createQuery(self, content): #before calling createQuery we have to set the lines  
        
        self.includePlaceholder(content,self.linesAddPlaceholder,self.placeholder)
        self.deleteBuggyLines(content,self.linesAddPlaceholder)  
        return content
    
class HFHintQuery(HFStandardQuery):
    hint = "buggy line:"
    linesAddHint = []

    def setHint(self,hint):
        self.hint = hint
    def setLinesAddHint(self,linesAdd):
        self.linesAddHint = linesAdd
    def includeHint(self,content,pointModified,hint):
        for point in pointModified:
            line = content[point]
            indentation = line[:len(line)-len(line.strip())-5]
            content[point] = indentation + "#" + hint + line
            
    def createQuery(self, content): #before calling createQuery we have to set the lines    
        self.includeHint(content,self.linesAddHint,self.hint)
        self.includePlaceholder(content,[self.linesAddHint[0]+1],self.placeholder)
        return content

    
## This is for testing this pipeline module
buggy =  HFHintQuery()
f = open('../Tests/input.py', "r")
text = f.readlines()
buggy.setPlaceholder("<mask>")
buggy.setLinesAddHint([3])
text = buggy.createQuery(text)
print(text)
f.close()

f = open('../Tests/input.py', "r")
text = f.readlines()
comunicator =  HFStandardQuery()
comunicator.setPlaceholder("<mask>")
comunicator.setLinesAddPlaceholder([4])
print(comunicator.createQuery(text))
f.close()


