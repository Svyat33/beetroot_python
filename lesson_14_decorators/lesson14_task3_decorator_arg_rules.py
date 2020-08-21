# Lesson 14
# Task 3
#
# Write a decorator `arg_rules` that validates arguments passed to the function.
# A decorator should take 3 arguments:
#   max_length: 15
#   type_: str
#   contains: [] - list of symbols that an argument should contain
#
# If some of the rules' checks returns False, the function should return False and print
# the reason it failed; otherwise, return the result.

'''
def arg_rules(type_: type, max_length: int, contains: list):

    pass

@arg_rules(type_=str, max_length=15, contains=['05', '@'])

def create_slogan(name: str) -> str:

    return f"{name} drinks pepsi in his brand new BMW!"

assert create_slogan('johndoe05@gmail.com') is False

assert create_slogan('S@SH05') == 'S@SH05 drinks pepsi in his brand new BMW!'
'''

# TODO: Выяснить, что делать с этим заданием. Его полностью разобрали на уроке.
# made by Svyatoslav:
def arg_rules(type_: type, max_length: int, contains: list):
    def decor(func):
        def wrapper(*args, **kwargs):
            for arg in args:
                if type(arg) is not type_:
                    print("Wrong type")
                    return False
                if len(arg) > max_length:
                    print("Very long")
                    return False
                for item in contains:
                    if item not in arg:
                        print("Contain error")
                        return False
            return func(*args, **kwargs)
        return wrapper
    return decor


@arg_rules(type_=str, max_length=15, contains=['05', '@'])
def create_slogan(name: str) -> str:

    return f"{name} drinks pepsi in his brand new BMW!"


if __name__ == '__main__':
    assert create_slogan('johndoe05@gmail.com') is False
    assert create_slogan('S@SH05') == 'S@SH05 drinks pepsi in his brand new BMW!'