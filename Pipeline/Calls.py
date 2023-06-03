import os
import openai
import torch
from transformers import pipeline , AutoTokenizer, AutoModelForSeq2SeqLM, AutoModelForCausalLM
from enum import Enum


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
    def callToModel(self,query):
        print("THIS IS AN ABSTRACT CLASS PLEASE REFFER TO AN SPECIFIC Hugging Face Controller")


class HFPlBartController(HFCommunicationController):
    MAX_LENGTH = 512
    NUM_BEAMS = 10
    NUM_RETURN_SEQUENCES = 10
    def __init__(self,num_responses=None):
        self.tokenizer = AutoTokenizer.from_pretrained("uclanlp/plbart-base",src_lang="python", tgt_lang="python")
        self.model = AutoModelForSeq2SeqLM.from_pretrained("uclanlp/plbart-base")
        if (num_responses is not None):
            self.NUM_BEAMS = self.Num_RETURN_SEQUENCES = num_responses
    def callToModel(self,query, add_special_tokens=False):
        
        input_ids = self.tokenizer(query, add_special_tokens=add_special_tokens, return_tensors="pt").input_ids
        generated_ids = self.model.generate(
            input_ids, max_length=self.MAX_LENGTH, num_beams=self.NUM_BEAMS, num_return_sequences=self.NUM_RETURN_SEQUENCES, 
            early_stopping=True, decoder_start_token_id=self.tokenizer.lang_code_to_id["__python__"]#"__python__"
        )
        output = []
        for generated_id in generated_ids:
            aSolution = self.tokenizer.decode(generated_id, skip_special_tokens=True)
            #print(aSolution)
            output.append(aSolution)

        return output


class HFCodeT5Controller(HFCommunicationController):
    MAX_LENGTH = 512
    NUM_BEAMS = 10
    NUM_RETURN_SEQUENCES = 10
    def __init__(self, num_responses=None):
        self.tokenizer = AutoTokenizer.from_pretrained("Salesforce/codet5-base")
        self.model = AutoModelForSeq2SeqLM.from_pretrained("Salesforce/codet5-base")
    
        if (num_responses is not None):
            self.NUM_BEAMS = self.Num_RETURN_SEQUENCES = num_responses
    def callToModel(self,query):
        input_ids = self.tokenizer(query, return_tensors="pt").input_ids
        generated_ids = self.model.generate(input_ids, max_length=self.MAX_LENGTH, num_beams=self.NUM_BEAMS, num_return_sequences=self.NUM_RETURN_SEQUENCES)
        output = []
        for generated_id in generated_ids:
            output.append(self.tokenizer.decode(generated_id, skip_special_tokens=True))
        return output
class CodeGenSize(Enum):
    size350M ="350M"
    size2B ="2B"
    size6B ="6B"
    size16B ="16B"

class CodeGenData(Enum):
    nl = "nl"
    multi = "multi"
    mono = "mono"

class HFCodeGenController(HFCommunicationController):
    MAX_NEW_TOKENS = 128
    NUM_BEAMS = 10
    NUM_RETURN_SEQUENCES = 10
    def __init__(self, num_responses=None):
        self.tokenizer = AutoTokenizer.from_pretrained("Salesforce/codegen-2B-mono")
        self.model = AutoModelForCausalLM.from_pretrained("Salesforce/codegen-2B-mono")
        if (num_responses is not None):
            self.NUM_BEAMS = self.Num_RETURN_SEQUENCES = num_responses

    def callToModel(self,query):
        input_ids = self.tokenizer(query, return_tensors="pt").input_ids
        eos_id = self.tokenizer.convert_tokens_to_ids(self.tokenizer.eos_token)
        generated_ids = self.model.generate(
            input_ids, max_new_tokens=self.MAX_NEW_TOKENS, num_beams=self.NUM_BEAMS, num_return_sequences=self.NUM_RETURN_SEQUENCES, early_stopping=True,
            pad_token_id=eos_id, eos_token_id=eos_id
        )
        output = []
        for generated_id in generated_ids:
            output.append(self.tokenizer.decode(generated_id, skip_special_tokens=True))
        return output

class HFIncoderController(HFCommunicationController):
    MAX_NEW_TOKENS = 128
    NUM_BEAMS = 10
    NUM_RETURN_SEQUENCES = 10
    def __init__(self, num_responses= None):
        self.tokenizer = AutoTokenizer.from_pretrained("facebook/incoder-1B")
        self.model = AutoModelForCausalLM.from_pretrained("facebook/incoder-1B")
        if (num_responses is not None):
            self.NUM_BEAMS = self.Num_RETURN_SEQUENCES = num_responses
    def callToModel(self,query):
        input_ids = self.tokenizer(query,add_special_tokens=False, return_tensors="pt").input_ids
        eos_id = self.tokenizer.convert_tokens_to_ids('</code>')
        generated_ids = self.model.generate(
            input_ids, max_new_tokens=self.MAX_NEW_TOKENS, num_beams=self.NUM_BEAMS, num_return_sequences=self.NUM_RETURN_SEQUENCES, early_stopping=True,
            pad_token_id=eos_id, eos_token_id=eos_id
        )
        output = []
        for generated_id in generated_ids:
            output.append(self.tokenizer.decode(generated_id, skip_special_tokens=True,clean_up_tokenization_spaces=True))
        return output
