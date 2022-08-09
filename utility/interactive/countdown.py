from time import sleep
from utility.interactive.textout import printinfo

def countdown(t):
    while t:
        secs = t
        timer = f"Starting in {secs} second(s)..."
        print(timer, end="\r")
        sleep(1)
        t -= 1
      
    printinfo("Starting...")