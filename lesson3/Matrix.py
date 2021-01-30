"""
Write a program that draws “modular rectangles” like the ones below.
The user specifies the
width and height of the rectangle, and the entries start at 0 and increase
typewriter fashion
from left to right and top to bottom, but are all done mod 10.
Below are examples of a 3 × 5
rectangle and a 4 × 8. NOTE: Use just ONE LOOP!!!
0 1 2 3 4
5 6 7 8 9
0 1 2 3 4

0 1 2 3 4 5 6 7
8 9 0 1 2 3 4 5
6 7 8 9 0 1 2 3
4 5 6 7 8 9 0 1
"""
class Matrix:
    def __init__(self):
        self.a, self.b = map(int, input('Enter a numbers: ').split())
    def get_matrix(self):
        counter = 0
        for i in range(self.a):
            for j in range(self.b):
                print(counter % 10, end=' ')
                counter += 1
            print()

matrix = Matrix()
matrix.get_matrix()