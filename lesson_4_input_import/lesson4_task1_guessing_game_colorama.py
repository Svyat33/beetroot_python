### Task 1. The Guessing Game.
# Write a program that generates a random number between 1 and 10 and lets
# the user guess what number was generated. The result should be sent back
# to the user via a print statement.

import random
import time

# With colorama and termcolor modules (example without this modules in another file)
from colorama import init, deinit, reinit, Fore, Back, Style
from termcolor import cprint


def thinking():
    print('The program thinking...')
    time.sleep(1)
    print('Nope! Still thinking...')
    time.sleep(1)
    cprint("Yeap! It's ready!", 'red', 'on_green', attrs=['bold'])
    time.sleep(1)


# While switchers
switcher = True
switcher2 = True

# For changing app_value every time => put it to the first WHILE.
app_value = random.randint(1, 10)

# Comment this string for hiding checking value
print(app_value)

cprint('If yoy want shutdown program, just type "Q" or "q" and hit "Enter".', 'yellow')
while switcher:
    init()
    player_value = input(Fore.BLUE + Back.YELLOW + Style.BRIGHT + 'Try to guess a right value (only integers!):' + Style.RESET_ALL + ' ').strip()
    if player_value == 'Q' or player_value == 'q':
        print(Fore.CYAN + '\nThis is not a defeat, but a tactical retreat')
        switcher = False
    else:
        thinking()
        while switcher2:
            if player_value == 'Q' or player_value == 'q':
                print(Fore.CYAN + '\nThis is not a defeat, but a tactical retreat')
                switcher = False
            elif int(player_value) == app_value:
                print(Fore.GREEN + '\nYou win')
                switcher = False
                switcher2 = False
            else:
                reinit()
                print(Fore.RED + '\nWrong answer\n')
                break

else:
    print(Fore.CYAN + '\nGame over')
    deinit()
