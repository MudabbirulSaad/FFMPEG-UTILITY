from pathlib import Path
from utility.programs.audio.converter import ext_mp3
from utility.interactive.textout import printinfo, printerror
from utility.interactive.textin import ininfo

def direct_path_audio():
    inp = input(ininfo("Enter the filename: "))
    kbit = input(ininfo("Bitrate of the output file (default: 320): "))
    outp = input(ininfo("Enter the output filename (optional): "))
    if inp == '':
        printerror("No file name is given.")
        exit(1)
    if kbit == '':
        printinfo("No input detected. using 320k by default.")
        kbit = "320"
    else:
        kbit = kbit
    if outp == '':
        printinfo("No input detected. using default name.")
        outp = f"{Path(inp).name}-{kbit}K"
    else:
        outp = "{}-{}".format(outp, kbit)
    ext_mp3(inp, kbit, outp)