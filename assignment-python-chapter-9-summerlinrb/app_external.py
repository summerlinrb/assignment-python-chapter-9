import subprocess

# run a command in the terminal
# ls -l means list files and folders with details
subprocess.run(["ls", "-l"])

# run some git commands
# the arguments are entered as a seperate items in the list
subprocess.run(["git", "--version"])
subprocess.run(["git", "status"])
