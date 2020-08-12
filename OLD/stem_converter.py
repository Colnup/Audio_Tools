"""Module permettant de convertir un fichier audio en stem"""

import argparse, os

parser = argparse.ArgumentParser(description="utility to convert audio files to stems using spleeter")
parser.add_argument("file", help="the file to convert")
parser.add_argument("-p", "-pists", type=int, choices=[2,4,5], default=4, help="Nombre de pistes à générer")
args = parser.parse_args()

os.system(f"spleeter separate -i \"{args.file}\" -o C:\%HOMEPATH%\Desktop\Musique\\temp -p spleeter:{args.p}stems")