i = open('input.txt')
o = open('output.txt', 'w')
x = i.read().split()  # [5,30,......]
n = list(map(int, x))[1:]
l = [0 for _ in range(-100, 101)]
for x in range(len(n)):
    num = n[x]
    l[num] += 1
s = ''
for m in range(-100, 101):
    if l[m]:
        s += ((str(m) + ' ') * l[m])
o.write(s)
