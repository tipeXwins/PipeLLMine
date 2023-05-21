class Filter: 
    maxModifiedLines = maxAddedLines = maxRemovedLines = 0
    def setMaxModifiedLines(self, maxModifiedLines):
        self.maxModifiedLines = maxModifiedLines
    def setMaxAddedLines(self, maxAddedLines):
        self.maxAddedLines = maxAddedLines
    def setMaxRemovedLines(self, maxRemovedLines):
        self.maxRemovedLines = maxRemovedLines 
    def setMaxLines(self, maxModifiedLines, maxAddedLines, maxRemovedLines):
        self.maxModifiedLines = maxModifiedLines
        self.maxAddedLines = maxAddedLines
        self.maxRemovedLines = maxRemovedLines 
    def filter(self, modifiedLines, addedLines, removedLines):
        if (len(modifiedLines) <= self.maxModifiedLines and len(addedLines) <= self.maxAddedLines and len(removedLines) <= self.maxRemovedLines):
            return True
        else:
            return False