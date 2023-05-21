
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

    



