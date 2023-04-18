import subprocess
subprocess.run(["./prueba.sh", "--input_file=input.txt"],cwd="../Codes/QuixBugs/") 
# With the above line we will execute the shell script inside the directory we diefine with cwd and then this sh has to create the diffs.
#In my behaviour I created all the diffs and Unidiffs files iteratively with sh commands.