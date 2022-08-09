#import argparse
from utility.decoration.logo import logo
from utility.interactive.textout import printerror, printinfo
from utility.programs.audio.direct_path import direct_path_audio
from utility.programs.audio.serial_path import serial_path_audio
from utility.programs.audio.batch_path import batch_path_audio


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
        printinfo("What do you preffered?\n1. Enter direct file path\n2. Enter filename by checking serial no.\n3. Batch Extraction.")
        user_choice = int(input("Enter your choice: "))
        if user_choice == 1:
            direct_path_audio()
        elif user_choice == 2:
            serial_path_audio()
        elif user_choice == 3:
            batch_path_audio()
        else:
            printerror("Invalid choice: " + user_choice)
    except Exception as e:
        print("Error Log: {}\n".format(e))
        printinfo("Okay! Exiting...")
        exit(1)
        
if __name__ == '__main__':
    main()