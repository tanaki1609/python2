i = open('input.txt')
o = open('output.txt', 'w')
x = i.read().split()  # [5,30,......]
m = x[0]
n = []
for i in x[1:]:
    n.append(int(i))
l = [0 for i in range(-100, 101)]
for x in range(len(n)):
    num = n[x]
    l[num] += 1
new = []
for m in range(-100, 101):
    if l[m]:
        for n_ in range(l[m]):
            new.append(m)
for i in new:
    o.write(str(i))
    o.write(' ')