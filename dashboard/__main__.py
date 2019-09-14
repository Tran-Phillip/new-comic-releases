#first party
import subprocess
import os
import sys

os.chdir("dashboard")
print(os.getcwd())

subprocess.call(['python3', 'manage.py', 'runserver'])
