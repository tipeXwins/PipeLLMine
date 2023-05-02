"""import urllib.request
from unidiff import PatchSet



patch = PatchSet.from_filename('/home/tipex/TFG/TFG-LMBugFixing/Codes/QuixBugs/UniDiffs/bitcount.py', encoding='utf-8')
print(dir(patch[0]))
print(patch[0].is_modified_file) """
import os 
import openai
#pip install --upgrade tiktoken
import tiktoken



def readNormalDiffChanges():
    # I will try to read the lines of the change from the normal diff directly and reading the line
    file1 = open('/home/tipex/TFG/TFG-LMBugFixing/Codes/QuixBugs/Diffs/bitcount.py','r')
    modifications = changes= deletions= 0
    for line in file1.readlines():
    
        # reading all lines that do not
        # begin with "TextGenerator"
        if not (line.startswith('<') or line.startswith('---') or line.startswith('>')):
        
            # printing those lines
            print(line)
            modifications +=1

            if (line.find('c') == (0 or 1)):
                changes +=1
            elif (line.find('d') == (0 or 1)):
                deletions += 1

            
            print(line.find('c')) # return 1 if has a c or -1 if not or 0 if is on the start
    # when we finish readinf if there are less than x modifications/additions or deletions we want to save the file in antoher folder

    #Saving 
    """if (modifications < 4  and changes < 3) :
        newfile = open(os.path.join("/home/tipex/TFG/TFG-LMBugFixing/Codes/QuixBugs/FewModificationCodes/", filename ), 'w')
        newfile.write(file_content)"""
    # close and save the files
    file1.close()

def includeHint(filePath,pointModified,hint):
    file = open(filePath,'r')
    content = file.readlines()
    print("line")
    line = content[pointModified]
    print(line)
    print(line[:len(line)-1] +" #Im not sure about the code")
    #remove \n from end of line line[:len(line)-1]
    content[pointModified] = line[:len(line)-1] + "-2" +"#Im not sure about the code"
    # content.insert(4,'holita \n' ) # insert a line in a position
    
    file.close()
    file = open('/home/tipex/TFG/TFG-LMBugFixing/bitcountmodification.py','w') # open as write mode and write the new content here
    file.writelines(content)
    file.close()


#includeHint('/home/tipex/TFG/TFG-LMBugFixing/Codes/QuixBugs/BuggyCodes/bitcount.py', 5-1,"pistita") # Be careful line from os start counting from 0 line from diffs and unidiff starts from 1 so the line returned by diff for example line 5 is line 4



def num_tokens_from_messages(messages, model="gpt-3.5-turbo-0301"):
    """Returns the number of tokens used by a list of messages."""
    try:
        encoding = tiktoken.encoding_for_model(model)
    except KeyError:
        encoding = tiktoken.get_encoding("cl100k_base")
    if model == "gpt-3.5-turbo-0301":  # note: future models may deviate from this
        num_tokens = 0
        for message in messages:
            num_tokens += 4  # every message follows <im_start>{role/name}\n{content}<im_end>\n
            for key, value in message.items():
                num_tokens += len(encoding.encode(value))
                if key == "name":  # if there's a name, the role is omitted
                    num_tokens += -1  # role is always required and always 1 token
        num_tokens += 2  # every reply is primed with <im_start>assistant
        return num_tokens
    else:
        raise NotImplementedError(f"""num_tokens_from_messages() is not presently implemented for model {model}.
See https://github.com/openai/openai-python/blob/main/chatml.md for information on how messages are converted to tokens.""")



def createStandardPythonBugFixingQuery(filePath):
    file = open(filePath,'r')
    content = file.readlines()
    #Add at file start the necessary content
    content.insert(0,"##### Fix bugs in the below function  \n")
    content.insert(1,"\n")
    content.insert(2,"### Buggy Python \n")

    

    #Add at the end the necesary content
    content.append("\n")
    content.append("### Fixed Python \n")
    content.append("\n")


    file.close()
    file = open('/home/tipex/TFG/TFG-LMBugFixing/bitcountmodification.py','w') # open as write mode and write the new content here
    file.writelines(content)
    file.close()

createStandardPythonBugFixingQuery('/home/tipex/TFG/TFG-LMBugFixing/Codes/QuixBugs/BuggyCodes/bitcount.py')
#link to the code https://github.com/openai/openai-cookbook/blob/main/examples/How_to_count_tokens_with_tiktoken.ipynb