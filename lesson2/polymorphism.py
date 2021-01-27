"""
Полиморфизм — это способность программы выбирать различные
реализации при вызове операций с одним и тем же
названием.
"""


class Cat:
    def sing(self):
        print('meow')


class Dog:
    def sing(self):
        print('gav')


class Cow:
    def sing(self):
        print('muuu')


chores = [Cat(), Dog(), Cat(), Cow(), Cat(), Dog(), Dog()]
for i in chores:
    i.sing()
