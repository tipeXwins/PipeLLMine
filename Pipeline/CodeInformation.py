class CodeInformation():
    
    def __init__(self, buggyCode, correctCode):
        self.buggyCodeContent = buggyCode
        self.correctCodeContent = correctCode
        self.queries = []
        self.responses = []
        self.name = ""
        self.linesChanged = []
    def setName(self, name):
        self.name = name
    def setLinesChanged(self, linesChanged):
        self.linesChanged = linesChanged
    def addQuery(self, query):
        self.queries.append(query)
    def addResponse(self, response):
        self.responses.append(response)