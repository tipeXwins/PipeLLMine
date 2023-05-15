import os
import openai
import torch
from transformers import pipeline , AutoTokenizer, AutoModelForSeq2SeqLM

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
        input_ids = self.tokenizer(query, add_special_tokens=False, return_tensors="pt").input_ids
        generated_ids = self.model.generate(
            input_ids, max_length=512, #num_beams=10, num_return_sequences=10, 
            early_stopping=True, decoder_start_token_id=self.tokenizer.lang_code_to_id["__python__"] # language code is 50002
        )
        output = []
        for generated_id in generated_ids:
            output.append(self.tokenizer.decode(generated_id, skip_special_tokens=True))
        #file = open('/home/tipex/TFG/TFG-LMBugFixing/Tests/output.txt','w') # open as write mode and write the new content here
        #file.writelines(output)
        #file.close()
        print("output",output[0])


comunicator = HFCommunicationController()
f = open('/home/tipex/TFG/TFG-LMBugFixing/Tests/input.py', "r")
text = f.read()
print("leido", text)
print("hackiau", "".join(text))
comunicator.callToModelWithTransformers("".join(text))
f.close()










































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