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


Write.Print(f"""

\t  ______   __    __  ________  __         ______   __       __   ______  
\t/      \ /  |  /  |/        |/  |       /      \ /  |  _  /  | /      \ 
\t/$$$$$$  |$$ |  $$ |$$$$$$$$/ $$ |      /$$$$$$  |$$ | / \ $$ |/$$$$$$  |
\t$$ |  $$ |$$ |  $$ |   $$ |   $$ |      $$ |__$$ |$$ |/$  \$$ |$$ \__$$/ 
\t$$ |  $$ |$$ |  $$ |   $$ |   $$ |      $$    $$ |$$ /$$$  $$ |$$      \ 
\t$$ |  $$ |$$ |  $$ |   $$ |   $$ |      $$$$$$$$ |$$ $$/$$ $$ | $$$$$$  |
\t$$ \__$$ |$$ \__$$ |   $$ |   $$ |_____ $$ |  $$ |$$$$/  $$$$ |/  \__$$ |
\t$$    $$/ $$    $$/    $$ |   $$       |$$ |  $$ |$$$/    $$$ |$$    $$/ 
\t$$$$$$/   $$$$$$/     $$/    $$$$$$$$/ $$/   $$/ $$/      $$/  $$$$$$/
                       Welcome to OuTlAwS tool!
                    Made with love by: TemoOutlaws & Gravity
              გამზადებულია სიყვარულით TemoOutlaws & Gravity - ისგან
               ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~""", Colors.red_to_blue, interval=0.000)
def display():
    Write.Print(f"\n[1] - DOS / დ ო ს ი\n[2] - IP LOOKUP / ა ი პ ი ს   ძ ე ბ ნ ა\n[3] - PHONE LOOKUP / ტ ე ლ ე ფ ო ნ ი ს   ძ ე ბ ნ ა\n[4] HASHING / ჰაშინგი", Colors.blue_to_cyan, interval=0.000)

def cmd_exec(command):
    if command == '1':
        os.system('cmd /k "python reqs.py"' if os.name == 'nt' else 'python reqs.py')
    elif command == '2':
        os.system('cmd /k "python iptracker.py"' if os.name == 'nt' else 'python iptracker.py')
    elif command == '3':
        os.system('cmd /k "python phonenum.py"' if os.name == 'nt' else 'python phonenum.py')
    elif command == '4':
        os.system('cmd /k "python hashing.py"' if os.name == 'nt' else 'python hashing.py')

        display()
    else:
        print('Invalid option!')
while True:
    display()
    command = input('\n> ')

    if command.lower() == 'exit':
        break

    cmd_exec(command)
