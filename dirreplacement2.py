import sys
import getopt
import os
from pathlib import *
p=os.getcwd()
dirs = sorted(os.listdir(p))

sys.argv = sys.argv[1:]
names = []
while sys.argv and sys.argv[0] == '-d':
    dirs = sorted(os.listdir(sys.argv[1]))

    for file in dirs:
        print(file)

    if dirs == []:
        print("This directory is empty")

    exit()


#p is directory path
for file in dirs:
    print(file)

if dirs == []:
    print("This directory is empty")
