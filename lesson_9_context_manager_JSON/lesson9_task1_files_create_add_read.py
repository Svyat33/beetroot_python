# lesson_9_context_manager_JSON
'''Task 1.1 Files (create_write)'''
#
# Write a script that creates a new output file called myfile.txt and writes the string
# "Hello file world!" in it. Then write another script that opens myfile.txt, and reads and prints
# its contents. Run your two scripts from the system command line.
#
# Does the new file show up in the directory where you ran your scripts?
#
# What if you add a different directory path to the filename passed to open?
#
# Note: file write methods do not add newline characters to your strings; add an explicit ‘\n’ at
# the end of the string if you want to fully terminate the line in the file.
if __name__ == '__main__':
    with open('myfile.txt', 'w') as myfile_object:
        myfile_object.write("Hello file world!\n")

'''Task 1.2 Files (read / read_from_wrong_dir)'''
from os import path

if __name__ == '__main__':
    current_dir = path.dirname(__file__)
    print(current_dir)
    try:
        with open('myfile.txt', 'r') as myfile_object:
            file_print = myfile_object.read()
        print(file_print)
    except FileNotFoundError:
        print('Oops! File not found in this dir.')
    try:
        with open(path.join(current_dir, '/wrongfolder/myfile.txt')) as myfile_wrong_dir:
            file_print_wrong_dir = myfile_wrong_dir.read()
        print(file_print_wrong_dir)
    except FileNotFoundError:
        print('Oops! File not found in this dir.')

''' Возможно в вопросе "if you add a different directory path to the filename passed to open"
    и имелась ввиду ошибка FileNotFoundError. Просто я не нашёл исключение конкретно по отсутствующему
    пути, но вероятно это и не нужно. Убирая '/wrongfolder/'файл запускается. По идее всё верно. '''