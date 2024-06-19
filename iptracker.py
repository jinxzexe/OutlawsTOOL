from colorama import Fore, Style
from pystyle import Write, System, Colors, Colorate, Anime
import sys,os
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


Write.Print(f" [1] - Get Details About Your Ip / გაიგე შენ აიპიზე დეტალები \n", Colors.red_to_blue, interval=0.000)
Write.Print(f" [2] - Get Details About IP / გაიგე დეტალები აიპიზე\n", Colors.red_to_blue, interval=0.000)
Write.Print(f"Press enter to exit / დააჭირე Enter - ს რომ გახვიდე ", Colors.red_to_blue, interval=0.000)
option = input('''>  ''')





while True:
  if option == "1":

      from requests import get
      myip = get('https://ipapi.co/json/')
      print(myip.json())
      import sys
      sys.exit()
      
                
  elif option == "2" :

      from requests import get
      ip = input("მიუთითე IP:")
      track = get(f'https://ipapi.co/{ip}/json/')
      print(track.json())
      import sys
      sys.exit()
  else:
      Write.Print(f"Thanks for using! / გმადლობთ გამოყენებისთვის! \n", Colors.red_to_blue, interval=0.000)
      import sys
      sys.exit()