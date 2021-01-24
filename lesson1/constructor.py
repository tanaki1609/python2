class Summa:
    def __init__(self, a, b):
        print('Initialized')
        self.first_arg = a
        self.second_arg = b

    def get_sum(self):
        print(self.first_arg+self.second_arg)

s = Summa(4, 5)
s.get_sum()

# def summa(a,b):
#     print(a+b)
#
# summa(2,3)
