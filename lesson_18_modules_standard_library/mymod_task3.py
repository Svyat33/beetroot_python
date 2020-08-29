# count_lines(name) function that reads an input file and counts the number
# of lines in it (hint: file.readlines() does most of the work for you, and
# `len` does the rest)

# count_chars(name) function that reads an input file and counts the number
# of characters in it (hint: file.read() returns a single string)

# test(name) function that calls both counting functions with a given input
# filename. Such a filename generally might be passed-in, hard-coded, input
# with raw_input, or pulled from a command-line via the sys.argv list; for
# now, assume it’s a passed-in function argument.

import os, sys

FILE = 'test.txt'
# TODO: Вынести отдельным методом чтение файла



# Counting lines
def count_lines(file_name) -> int:
    """
    counting lines in file
    :param: file_name: Name of file
    :return: quantity of lines
    """
    with open(file_name, "r") as f:
        cnt = 0
        for line in f:
            # print(line)
            cnt += 1
        return cnt


# Counting lines (another variation)
def count_lines2(file_name) -> int:
    """
    counting lines in a file
    :param: file_name: Name of file
    :return: quantity of lines
    """
    with open(file_name, "r") as f:
        quantity = len(f.readlines())
        return quantity


def count_chars(file_name) -> int:
    """
    counting chars in a file
    :param: file_name: Name of file
    :return: quantity of chars
    """
    with open(file_name, "r") as f:
        quantity = len(f.read())
        return quantity

def test(file_name):
    # file_dir = os.path.dirname(file_name)
    # sys.path.append(file_dir)

    lines, chars = count_lines(file_name), count_chars(file_name)
    return f"There are {lines} lines and {chars} chars in a {file_name}\n"


if __name__ == '__main__':
    # Checking count_lines
    print(f"There are {count_lines(FILE)} lines in a {str(FILE)}.")
    print(f"There are {count_lines2(FILE)} lines in a {str(FILE)}.")

    # Checking count_chars
    print(f"There are {count_chars(FILE)} chars in a {str(FILE)}.")

    # Checking test
    print(test(FILE))

    # # Checking dir
    # print(this_dir)
    # sys.path.append(this_dir)
    # print(sys.path)
    print(os.path.dirname(FILE))
    var = sys.path
    print(var)
