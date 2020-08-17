#  lesson_8_try_except.
#
#  Task 1
#  Write a function called oops that explicitly raises an IndexError
#  exception when called. Then write another function that calls
##  oops inside a try/except state­ment to catch the error.
#  What happens if you change oops to raise KeyError instead of IndexError?
'''При изменении параметра raise, получается следующее:
# если IndexError как таковой, является TRUE, то есть действительно ошибка в индексе, то в начале
выполняется код цикла, а потом уже мы получаем наш raise.

# если же значением будет KeyError, хотя по факту там IndexError, то мы получаем в начале вывод ошибки,
а потом уже результаты выполнения цикла while.

# Я не могу точно сформулировать механику всего этого процесса, но возможно это как то подвязно под return
ф-ции или под особенность raise.

# сама ошибка в обоих случаях остаётся прежней IndexError: list index out of range. Вероятно, что
независимо от указанного raise, ошибка всё равно как то хэндлится.

# П. С. Вышеуказанный поток сознания, по моим ощущениям, прямо на грани какой то "бредовой теории заговора", но
порядок вывода, то всё равно меняется.
'''


def oops():
    # Change on IndexError or KeyError
    raise KeyError


def some_foo():
    num_list = [1, 2, 3, 4]
    i = 0
    try:
        while i <= len(num_list)-1:
            i += 1
            print(f'i: {i}')
    except:
        oops()
    #  For running without errors need next changes: num_list[i-1]
    return num_list[i]


if __name__ == "__main__":
    print(some_foo())


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
