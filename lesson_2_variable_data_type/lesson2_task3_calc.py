# Input numbers in this variables
a = 10
b = -20


if a != 0 and b != 0:
    result_add = a + b
    result_sub = a - b
    result_div = a / b
    result_mul = a * b
    result_exp = a ** b
    result_mod = a % b
    result_fl_div = a // b
    print(f'\n{a} + {b} = {result_add}'
          f'\n{a} - {b} = {result_sub}'
          f'\n{a} / {b} = {result_div}'
          f'\n{a} * {b} = {result_mul}'
          f'\n{a} ** {b} = {result_exp}'
          f'\n{a} % {b} = {result_mod}'
          f'\n{a} // {b} = {result_fl_div}')
elif a == 0:
    #a = int(0)
    result_add = a + b
    result_sub = a - b
    result_div = a / b
    result_mul = a * b
    result_exp = a ** b
    result_mod = a % b
    result_fl_div = a // b
    print(f'\n{a} + {b} = {result_add}'
          f'\n{a} - {b} = {result_sub}'
          f'\n{a} / {b} = {result_div}'
          f'\n{a} * {b} = {result_mul}'
          f'\n{a} ** {b} = {result_exp}'
          f'\n{a} % {b} = {result_mod}'
          f'\n{a} // {b} = {result_fl_div}')
elif b == 0:
    #b = int(0)
    result_add = a + b
    result_sub = a - b
    result_mul = a * b
    result_exp = a ** b
    print(f'\n{a} + {b} = {result_add}'
          f'\n{a} - {b} = {result_sub}'
          f'\n{a} / {b} = На \'0\' делить нельзя'
          f'\n{a} * {b} = {result_mul}'
          f'\n{a} ** {b} = {result_exp}'
          f'\n{a} % {b} = На \'0\' делить нельзя'
          f'\n{a} // {b} = На \'0\' делить нельзя')
else:
    print('Что то пошло не так')


'''
Комментарий преподавателя:
elif a == 0:     a = int(0)  нижня стрічка приведення до int зайва, 
бо вище ти вже зробив порівняння з 0, і зрозуміло що вона 0, якщо 
інтерпретатор потрапив всередину даного блоку
'''