import colorama
from colorama import init,Fore,Style
init()

def get_inputa(Name,Num,Color):
    x = input(f"Type {Num} {Name}: ").split(',')[:Num]
    while len(x) < Num :
        print(f"{Fore.RED}NOT ENOUGH {Name.upper()}!!{Style.RESET_ALL}")
        x = input(f"Type {Num} {Name}: ").split(',')[:Num]
    for i in x :
        y = Color + i.strip() + Style.RESET_ALL
        i = y
        print( f"{Name} entered: {i}")

    x = [e.strip() for e in x]

    return x