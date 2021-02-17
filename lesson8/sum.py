i = open('input.txt')
x = i.read().split() # [5,30,......]
n = list(map(int, x))
o = open('output.txt', 'w')
sum = n[0]+n[1]
print(sum)
o.write(str(sum))