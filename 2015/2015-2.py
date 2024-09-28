a = open('2015/2015-1-input.txt','r')

f = a.read()
a.close()

idx = 0
lvl = 0
basement = 0

for x in f:
    idx += 1
    if x =='(':
        lvl += 1
    elif x == ')':
        lvl -= 1
    
    if lvl < 0:
        basement = idx
        break

print(basement)
        
