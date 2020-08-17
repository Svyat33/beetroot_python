# Lesson 13
# Task 2. Foo return foo
# Write a Python program to access a function inside a function
# (Tips: use function, which returns another function)
from datetime import datetime
YEAR = 2019


def hello(name: str):
    def leap():
        return YEAR % 4 == 0
    return name.title(), leap


if __name__ == '__main__':
    name, leap_check = hello('john')
    print(leap_check())
    print(YEAR % 4)
    if leap_check():
        print(f"Hi {name}. {YEAR} is a leap year!")
    else:
        print(f"Hi {name}. {YEAR} is not a leap year!")