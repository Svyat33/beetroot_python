# Lesson 11
# Task 1. School
#
# Make a class structure in python representing people at school. Make a
# base class called Person, a class called Student, and another one called
# Teacher. Try to find as many methods and attributes as you can which
# belong to different classes, and keep in mind which are common and which
# are not. For example, the name should be a Person attribute, while
# salary should only be available to the teacher.

class Person:
    def __init__(self, name_f, name_l, age, sex, parking_employyes, key_card=True):
        self.name_f = name_f
        self.name_l = name_l
        self.age = age
        self.sex = sex
        self.parking_employyes = parking_employyes
        self.key_card = key_card
        pass


class Teacher(Person):
    def __init__(self, name_f, name_l, age, sex, parking_employyes, key_card, salary, hiring_date):
        super().__init__(name_f, name_l, age, sex, parking_employyes, key_card)
        self.salary = salary
        self.hiring_date = hiring_date
        self.key_card = True


class Student(Person):
    def __init__(self, name_f, name_l, age, sex, key_locker, elective=None):
        super().__init__(name_f, name_l, age, sex)
        self.key_locker = key_locker
        self.elective = elective
        pass
