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