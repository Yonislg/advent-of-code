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
        else:
            for b in range(i+2,i+6):
                a = cipherize(row[i:b])
                if a.isdigit():
                    print(a)
                    print(i,b)
                    break
            if a.isdigit():
                break

            
