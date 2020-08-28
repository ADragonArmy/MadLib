import colorama 
from colorama import init,Fore,Style
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

noun =(get_inputa("Nouns",2,c))
verb =(get_inputa("Verbs",2,g))
adjective =(get_inputa("Adjectives",3,y))
ing = (get_inputa("Verb ending in ing",1,g))
place =(get_inputa("Place",1,r))
nouns = (get_inputa("Plural Noun",1,c))
celebrity = (get_inputa("Celebrity",1,c))
job = (get_inputa("Job",1,r))


print("**********************************")
print("    ")


print(f"""So, you want to {g}{verb[0]}{rs} Pokemon, huh? Well, it's not as
{y}{adjective[0]}{rs} as it seems. First off, you'll need to find them. You can
catch Pokemon in the wild of in (the) {r}{place[0]}{rs}. Once you have
a Charizard or a Blastoise, you'll need to gain its trust. That's not always
easy. You can try feeding it or {g}{ing[0]}{rs} it, but the best
way to gain a Pokemon's trust is to {g}{verb[1]}{rs} with it. Once you
and your Pokemon are best {c}{nouns[0]}{rs}, start training. You can
do this with a friend or even with {c}{celebrity[0]}{rs} at a/an {y}{adjective[1]}{rs}
Gym nearby. Think of it like training a/an {c}{noun[0]}{rs}! Only when
you've trained enough should you challenge another {r}{job[0]}{rs}
for real. After all that work, it would be {y}{adjective[2]}{rs} for someone to
come along and take your {c}{noun[1]}{rs} away!""")

print("    ")
print("**********************************")


Exit = input("Would you like to continue Y/N: ")

if Exit.lower() == "y":
    runpy.run_module(mod_name='mad_lib_one')
else:
    exit()