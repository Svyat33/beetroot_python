# Task 3
# Extracting numbers.
# Make a list that contains all integers from 1 to 100, then find all integers
# from the list that are divisible by 7 but not a multiple of 5, and store them
# in a separate list. Finally, print the list.
# Constraint: use only while loop for iteration


digit_list = []
num_counts = 1

while num_counts <= 100:
    digit_list.append(num_counts)
    num_counts += 1
    # Checking random/insert
    # print(digit_list_random)
# Checking list
num_counts = 0
print('List ready : ' + str(digit_list))








# digit_list_random = []
# count_index = 0
#
# while count_index <= 9:
#     digit_list_random.insert(0, randint(1, 10))
#     count_index += 1
#     # Checking random/insert
#     # print(digit_list_random)
# # Checking list
# # print('List ready : ' + str(digit_list_random))
# digit_list_sorted = sorted(digit_list_random)
# print('The largest number is: ' + str(digit_list_sorted[-1]))
