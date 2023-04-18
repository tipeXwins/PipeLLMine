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
                     filesModifiedByDiff[fileName]["added"].append(aLine.target_line_no)
                  elif aLine.is_removed:
                     filesModifiedByDiff[fileName]["removed"].append(aLine.source_line_no)

      return filesModifiedByDiff

def obtainInfoLines(filesModifiedByDiff={}, dirPath="",mode=1):
    infoLines = []
    infoGathered = ""
    if (mode == 1): 
        infoGathered = "added"
    elif (mode ==2):
       infoGathered = "removed"
    
    if (filesModifiedByDiff == {}):
        filesModifiedByDiff =obtainLinesFromPatch(dirPath)
    for key in list(filesModifiedByDiff.keys()):
       if (mode ==3):
          addedLines = filesModifiedByDiff[key]["added"]
          removedLines = filesModifiedByDiff[key]["removed"]
          changedLines = set(addedLines) & set(removedLines)

          infoLines.append([key,list(changedLines)])
       else:
          infoLines.append([key,filesModifiedByDiff[key][infoGathered]])
    return infoLines

