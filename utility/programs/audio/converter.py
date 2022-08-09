import subprocess
from utility.tools.paths import checkDir
from utility.interactive.textout import printsuccess, printerror

out_dir = "output"

def ext_mp3(inp, kbit, outp):
    invideo = inp
    bitrate = kbit
    outpex = f"{out_dir}/{outp}.mp3".replace(".mp4", "")
    if checkDir(out_dir):
        command = 'ffmpeg -i "{}" -b:a {}k -vn "{}"'.format(inp, kbit, outpex)
        try:
            process = subprocess.run(command, shell=True)
            return printsuccess(f"Process execution completed successfully!\n\n[+] Filename: {inp}\n[+] Bitrate: {kbit}K\n[+] Outputname: {outpex}")
        except Exception as e:
            return printerror(f"Error occured: \n LOG:\n{e}")
#TODO
# def ext_wav(inp, outp):
#     invideo = inp
#     outpex = f"{out_dir}/{outp}.wav".replace(".mp4", "")
#     if checkDir(out_dir):
#         command = 'ffmpeg -i "{}" -vn -acodec pcm_f32le -ar 44100 -ac 2 "{}"'.format(inp, outpex)
#         try:
#             process = subprocess.run(command, shell=True)
#             return printsuccess(f"Process execution completed successfully!\n\n[+] Filename: {inp}\n[+] Bitrate: 44100hz\n[+] Outputname: {outpex}")
#         except Exception as e:
#             return printerror(f"Error occured: \n LOG:\n{e}")