import colorama
from colorama import init,Fore,Style
init()

#This funtion asks the user for input, checks they they provided enough input
#if user has not put in enough it asks them for the input again
#then reprints the input entered, it also removes whitespace from before and after inputs 
#the parmaters on ths funtion String, List Size, Color 
def get_inputa(Name,Num,Color):
    user_in = input(f"Type {Num} {Name}: ").split(',')[:Num]
    while len(x) < Num :
        print(f"{Fore.RED}NOT ENOUGH {Name.upper()}!!{Style.RESET_ALL}")
        user_in = input(f"Type {Num} {Name}: ").split(',')[:Num]
    for i in user_in :
        y = Color + i.strip() + Style.RESET_ALL
        i = y
        print( f"{Name} entered: {i}")

    user_in = [e.strip() for e in user_in]

    return user_in