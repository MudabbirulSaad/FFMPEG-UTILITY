from ..decoration.infos import info_sign, success_sign, error_sign, regular_sign
from ..decoration.colorful import red, green, regular, yellow #blue, cyan also avaiable for future

def ininfo(text):
    return f"{info_sign} {yellow(text)}"
    
def inwarn(text):
    return f"{success_sign} {green(text)}"
    
def inerror(text):
    return f"{error_sign} {red(text)}"
    
def inregular(text):
    return f"{regular_sign} {regular(text)}"