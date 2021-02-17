i = open('input.txt')
o = open('output.txt', 'w')
x = i.read().split()
n = list(map(int, x))[1:]
print(n)
