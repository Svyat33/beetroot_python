from random import shuffle
string = input('Type word here: ')
string_list = list(string)
count = 0

while count != 5:
    shuffle(string_list)
    result = ''.join(string_list)
    print(result)
    count += 1
