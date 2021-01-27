class Parent:
    def __init__(self):
        print('Parent initialized')


class Child(Parent):
    def __init__(self):
        print('Child initialized')

    def get_data(self):
        print('a')


class Child2(Child):
    def __init__(self):
        print('Child2 initialized')

    def get_data(self):
        print('b')


c = Child2()
c.get_data()
