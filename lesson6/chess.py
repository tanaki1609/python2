import re

i = open('input.txt')
o = open('output.txt','w')
t = i.read()
if not (re.findall("[A-H][1-8]-[A-H][1-8]", t)):
    o.write('ERROR')
else:
    ch1 = ord(t[0])
    a = int(t[1])
    ch2 = ord(t[3])
    b = int(t[4])
    if abs(ch1 - ch2) == 1 and abs(a - b) == 2:
        o.write('YES')
    elif abs(ch1 - ch2) == 2 and abs(a - b) == 1:
        o.write('YES')
    else:
        o.write('NO')