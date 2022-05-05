from ..decoration.infos import info_sign, success_sign, error_sign, warn_sign, regular_sign
from ..decoration.colorful import red, green, blue, cyan, regular, yellow

def printinfo(text):
    print(f"{info_sign} {yellow(text)}")
    
def printsuccess(text):
    print(f"{success_sign} {green(text)}")
    
def printerror(text):
    print(f"{error_sign} {red(text)}")
    
def printcyan(text):
    print(f"{warn_sign} {cyan(text)}")
    
def printregular(text):
    print(f"{regular_sign} {regular(text)}")