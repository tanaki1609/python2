i = open('input.txt')
o = open('output.txt','w')
t = i.read()
o.write(str(int(t)+1))
