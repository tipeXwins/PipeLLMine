import subprocess
subprocess.run(["./createUniDiffs.sh", "--input_file=input.txt"],cwd="../Codes/QuixBugsNo/") 
# With the above line we will execute the shell script inside the directory we defined with cwd parameter and then this sh has to create the diffs.
#In my behaviour I created all the diffs and Unidiffs files iteratively with sh commands.