# Lesson 11
# Task 2. Mathematician
#
# Implement a class Mathematician which is a helper class for doing math operations on lists
# The class doesn't take any attributes and only has methods:
#     square_nums (takes a list of integers and returns the list of squares)
#     remove_positives (takes a list of integers and returns it without positive numbers
#     filter_leaps (takes a list of dates (integers) and removes those that are not 'leap years'
'''
class Mathematician:

    pass

m = Mathematician()

assert m.square_nums([7, 11, 5, 4]) == [49, 121, 25, 16]

assert m.remove_positives([26, -11, -8, 13, -90]) == [-11, -8, -90]

assert m.filter_leaps([2001, 1884, 1995, 2003, 2020]) == [1884, 2020]
'''


class Mathematician:

    def square_nums(self, num_list):
        res = []
        i = 0
        while i <= len(num_list)-1:
            res.append(num_list[i] * num_list[i])
            i += 1
        return res

    def remove_positives(self, num_list):
        res = []
        for i in num_list:
            if i < 0:
                res.append(i)
            else:
                pass
        return res

    def filter_leaps(self, num_list):
        res = []
        for i in num_list:
            if i % 4 == 0:
                res.append(i)
            else:
                pass
        return res


if __name__ == '__main__':
    some_list_square_nums = [7, 11, 5, 4]
    some_list_remove_positive = [26, -11, -8, 13, -90]
    some_list_filter_leaps = [2001, 1884, 1995, 2003, 2020]
    m = Mathematician()

    print(f'Squared list is: {m.square_nums(some_list_square_nums)}\n')
    assert m.square_nums([7, 11, 5, 4]) == [49, 121, 25, 16]

    print(f'List {some_list_remove_positive} without positives is: {m.remove_positives(some_list_remove_positive)}\n')
    assert m.remove_positives([26, -11, -8, 13, -90]) == [-11, -8, -90]

    print(f'Among years {some_list_filter_leaps}, leap years are: {m.filter_leaps(some_list_filter_leaps)}')
    assert m.filter_leaps([2001, 1884, 1995, 2003, 2020]) == [1884, 2020]
