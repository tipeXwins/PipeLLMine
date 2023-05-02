import os
import openai

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
    

from transformers import AutoTokenizer, AutoModelForCausalLM    
class HFCommunicationController():
    tokenizer = AutoTokenizer.from_pretrained("Salesforce/codegen-16B-multi")
    model = AutoModelForCausalLM.from_pretrained("Salesforce/codegen-16B-multi")
    query = "def hello_world():"

    def callToModel(self,query):
        input_ids = self.tokenizer(query, return_tensors="pt").input_ids
        generated_ids = self.model.generate(input_ids, max_length=128)
        print(self.tokenizer.decode(generated_ids[0], skip_special_tokens=True))

comunicator = HFCommunicationController()
comunicator.callToModel("def hello_world():")
""" 
tokenizer = AutoTokenizer.from_pretrained("codeparrot/codeparrot")
model = AutoModelWithLMHead.from_pretrained("codeparrot/codeparrot")

inputs = tokenizer("def hello_world():", return_tensors="pt")
outputs = model(**inputs)
"""
