#  lesson_8_try_except. Task 1
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

# П. С. Вышеуказанный поток сознания, по моим ощущениям, прямо на грани какой то бредовой теории заговора, но
порядок вывода, то всё равно меняется.
'''


def oops():
    # Change on IndexError or KeyError
    raise KeyError


def some_foo():
    num_list = [1, 2, 3, 4]
    print(f'длина списка: {len(num_list)}')
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