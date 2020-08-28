import colorama
from colorama import init,Fore,Style
init()

###This funtion asks the user for input, checks they they provided enough input
#if user has not put in enough it asks them for the input again
#then reprints the input entered, it also removes whitespace from before and after inputs 
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