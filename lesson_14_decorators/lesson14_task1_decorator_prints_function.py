# Lesson 14
# Task 1. Decorator prints function
# Write a decorator that prints a function with arguments passed to it.
# NOTE! It should print the function, not the result of its execution!
# For example:
# "add called with 4, 5"
'''
def logger(func):

    pass

@logger

def add(x, y):

    return x + y

@logger

def square_all(*args):

    return [arg ** 2 for arg in args]
'''


def logger(func):
    def wrapper(*args, **kwargs):
        # TODO: вписать метод или придумать другой способ удаления скобок в выводе
        print(f"{func.__name__} called with {str(args).replace('(','').replace(')','')}")
        return func(*args, **kwargs)
    return wrapper


@logger
def add(x, y):
    return x + y


@logger
def square_all(*args):
    return [arg ** 2 for arg in args]


if __name__ == '__main__':
    add(4, 5)
    square_all(4, 5, 6)
