#import argparse
from utility.converter import ext_audio
from utility.decoration.logo import logo
from utility.interactive.textout import printinfo, printerror
from utility.interactive.textin import ininfo, inerror, inregular, inwarn

# TODO
# parser = argparse.ArgumentParser(description='FFMPEG utility helper.')
# parser.add_argument('--input', 
#                     metavar='input',
#                     type=str,
#                     help='A filename for to input')

# parser.add_argument('--bitrate',
#                     metavar='vitrate',
#                     type=str,
#                     help='Bitrate of output audio',
#                     required=False)

# parser.add_argument('--output',
#                     metavar='output',
#                     type=str,
#                     help='A filename for output',
#                     required=False)

# data= parser.parse_args()

def main():
    logo()
    try:
        inp = input(ininfo("Enter the filename: "))
        kbit = input(ininfo("Bitrate of the output file (default: 320): "))
        outp = input(ininfo("Enter the output filename (optional): "))
        if inp == '':
            printerror("Please enter a file name.")
            exit(1)
        if kbit == '':
            kbit = "320"
        else:
            kbit = kbit
        if outp == '':
            outp = f"{inp}-{kbit}K"
        else:
            outp = "{}-{}".format(outp, kbit)
        ext_audio(inp, kbit, outp)
    except Exception as e:
        print("Error Log: {}\n".format(e))
        printinfo("Okay! Exiting...")
        exit(1)
        
if __name__ == '__main__':
    main()