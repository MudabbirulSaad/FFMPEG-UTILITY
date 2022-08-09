import os
from utility.interactive.textout import printcyan

def checkDir(dirName):
    if os.path.isdir(dirName):
        printcyan(f"'{dirName}' Directory already exists and sending output there")
        return True
    else:
        return createDir(dirName)
    
def createDir(dirName):
    os.mkdir(dirName)
    return True