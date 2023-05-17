import os
import openai
import torch
from transformers import pipeline , AutoTokenizer, AutoModelForSeq2SeqLM, AutoModelForCausalLM

class OAICommunicationController():
    openai.api_key = "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"
    model = "text-davinci-003"
    temperature = 0
    max_tokens = 1000
    top_p = 1
    frequency_penalty = 0
    presence_penalty = 0
    def setHyperparameters(self, hyperparameters):
        self.temperature = hyperparameters[0]
        self.max_tokens=hyperparameters[1],
        self.top_p=hyperparameters[2],
        self.frequency_penalty=hyperparameters[3],
        self.presence_penalty=hyperparameters[4],
    def setModel(self, model):
        self.model = model
    def setTemperature(self, temperature):
        self.temperature = temperature
    def setMaxTokens(self, max_tokens):
        self.max_tokens = max_tokens
    def setTopP(self, top_p):
        self.top_p = top_p
    def setFrequencyPenalty(self,frequency_penalty):
        self.frequency_penalty = frequency_penalty
    def setPresencePenalty(self,presence_penalty):
        self.presence_penalty = presence_penalty
    def setApiKey(self,apiKey):
        self.apiKey = apiKey
        openai.api_key = apiKey
    def callToModel(self, query):
        response = openai.Completion.create(
        model=self.model,
        prompt=query,
        temperature=self.temperature,
        max_tokens=self.max_tokens,
        top_p=self.top_p,
        frequency_penalty=self.frequency_penalty,
        presence_penalty=self.presence_penalty,
        stop=["###"]
        )
        return response['choices'][0]['text']
    

    
class HFCommunicationController():
    
    tokenizer = AutoTokenizer.from_pretrained("uclanlp/plbart-base")

    model = AutoModelForSeq2SeqLM.from_pretrained("uclanlp/plbart-base")

    def callToModelWithTransformers(self,query):
        print("THIS IS AN ABSTRACT CLASS PLEASE REFFER TO AN SPECIFIC Hugging Face Controller")


class HFPlBartController(HFCommunicationController):
    tokenizer = AutoTokenizer.from_pretrained("uclanlp/plbart-base")#,src_lang="python", tgt_lang="python")
    model = AutoModelForSeq2SeqLM.from_pretrained("uclanlp/plbart-base")
    def callToModelWithTransformers(self,query):
        input_ids = self.tokenizer(query, add_special_tokens=False, return_tensors="pt").input_ids
        generated_ids = self.model.generate(
            input_ids, max_length=512, num_beams=10, num_return_sequences=10, 
            early_stopping=True, decoder_start_token_id=self.tokenizer.lang_code_to_id["__python__"] # language code is 50002
        )
        output = []
        for generated_id in generated_ids:
            output.append(self.tokenizer.decode(generated_id, skip_special_tokens=True))
        #Writing on file for testing purposes
        file = open('../Tests/outputBart.txt','w') # open as write mode and write the new content here
        file.writelines(output)
        file.close()
        return output[0]
    
class HFCodeT5Controller(HFCommunicationController):
    tokenizer = AutoTokenizer.from_pretrained("Salesforce/codet5-base")
    model = AutoModelForSeq2SeqLM.from_pretrained("Salesforce/codet5-base")
    def callToModelWithTransformers(self,query):
        input_ids = self.tokenizer(query, return_tensors="pt").input_ids
        generated_ids = self.model.generate(input_ids, max_length=512, num_beams=10, num_return_sequences=10)
        output = []
        for generated_id in generated_ids:
            output.append(self.tokenizer.decode(generated_id, skip_special_tokens=True))
        #Writing on file for testing purposes
        file1 = open('../Tests/outputCodeT5.txt','w') # open as write mode and write the new content here
        file1.writelines(output)
        file1.close()
        return output
    
class HFCodeGenController(HFCommunicationController):
    tokenizer = AutoTokenizer.from_pretrained("Salesforce/codegen-2B-mono")
    model = AutoModelForCausalLM.from_pretrained("Salesforce/codegen-2B-mono")
    def callToModelWithTransformers(self,query):
        input_ids = self.tokenizer(query, return_tensors="pt").input_ids
        eos_id = self.tokenizer.convert_tokens_to_ids(self.tokenizer.eos_token)
        generated_ids = self.model.generate(
            input_ids, max_new_tokens=128, num_beams=10, num_return_sequences=10, early_stopping=True,
            pad_token_id=eos_id, eos_token_id=eos_id
        )
        output = []
        for generated_id in generated_ids:
            output.append(self.tokenizer.decode(generated_id, skip_special_tokens=True))
        #Writing on file for testing purposes
        file2 = open('../Tests/outputCodeGen.txt','w') # open as write mode and write the new content here
        file2.writelines(output)
        file2.close()
        return output[0]

