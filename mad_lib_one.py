import colorama
from colorama import init, Fore, Style
init()

import _main_
from _main_ import get_inputa

import runpy

bl = Fore.LIGHTBLACK_EX
b = Fore.BLUE
r = Fore.MAGENTA
y = Fore.YELLOW
g = Fore.GREEN
c = Fore.CYAN
t = Fore.LIGHTWHITE_EX
rs = Style.RESET_ALL







print(f"{Fore.RED}Please Separate All Inputs With A Comma!{rs}")
print("                      ")

person = get_inputa("Name",1,b)
verb = get_inputa("Verbs",3,g)
exclamation = get_inputa("Exclamations",2,y)
noun = get_inputa("Nouns",2,c)
place = get_inputa("Places",2,r)


print("****************************************")



 
print(f"""We live on a lake. Today {b}{person[0]}{rs} tested
the ice. {y}{exclamation[0]}{rs} it's frozen! Now I am
off to {g}{verb[0]}{rs} my skates. I {g}{verb[1]}{rs}
in the {r}{place[0]}{rs} ,not there. I look in the
{r}{place[1]}{rs} , nope not there.I search
high and low for my ice {c}{noun[0]}{rs}.
Ok so the one place I havn't, {g}{verb[2]}{rs}
my {c}{noun[1]}{rs}. {y}{exclamation[1]}{rs} they are there!
Let's Go skating!""")

print("*****************************************")



Exit = input("Would you like to continue Y/N: ")

if Exit.lower() == "y":
    runpy.run_module(mod_name='mad_lib_two')
else:
    exit()