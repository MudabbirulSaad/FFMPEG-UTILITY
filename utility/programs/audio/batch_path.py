from pathlib import Path
from utility.programs.audio.converter import ext_mp3
from utility.interactive.countdown import countdown
from utility.interactive.textout import printinfo, printcyan, printerror
from utility.interactive.textin import ininfo

def batch_path_audio():
    path_name = input("Enter the path of files (press enter if using default path 'contents'): ")
    if path_name == '':
        path_name = 'contents'
    else:
        path_name = path_name
    kbit = input(ininfo("Bitrate of the output file (default: 320): "))
    if kbit == '':
        kbit = "320"
    else:
        kbit = kbit
    try:
        path_dir = Path(path_name)
        files_count = len(list(path_dir.glob('*.mp4')))
        files = list(path_dir.glob('*.mp4'))
        printinfo(f"Total number of files: {files_count}")
        if files_count == 0:
            printerror('No files were found in the directory')
            exit(1)
        countdown(5)
        printcyan("Starting within 5 seconds...")
        for i in range(0, files_count):
            printinfo(f"{i}. {files[i]}")
            inp = files[i]
            outp = f"{Path(inp).name}-{kbit}K"
            ext_mp3(inp, kbit, outp)
        
    except Exception as e:
        printerror("Error: " + str(e))