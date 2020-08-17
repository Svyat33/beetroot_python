# The greatest number
# Write a Python program to get the largest number from a list of random
# numbers with the length of 10
# Constraints: use only while loop and random module to generate numbers

from random import randint

digit_list_random = []
count_index = 0

while count_index <= 9:
    digit_list_random.insert(0, randint(1, 10))
    count_index += 1
    # Checking random/insert
    # print(digit_list_random)
# Checking list
# print('List ready : ' + str(digit_list_random))
digit_list_sorted = sorted(digit_list_random)
print('The largest number is: ' + str(digit_list_sorted[-1]))

