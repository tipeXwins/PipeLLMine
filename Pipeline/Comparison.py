from tokenize import tokenize, untokenize, TokenInfo
from io import BytesIO
#from codexglue.evaluation.metrics import CodeBLEU

import nltk
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
   

references =['\n', 'def bitcount(n):\n', '    count = 0\n', '    while n:\n', '        n ^= n - 1\n', '        count += 1\n', '    return count\n']
hypotheses =['\n', 'def bitcount(n):\n', '    count = 0\n', '    while n:\n', '        n &= n - 1\n', '        count += 1\n', '    return count\n']
comparer = ComparerNLTKCodeBleu()
code_bleu = comparer.compare(references, hypotheses)
print(f"CodeBleu score: {code_bleu}")

"""class ComparerCodeXGLUECodeBleu(ComparerCodeBleu): 
    def compute_code_bleu(self,references, hypotheses):
        #Compute CodeBleu metric given reference and hypothesis source code.
        # Tokenize the source codes
        references = [self.tokenize_code(ref) for ref in references]
        hypotheses = [self.tokenize_code(hyp) for hyp in hypotheses]
    
        # Convert the tokenized code back to string
        references = [" ".join(ref).strip() for ref in references]
        hypotheses = [" ".join(hyp).strip() for hyp in hypotheses]
    
        # Compute the CodeBleu score
        code_bleu = CodeBLEU()
        score = code_bleu.compute(references, hypotheses)
    
        return score

"""
