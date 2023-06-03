from tokenize import tokenize, untokenize, TokenInfo
from io import BytesIO
#from codexglue.evaluation.metrics import CodeBLEU

import nltk
import statistics
#nltk.download('punkt')
from nltk.translate.bleu_score import corpus_bleu, sentence_bleu,SmoothingFunction

class Comparer: 
    def compare(self, file1, file2):
        return (file1 == file2)
    

class ComparerCodeBleu(Comparer): 
    def tokenize_code(self,code):
        """Tokenize source code and return the list of tokens."""
        tokens = []
        for tok in tokenize(BytesIO(code.encode('utf-8')).readline):
            if tok.type == 57: # TokenInfo.NEWLINE is 57 in Python 3.8
                tokens.append("\n")
            elif tok.type == 58: # TokenInfo.INDENT is 58 in Python 3.8
                tokens.append("    ")
            elif tok.type == 59: # TokenInfo.DEDENT is 59 in Python 3.8
                pass
            else:
                tokens.append(tok.string)
        return tokens
    def compute_code_bleu(self,references, hypotheses):
        score = 0
    
        return score
    def compare(self, file1, file2):
        return (self.compute_code_bleu(file1,file2))
    
class ComparerNLTKCodeBleu(ComparerCodeBleu): 
    def compute_code_bleu(self,references, hypotheses):

        references = ''.join(references)
        hypotheses = ''.join(hypotheses)
        # Tokenize the source codes
        ref_tokens = references.split()
        hyp_tokens = hypotheses.split()

        # Compute the CodeBLEU score
        weights = [0.25] * 4  # Use the default weights for CodeBLEU
        smoothing = SmoothingFunction()
        code_bleu = sentence_bleu([ref_tokens], hyp_tokens, weights=weights, smoothing_function=smoothing.method1)

        return code_bleu

class MultipleComparerNLTKCodeBleu(ComparerNLTKCodeBleu): 
    def __init__(self,codeBleuRef=None):
        self.metric = 0
        if (codeBleuRef is not None):
            self.codeBleuRef = codeBleuRef
        else:
            self.codeBleuRef = 0.5
    def setCodeBleuRef(self, codeBleuRef):
        self.codeBleuRef = codeBleuRef
    def compareMultipleOutputs(self, outputs, reference):
        #primero k valores
        #mediana y standard deviation 
        self.metric = 0
        self.avg = 0 
        self.median = 0
        self.stand_dev = 0
        codeBleuValues = []
        for output in outputs:
            codeBleu= self.compute_code_bleu(reference,output)
            codeBleuValues.append(codeBleu)
            self.avg += codeBleu
            if codeBleu >= self.codeBleuRef:
                self.metric += 1
        self.avg /= len(outputs)
        self.metric /= len(outputs)
        self.median = statistics.median(codeBleuValues)
        self.stand_dev = statistics.stdev(codeBleuValues)
        return "values: " + "".join(str(s)+" " for s in codeBleuValues)+" avg: " + str(self.avg) + " metric_treshold: " + str(self.codeBleuRef) + " metric: " + str(self.metric) + " median: " + str(self.median) + " standard deviation: " + str(self.stand_dev)
