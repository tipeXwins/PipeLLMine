"""import urllib.request
from unidiff import PatchSet



patch = PatchSet.from_filename('/home/tipex/TFG/TFG-LMBugFixing/Codes/QuixBugs/UniDiffs/bitcount.py', encoding='utf-8')
print(dir(patch[0]))
print(patch[0].is_modified_file) """




# I will try to read the lines of the change from the normal diff directly and reading the line
file1 = open('/home/tipex/TFG/TFG-LMBugFixing/Codes/QuixBugs/Diffs/bitcount.py','r')
for line in file1.readlines():
   
     # reading all lines that do not
     # begin with "TextGenerator"
    if not (line.startswith('<') or line.startswith('---') or line.startswith('>')):
       
        # printing those lines
        print(line)
        print(line.find('c')) # return 1 if has a c or -1 if not or 0 if is on the start
        """# storing only those lines that
        # do not begin with "TextGenerator"
        file2.write(line)"""
 
# close and save the files
file1.close()

