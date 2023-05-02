import urllib.request
from unidiff import PatchSet
import os

def obtainLinesFromPatch(pathPatchC):
   filesModifiedByDiff = {}
   if os.path.exists(pathPatchC):
      filep = open(pathPatchC, 'r')
      Lines = filep.read()
      patchSet = PatchSet.from_string(Lines)

      for aPatchSet in patchSet:
         fileName = aPatchSet.source_file
         if fileName not in filep:
            filesModifiedByDiff[fileName]={"added":[], "removed":[]}

         for aHunk in aPatchSet:
            for aLine in aHunk:
               if not aLine.is_context:
                  if aLine.is_added:
                     print("debugging")
                     print(type(aLine))
                     filesModifiedByDiff[fileName]["added"].append(aLine.target_line_no)
                  elif aLine.is_removed:
                     filesModifiedByDiff[fileName]["removed"].append(aLine.source_line_no)

      return filesModifiedByDiff
   

results = obtainLinesFromPatch('/home/tipex/TFG/TFG-LMBugFixing/Codes/QuixBugs/UniDiffs/bitcount.py')
print(results)
print("hi")
print(results['BuggyCodes/bitcount.py'])
print(results['BuggyCodes/bitcount.py']['added'][0])
print(list(results.keys())[0]) # obtain all keys from the dictionary (all chunks in this case)
print(results['BuggyCodes/bitcount.py']['removed'][-1])
number = results['BuggyCodes/bitcount.py']['added'][0] # gets the first line modified

print("changed_lines")
print(results['BuggyCodes/bitcount.py']['removed'])

filePath = '/home/tipex/TFG/TFG-LMBugFixing/Codes/QuixBugs/' + list(results.keys())[0]
# Now with the lines modified we will open the buggy code and select a number of lines above and below these modified lines
def obtainLinesBelowAndTop(filePath,pointModified,linesBelow,linesTop):
   file = open(filePath,'r')
   content = file.readlines()
   startLine = max(0,pointModified-linesBelow)
   
   finishLine = pointModified + linesTop
   file.close()
   return content[startLine:finishLine]

print(obtainLinesBelowAndTop(filePath,1,2,30)) ## no problems related with a linereference that not exist only returning void results