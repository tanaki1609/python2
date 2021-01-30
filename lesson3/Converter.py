"""
У вас есть класс Time с состоянием time, который обозначает секунды.
У вас должно быть 2 метода. Один переводит в минуты, второй в часы.
Пример-230 секунд переводит 3:50 и 0:3:50
"""
class Time:
    def __init__(self):
        self.time = int(input('Enter a number: '))

    def convert_to_minutes(self):
        print(f'{self.time // 60}:{self.time % 60}')


time = Time()
time.convert_to_minutes()
