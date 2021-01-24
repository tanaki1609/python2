class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def get_data(self):
        print(self.name, self.age)
obj1 = Student('aza', 18)
obj1.get_data()
obj2 = Student('Aidar', 22)
obj2.get_data()
