import random
from colorama import init, deinit, Fore, Back, Style

a = random.randint(1, 10)
b = random.randint(1, 10)

operators_list = ['+', '-', '*']
operator_random = random.choice(operators_list)

result_add = a + b
result_sub = a - b
result_mul = a * b

init()
result_entered = input(f'Please, write result (without decimals) for this sum: {a} {operator_random} {b} = ')
if '+' in operator_random and result_add == int(result_entered):
    print(Fore.GREEN, 'Congrats, this is right answer!')
elif '-' in operator_random and result_sub == int(result_entered):
    print(Fore.GREEN, 'Congrats, this is right answer!')
elif '*' in operator_random and result_mul == int(result_entered):
    print(Fore.GREEN, 'Congrats, this is right answer!')
else:
    print(Fore.RED, 'This is wrong answer')
deinit()
