import colorama
from termcolor import colored
from colorama import Fore, init

def red(text):
    return colored(text, "red")

def green(text):
    return colored(text, "green")

def blue(text):
    return colored(text, "blue")

def cyan(text):
    return colored(text, "cyan")

def yellow(text):
    return colored(text, "yellow")

def regular(text):
    return text

# red = Fore.RED
# green = Fore.GREEN
# blue = Fore.BLUE
# cyan = Fore.CYAN
# yellow = Fore.YELLOW