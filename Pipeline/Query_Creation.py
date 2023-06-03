
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
    def __init__(self, placeholder=None, linesAddPlaceholder=None):
        if (placeholder is None):
            self.placeholder = ""
        else :
            self.placeholder = placeholder
        if (linesAddPlaceholder is None):
            self.linesAddPlaceholder = []
        else:
            self.linesAddPlaceholder = linesAddPlaceholder
    def setPlaceholder(self,placeholder):
        self.placeholder = placeholder
    def setLinesAddPlaceholder(self,linesAdd):
        self.linesAddPlaceholder = linesAdd
    def deleteBuggyLines(self,content,pointModified):
        for point in pointModified:
            content_start = content[:point-1]
            content_end = content[point:]
            content = (content_start + content_end)
        return content
    def includePlaceholder(self,content,pointModified,placeholder):
        for point in pointModified:
            buggyline = content[point-1]
            indentation = buggyline[:len(buggyline)-len(buggyline.strip())-1]
            content.insert(point,indentation + placeholder) #line behind
        
    def createQuery(self, content): #before calling createQuery we have to set the lines 
        self.includePlaceholder(content,self.linesAddPlaceholder,self.placeholder)
        content = self.deleteBuggyLines(content,self.linesAddPlaceholder) 
        return content
    
class HFHintQuery(HFStandardQuery):
    def __init__(self, placeholder=None, linesAddPlaceholder=None, hint=None, linesAddHint=None):
        if (placeholder is None):
            self.placeholder = ""
        else :
            self.placeholder = placeholder
        if (linesAddPlaceholder is None):
            self.linesAddPlaceholder = []
        else:
            self.linesAddPlaceholder = linesAddPlaceholder
        if (hint is None):
            self.hint = "buggy line:"
        else :
            self.hint = hint
        if (linesAddHint is None):
            self.linesAddHint = []
        else:
            self.linesAddHint = linesAddHint
    def setHint(self,hint):
        self.hint = hint
    def setLinesAddHint(self,linesAdd):
        self.linesAddHint = linesAdd
    def includeHint(self,content,pointModified,hint):
        for point in pointModified:
            print("poimt",point)
            line = content[point-1]
            
            indentation = line[:len(line)-len(line.strip())-1]
            content[point-1] = indentation + "#" + hint + line
        return content   
    def createQuery(self, content): #before calling createQuery we have to set the lines   
        self.includePlaceholder(content,self.linesAddPlaceholder,self.placeholder) 
        self.includeHint(content,self.linesAddHint,self.hint)
        
        return content

class HFPlBartStandardQuery(HFStandardQuery):
    def addSpecialTokens(self,content):
        content[0] = "<s> " + content[0]
        content.append("</s> Python")
    def createQuery(self, content): #before calling createQuery we have to set the lines  
        self.includePlaceholder(content,self.linesAddPlaceholder,self.placeholder)
        content = self.deleteBuggyLines(content,self.linesAddPlaceholder) 
        self.addSpecialTokens(content)
        return content
class HFPlBartHintQuery(HFPlBartStandardQuery,HFHintQuery):
    def __init__(self, placeholder=None, linesAddPlaceholder=None, hint=None, linesAddHint=None):
        if (placeholder is None):
            self.placeholder = ""
        else :
            self.placeholder = placeholder
        if (linesAddPlaceholder is None):
            self.linesAddPlaceholder = []
        else:
            self.linesAddPlaceholder = linesAddPlaceholder
        if (hint is None):
            self.hint = "buggy line:"
        else :
            self.hint = hint
        if (linesAddHint is None):
            self.linesAddHint = []
        else:
            self.linesAddHint = linesAddHint
    def createQuery(self, content): #before calling createQuery we have to set the lines   
        self.includePlaceholder(content,self.linesAddPlaceholder,self.placeholder) 
        self.includeHint(content,self.linesAddHint,self.hint)
        self.addSpecialTokens(content)
        return content
    
class HFCodegenStandardQuery(QueryCreator):
    def __init__(self, lineChanged=None):
        if (lineChanged is None):
            self.lineChanged = 0
        else :
            self.lineChanged = lineChanged
    def setLineChanged(self,lineChanged):
        self.lineChanged = lineChanged
      
    def removeTail(self,content,point):
        if (point):
            if point >0 : 
                content = content[:point-1]
        return content
        
    def createQuery(self, content): #before calling createQuery we have to set the lines  
        content = self.removeTail(content, self.lineChanged)
        return content
    
class HFCodegenHintQuery(HFCodegenStandardQuery,HFHintQuery):
    def __init__(self, lineChanged=None, hint=None):
        if (lineChanged is None):
            self.lineChanged = 1
        else :
            self.lineChanged = lineChanged
        if (hint is None):
            self.hint = "buggy line:"
        else :
            self.hint = hint
    
   
        
    def createQuery(self, content): #before calling createQuery we have to set the lines  
        print("lineChanged",self.lineChanged)
        print(content)
        if (self.lineChanged >0):
            self.includeHint(content,[self.lineChanged],self.hint)
        content = self.removeTail(content, self.lineChanged + 1)
        return content



