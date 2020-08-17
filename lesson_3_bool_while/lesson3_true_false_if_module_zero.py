# Пременная которую проверяем, делиться на 3 или 5 нет и вывести результат в bool
num = 18

# is_divided_by_3 = not num % 3 or False
# print(is_divided_by_3)
#
# is_divided_by_3_and_5 = not num % 3 and not num % 5 or False
# print(is_divided_by_3_and_5)

                        # нет остатка на 3 и нет остатка на 5
is_divided_by_3_second = not num % 3 and not num % 5
print(is_divided_by_3_second)
