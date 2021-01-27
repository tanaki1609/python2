"""
Наследование — это возможность создания новых классов
на основе существующих. Главная польза от наследования —
повторное использование существующего кода.
"""


class Person:                # parent
    def can_breathe(self):
        print('i can breathe')

    def can_kill(self):
        print('i can kill')


class Doctor(Person):        #  child
    def can_heal(self):
        print('i can heal')

class Teacher(Person):
    def can_teach(self):
        print('i can teach')

t = Teacher()
t.can_breathe()