class HFIncoderController(HFCommunicationController):
    tokenizer = AutoTokenizer.from_pretrained("facebook/incoder-1B")
    model = AutoModelForCausalLM.from_pretrained("facebook/incoder-1B")
    def callToModelWithTransformers(self,query):
        input_ids = self.tokenizer(query, return_tensors="pt").input_ids
        eos_id = self.tokenizer.convert_tokens_to_ids('</code>')
        generated_ids = self.model.generate(
            input_ids, max_new_tokens=128, num_beams=10, num_return_sequences=10, early_stopping=True,
            pad_token_id=eos_id, eos_token_id=eos_id
        )
        output = []
        for generated_id in generated_ids:
            output.append(self.tokenizer.decode(generated_id, skip_special_tokens=True,clean_up_tokenization_spaces=False))
        #Writing on file for testing purposes
        file3 = open('../Tests/outputIncoder.txt','w') # open as write mode and write the new content here
        file3.writelines(output)
        file3.close()
        return output



## This is for testing this pipeline module

### READ QUERIES
f = open('../Tests/plbartQuery.py', "r")
queryBart = f.read()
f.close()

f = open('../Tests/codet5Query.py', "r")
queryCodeT5 = f.read()
f.close()

f = open('../Tests/codegenQuery.py', "r")
queryCodeGen = f.read()
f.close()

f = open('../Tests/incoderQuey.py', "r")
queryInCoder = f.read()
f.close()


### Do the calls with the respective query
# Output will be writed on outputHFModel.txt on Test folder

comunicatorBart =  HFPlBartController() # Return full code one string 
print("Bart",comunicatorBart.callToModelWithTransformers("".join(queryBart)))

"""
comunicatorCodeT5 =  HFCodeT5Controller() # return only snipets of code where specified and vector of string with lines
print("CodeT5",comunicatorCodeT5.callToModelWithTransformers("".join(queryCodeT5)))

comunicatorIncoder =  HFIncoderController() # Complexx queries and vectors of full results but strange ones
print("Incoder",comunicatorIncoder.callToModelWithTransformers("".join(queryInCoder)))

comunicatorCodeGen =  HFCodeGenController() #gives 4 responses with full code try to se if every output is a result
print("CodeGen",comunicatorCodeGen.callToModelWithTransformers("".join(queryCodeGen)))

"""









































"""

class HFCommunicationController():

    tokenizer = AutoTokenizer.from_pretrained("Salesforce/codegen-16B-multi")
    model = AutoModelForCausalLM.from_pretrained("Salesforce/codegen-16B-multi") #16b is also for python
    query = "def hello_world():"

    def callToModel(self,query):
        input_ids = self.tokenizer(query, return_tensors="pt").input_ids
        generated_ids = self.model.generate(input_ids, max_length=128)
        print(self.tokenizer.decode(generated_ids[0], skip_special_tokens=True))

comunicator = HFCommunicationController()
comunicator.callToModel("def hello_world():")
"""
""" 
tokenizer = AutoTokenizer.from_pretrained("codeparrot/codeparrot")
model = AutoModelWithLMHead.from_pretrained("codeparrot/codeparrot")

inputs = tokenizer("def hello_world():", return_tensors="pt")
outputs = model(**inputs)
"""

"""
class HFCommunicationController():
    
    tokenizer = AutoTokenizer.from_pretrained("codeparrot/codeparrot")
    model = AutoModelForCausalLM.from_pretrained("codeparrot/codeparrot") #AutoModelWithLMHead
    

    def callToModelWithTransformers(self,query):
        inputs = self.tokenizer(query, return_tensors="pt")
        outputs = self.model(**inputs)

        generated_ids = outputs["logits"].squeeze().argmax(dim=-1)
        generated_text = self.tokenizer.decode(generated_ids, skip_special_tokens=True)
        print(generated_text)

        
        input_ids = self.tokenizer(query, return_tensors="pt").input_ids
        attention_mask = torch.ones(input_ids.shape, dtype=torch.long)
        generated_ids = self.model.generate(input_ids, max_length=128, attention_mask=attention_mask )#pad_token_id=self.tokenizer.pad_token_id
        print(self.tokenizer.decode(generated_ids[0], skip_special_tokens=True))
        
    def callToModelWithPipeline(self,query):
        
        pipe = pipeline("text-generation", model="codeparrot/codeparrot")
        outputs = pipe("def hello_world():") #returning the entire output tensors, including hidden states
        print(outputs) """