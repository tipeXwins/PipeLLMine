class CodeInformation():
    queries = []
    responses = []
    def __init__(self, buggyCode, correctCode):
        self.buggyCodeContent = buggyCode
        self.correctCodeContent = correctCode
        self.queries = []
    def addQuery(self, query):
        self.queries.append(query)
    def addResponse(self, response):
        self.responses.append(response)