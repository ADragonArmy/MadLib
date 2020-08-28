import colorama
from colorama import init,Fore,Style
init()


def get_inputa(Name,Num,Color):
    """Asks the user for as many inputs as needed checks that there are no empty strings"""

    user_in = input(f"Type {Num} {Name}: ").split(',')[:Num]
    user_in = [e.strip() for e in user_in]
    while len(user_in) < Num or '' in user_in:
        print(f"{Fore.RED}NOT ENOUGH {Name.upper()}!!{Style.RESET_ALL}")
        user_in = input(f"Type {Num} {Name}: ").split(',')[:Num]
        user_in = [e.strip() for e in user_in]
    for i in user_in :
        y = Color + i.strip() + Style.RESET_ALL
        i = y
        print( f"{Name} entered: {i}")

    user_in = [e.strip() for e in user_in]

    return user_in

