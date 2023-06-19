
class Reconstructor: 
    def reconstruct(self, originalContent, returnedContent):
        return ""

class ReconstructorPatch(Reconstructor):
    def setPlaceholder(self, placeholder):
        self.placeholder = placeholder
    def reconstruct(self, originalContent, returnedContent):
        reconstructedContent = originalContent.replace(self.placeholder, returnedContent)
        print("rec",reconstructedContent)
        return  reconstructedContent
class ReconstructorTruncate(Reconstructor):
    def __init__(self, lineModified=None, linesBelow=None, linesAbove=None):
        if (lineModified is None):
            self.lineModified= ""
        else :
            self.lineModified = lineModified
        if (linesBelow is None):
            self.linesBelow = 10
        else:
            self.linesBelow = linesBelow
        if (linesAbove is None):
            self.linesAbove = 10
        else:
            self.linesAbove = linesAbove
        
    def setLineModified(self,lineModified):
        self.lineModified = lineModified
    def setLinesBelow(self,linesBelow):
        self.linesBelow = linesBelow
    def setLinesAbove(self,linesAbove):
        self.linesAbove= linesAbove
    
    def reconstruct(self, originalContent, returnedContent):
        content_start = originalContent[:self.lineModified-self.linesAbove]
        content_end = originalContent[self.lineModified-self.linesAbove:]
        return (content_start + returnedContent +content_end)
    



