# Lesson 18
# Task 2. The sys module.
# The “sys.path” list is initialized from the PYTHONPATH environment variable.
# Is it possible to change it from within Python? If so, does it affect where
# Python looks for module files? Run some interactive tests to find it out.

'''
При запуске скрипта в папке с другим именем, в строке импорта пользовательского
модуля module_task2, нужно изменить "lesson_18_modules_standard_library"
на имя папки, в которой он находится
'''
from lesson_18_modules_standard_library.task2.module_task2 import module_dir
from sys import path

# print(f"\nПуть к текущему файлу: \n{__file__}")

# print(f"\nДиректория модуля запущенная в {__file__}:\n{module_dir}")

print(f"\nСписок системных $PATH до внесения изменений:\n{path}")

path.append(module_dir)
print(f"\nСписок системных $PATH ПОСЛЕ внесения изменений:\n{path}")

# Если путь sys.path ну будет изменён, появится ошибка импорта модуля
import module_task2

# Я так понял, что изменения сделанные таким способом не вносятся в sys.path
# перманетно, так что удаление вроде как и не нужно
path.remove(str(module_dir))
print(f"\nСписок системных $PATH ПОСЛЕ ОТКАТА изменений:\n{path}")