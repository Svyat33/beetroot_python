# Task 1
# Make a program that has some sentence (a string) on input and
# returns a dict containing all unique words as keys and the number
# of occurrences as values.

import collections
import string


# Sample for string:
# user_string = "Hey, hey, hey, hey. Look. I take a girl out, she can order whatever she wants! The more, the better! All right? Just don’t order a Garden salad and then eat my food! That’s a good way to lose some fingers!

trantab = str.maketrans('', '', string.punctuation)
user_string = input('Enter a string here: ').translate(trantab).lower()

user_list = user_string.split()

string_insertions = dict(collections.Counter(user_list))
print(string_insertions)
