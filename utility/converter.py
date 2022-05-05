import subprocess
from utility.paths import checkDir
from utility.interactive.textout import printsuccess, printerror

out_dir = "output"

def ext_audio(inp, kbit, outp):
    invideo = inp
    bitrate = kbit
    outpex = f"{out_dir}/{outp}.mp3".replace(".mp4", "")
    if checkDir(out_dir):
        command = "ffmpeg -i {} -b:a {}k -vn {}".format(inp, kbit, outpex)
        try:
            process = subprocess.run(command, shell=True)
            return printsuccess(f"Process execution completed successfully\n\n[+] Filename: {inp}\n[+] Bitrate: {kbit}K\n[+] Outputname: {outpex}")
        except Exception as e:
            return printerror(f"Error occured: \n LOG:\n{e}")