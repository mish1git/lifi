import sys
import getopt
import os
from pathlib import *
p=os.getcwd()
dirs = os.listdir(p)

#p is directory path
for file in dirs:
    print(file)

if dirs == []:
    print("This directory is empty")
