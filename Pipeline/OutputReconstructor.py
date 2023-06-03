
class Reconstructor: 
    def reconstruct(self, originalContent, returnedContent, placeholder):
        return ""

class ReconstructorPatch(Reconstructor):
    def reconstruct(self, originalContent, returnedContent, placeholder):
        reconstructedContent = originalContent.replace(placeholder, returnedContent)
        print("rec",reconstructedContent)
        return  reconstructedContent