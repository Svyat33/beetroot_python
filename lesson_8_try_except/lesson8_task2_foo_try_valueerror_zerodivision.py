#  Task 2
#  Write a function that takes in two numbers from the user via input(),
#  call the numbers a and b, and then returns the value of squared a divided by b,
#  construct a try-except block which raises an exception if the two values given
#  by the input function were not numbers, and if value b was zero (cannot divide
#  by zero).
def foo(arg1, arg2):
    try:
        ret = a ** 2 / b
        return ret
    except ZeroDivisionError:
        print('Dividing by Zero is unacceptable')
        exit(1)


def inp_check():
    try:
        a = int(input(f'Please, enter value for numeric value for "a": '))
        b = int(input(f'Please, enter value for numeric value for "b": '))
        # print('Numbers accepted')
        return a, b
    except ValueError:
        print('Values for "a" and "b" must be only numeric')
        exit(1)


if __name__ == '__main__':
    a, b = inp_check()
    result = foo(a, b)
    print(result)
