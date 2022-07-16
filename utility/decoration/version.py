import requests

def version():
    with open("version.txt", "r") as ver_file:
        version = ver_file.read()
    resp = requests.get('https://raw.githubusercontent.com/MudabbirulSaad/FFMPEG-UTILITY/alpha/version.txt')
    remote_version = resp.text
    if remote_version == version:
        return version
    else:
        return f"{version} (updates available) ==> {remote_version}"