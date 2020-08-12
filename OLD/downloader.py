"""Module permettant de télécharger des vidéos via youtube-dl"""

import argparse, os, sys

parser = argparse.ArgumentParser(description="utility to download video files from the internet using youtube-dl")
group = parser.add_mutually_exclusive_group()
group.add_argument("-s", "--search", action="store_true", help="Recherche une vidéo sur youtube")
group.add_argument("-l", "--link", action="store_true", help="Télécharge la vidéo depuis le lien")
parser.add_argument("x", type=str, help="the object to search or download")
parser.add_argument("format", type=str, choices=["mp3", "wav", "flac", "best"], help="type of file to be stored")
args = parser.parse_args()

if args.format == "mp3" or args.format=="flac" or args.format=="wav":
    if args.search:
        os.system(f"youtube-dl --ignore-config --no-playlist -x --audio-format {args.format} -o \"C:\%HOMEPATH%\Desktop\Musique\\temp\%(title)s.%(ext)s\" \"ytsearch:{args.x}\"")
    elif args.link:
        os.system(f"youtube-dl --ignore-config --no-playlist -x --audio-format {args.format} -o \"C:\%HOMEPATH%\Desktop\Musique\\temp\%(title)s.%(ext)s\" \"{args.x}\"")
elif args.format == "best":
    if args.search:
        os.system(f"youtube-dl --ignore-config --no-playlist -o \"C:\%HOMEPATH%\Desktop\Musique\\temp\%(title)s.%(ext)s\" \"ytsearch:{args.x}\"")
    elif args.link:
        os.system(f"youtube-dl --ignore-config --no-playlist -o \"C:\%HOMEPATH%\Desktop\Musique\\temp\%(title)s.%(ext)s\" \"{args.x}\"")
