# Santa floor
a = open('2015/2015-1-input.txt','r')

f = a.read()
a.close()

up = f.count('(')
down = f.count(')')

ans = up - down

print(ans)