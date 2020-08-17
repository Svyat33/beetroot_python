# Task 2
# The birthday greeting program.
# Write a program that takes your name as input, and then your age as input and greets you with the following:
# “Hello <name>, on your next birthday you’ll be <age+1> years”

usr_name = input("Type your name here: ")
usr_age = input("Type your age here: ")

print(f'"Hello {usr_name}, on your next birthday you’ll be {int(usr_age) + 1} years"')
