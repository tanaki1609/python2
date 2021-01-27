class Person:
    def can_brethe(self):
        print('breathe')


class Robot:
    def can_kill(self):
        print('kill')


class PoliceMan:
    def can_arrest(self):
        print('arrest')


class RoboCop(PoliceMan, Robot, Person):
    pass


print(RoboCop.mro())
