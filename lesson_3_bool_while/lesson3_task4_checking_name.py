name_stored = 'john'
name_received = input('Please, enter your name: ')
name_received_lower = name_received.lower()
name_correct = False


while name_stored != name_received_lower:
    name_received = input('Please, enter your name: ')
    name_received_lower = name_received.lower()
else:
    name_correct = True
print(name_correct)

'''
Task 4
The name check.
Write a program that has a variable with your name stored (in lowercase)
 and then asks for your name as input. The program should check if your 
 input is equal to the stored name even if the given name has another 
 case, e.g., if your input is “Anton” and the stored name is “anton”, 
 it should return True.
'''