import sys
from sys import exit
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

while sys.argv and sys.argv[0] == '-h':
    print("[lifi] Command that lists directories\n-d - Lists fils in specified directory\n-h - The help command")

    exit()


#p is directory path
for file in dirs:
    print(file)

if dirs == []:
    print("This directory is empty")
