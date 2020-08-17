# lesson_7_functions. Task 3
# A simple calculator.
# Create a function called make_operation, which takes
# in a simple arithmetic operator as a first parameter
# (to keep things simple let it only be ‘+’, ‘-’ or ‘*’)
# and an arbitrary number of arguments (only numbers) as
# the second parameter. Then return the sum or product of
# all the numbers in the arbitrary parameter. For example:
#
#     the call make_operation(‘+’, 7, 7, 2) should return 16
#     the call make_operation(‘-’, 5, 5, -10, -20) should return 30
#     the call make_operation(‘*’, 7, 6) should return 42


def make_operation(action, *args):
    def my_add(a, b):
        return a + b

    def my_sub(a, b):
        return a - b

    def my_mul(a, b):
        return a * b

    def my_div(a, b):
        return a / b

    actions_list = ['+', '-', '*', '/']

    if action in actions_list:
        print(f'ARGS имеет следующие значения: {args}, с длиной {len(args)} и типом {type(args)}')
        i = 0
        res = args[0]
        print(f'Первичный res равен: {res}')
        if action == '+':
            for i in args[1:]:
                res = my_add(res, i)
                print(f'при добавлении {i} к {res}, получен результат: {res}')
            return res
        elif action == '-':
            for i in args[1:]:
                res = my_sub(res, i)
                print(f'при вычитании {i} от {res}, получен результат: {res}')
            return res
        elif action == '*':
            for i in args[1:]:
                res = my_mul(res, i)
                print(f'при умножении {i} на {res}, получен результат: {res}')
            return res
        elif action == '/':
            try:
                for i in args[1:]:
                    res = my_div(res, i)
                    print(f'при делении {i} на {res}, получен результат: {res}')
            except ZeroDivisionError:
                print(f'На 0 делить нельзя')
            return res
        else:
            print('Был использован неправильный оператор')


if __name__ == "__main__":
    try:
        a = make_operation('*', 5, 5, 10, -20)
        print(a)
    except:
        print('Что то не получилось')
