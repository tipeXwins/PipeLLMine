import os
import openai

#Path with the codes
dir_path_buggy_codes = "/home/tipex/TFG/TFG-LMBugFixing/Codes/Quantum-Computing-Platforms/minimal_bugfixes/Cirq/Cirq#608/after" #pasar por parametro 
dir_path_correct_codes = "" # esto igual   # mirar librerias para hacer unified diffs y  librerias que te leen los difss directamente

buggyCodes = []
correctCodes = []
totalCorreclyRepair = totalIncorrectlyRepair = 0
#openai.api_key = 

# list to store files
files = []

# Iterate directory
for path in os.listdir(dir_path_buggy_codes):
    # check if current path is a file
    if os.path.isfile(os.path.join(dir_path_buggy_codes, path)):
        files.append(path)
print(files)

for file in files :
  full_path = dir_path_buggy_codes +  "/" + file
  print(full_path)
  f = open(full_path, "r")
  text = f.read()
  buggyCodes.append(text)
  f.close()
print("holita")
print(buggyCodes)
files = []

# Iterate directory
for path in os.listdir(dir_path_correct_codes):
    # check if current path is a file
    if os.path.isfile(os.path.join(dir_path_correct_codes, path)):
        files.append(path)
print(files)

for file in files :
  full_path = dir_path_correct_codes +  "/" + file
  print(full_path)
  f = open(full_path, "r")
  text = f.read()
  correctCodes.append(text)
  f.close()




def callToModel(buggyCode, model, hyperparameters):
  response = openai.Completion.create(
    model= model,
    prompt=buggyCode,
    temperature=hyperparameters[0],
    max_tokens=hyperparameters[1],
    top_p=hyperparameters[2],
    frequency_penalty=hyperparameters[3],
    presence_penalty=hyperparameters[4],
    stop=["###"]
  )
  return response['choices'][0]['text']

def compareOutput(codeRepairCorrectly, codeProposedByTheModel):
  if (codeRepairCorrectly == codeProposedByTheModel):
    return True
  return False



""" 
response = openai.Completion.create(
  model="code-davinci-002",
  prompt="##### Fix bugs in the below function\n \n### Buggy Python\n a =+ 3\n    \n### Fixed Python",
  temperature=0,
  max_tokens=182,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0,
  stop=["###"]
)

#print(response) full response

#print(response['choices'][0]['text'])  # el texro de la primera respuesta


#f = open('/home/tipex/TFG/TFG-LMBugFixing/Codes/Quantum-Computing-Platforms/minimal_bugfixes/Cirq/Cirq#608/after/setup.py', "r")
f = open('./prueba.py', 'r')
#print(f.read())
correctText = f.read()

print(correctText == response['choices'][0]['text']) ## Compare the strings

f.close()

"""