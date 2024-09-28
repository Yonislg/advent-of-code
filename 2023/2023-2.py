import re
f = [
    'two1nine',
'eightwothree',
'abcone2threexyz',
'xtwone3four',
'4nineeightseven2',
'zoneight234',
'7pqrstsixteen'
]

def cipherize(line):
    nums = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

    newline = line
    for idx, x in enumerate(nums):
        newline = re.sub(x, str(idx+1),newline)
    
    return newline


for row in f:
    print(row)
    for i in range(len(row)):
        if row[i].isdigit():
            print(row[i])
            break
        elif i > 1:
            for b in range(i,i+4):
                a = cipherize(row[i-2:b])
                if a.isdigit():
                    print(a)
                    break
            if a.isdigit():
                break

    for i in range(-1,-len(row),-1):
        if row[i].isdigit():
            print(row[i])
            break
        else:
            for b in range(i-2,i-6,-1):
                if (i == -1):
                    a = cipherize(row[b:])
                else:
                    a = cipherize(row[b:i+1])
                if a.isdigit():
                    print(a)
                    break
            if a.isdigit():
                break
   

            
