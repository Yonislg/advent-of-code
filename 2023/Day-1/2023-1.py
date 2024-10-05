f = open('2023/Day-1/2023-1-input.txt','r')

# f = ['1abc2',
# 'pqr3stu8vwx',
# 'a1b2c3d4e5f',
# 'treb7uchet']

a = 0
for row in f:
    for i in row:
        if i.isdigit():
            a += int(i)*10
            break

    for i in reversed(row):
        if i.isdigit():
            a += int(i)
            break

print(a)




f.close()