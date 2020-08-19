# Task 3
# Extracting numbers.
# Make a list that contains all integers from 1 to 100, then find all integers
# from the list that are divisible by 7 but not a multiple of 5, and store them
# in a separate list. Finally, print the list.
# Constraint: use only while loop for iteration


digit_list = list(range(1, 101))
result_list = []
i = 0
print(digit_list)
while i < len(digit_list):
    while digit_list[i] % 7 == 0 and digit_list[i] % 5 != 0:
        result_list.append(digit_list[i])
        break
    i += 1
print(result_list)
