import os
import sys
import platform
import colorama
from colorama import Fore, Style
import pystyle
from pystyle import Write, System, Colors, Colorate, Anime
clear = "gravita sigmaa"
os_name = platform.system()
if os_name == "Linux":
    clear = "clear"
else:
    clear = "cls"

os.system(clear)
Write.Print("Input the string you want to hash / შეიყვანე სტრინგი რომელიც გინდა რომ დაჰაშო\n", Colors.red_to_blue, interval=0.000)
target = input('''>  ''')

os.system(clear)
Write.Print("Choose your algorithm / აირჩიე დაჰაშვის ალგორითმი\n", Colors.red_to_blue, interval=0.000)
Write.Print(f"[1] md5\n", Colors.red_to_blue, interval=0.000)
Write.Print(f"[2] sha1\n", Colors.red_to_blue, interval=0.000)
Write.Print(f"[3] sha256\n", Colors.red_to_blue, interval=0.000)
algorithm =  input('''>  ''')

def hashing(target, algorithm):
    if algorithm == "1":
        hashed_object = hashlib.md5(target.encode())
        os.system(clear)
    elif algorithm == "2":
        hashed_object = hashlib.sha1(target.encode())
        os.system(clear)
    elif algorithm == "3":
        hashed_object = hashlib.sha256(target.encode())
        os.system(clear)
    else:
        os.system(clear)
        return "Unsupported algorithm or invalid choice / არამხარდაჭერილი ალგორითმი ან არასწორი არჩევანი"
        sys.exit()
    os.system(clear)
    return hashed_object.hexdigest()
    

Write.Print(f"Hashed string: {hashing(target, algorithm)} / დაჰაშული სტრინგი: {hashing(target, algorithm)}\n", Colors.red_to_blue, interval=0.000)
