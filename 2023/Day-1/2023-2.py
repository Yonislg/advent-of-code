import re

f = open('2023/Day-1/2023-1-input.txt','r')

# f = [
#     'two1nine',
# 'eightwothree',
# 'abcone2threexyz',
# 'xtwone3four',
# '4nineeightseven2',
# 'zoneight234',
# '7pqrstsixteen'
# ]

def cipherize(line):
    nums = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

    newline = line
    for idx, x in enumerate(nums):
        newline = re.sub(x, str(idx+1),newline)
    
    return newline

ans = 0
for row in f:
    for i in range(len(row)):
        if row[i].isdigit():
            dec = row[i]
            break
        elif i > 1:
            if i + 4 > len(row):
                c = len(row)
            else:
                c = i + 4 
            for b in range(i,c):
                a = cipherize(row[i-2:b])
                if a.isdigit():
                    dec = a
                    break
            if a.isdigit():
                break

    ans += int(dec)*10

    for i in range(-1,-len(row)-1,-1):
        if row[i].isdigit():
            sing = row[i]
            break
        elif i < - 2:
            if i - 4 < -len(row):
                c = -len(row)
            else:
                c = i - 4
            for b in range(i,c,-1):
                if (i + 3 == 0):
                    a = cipherize(row[b:])
                else:
                    a = cipherize(row[b:i+3])
                if a.isdigit():
                    break
            if a.isdigit():
                sing = a
                break
    ans += int(sing)
    # print(dec+sing)

print(ans)

f.close()