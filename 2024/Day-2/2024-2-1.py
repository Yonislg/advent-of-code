import numpy as np
import re

f = open('2024/Day-2/2024-2-input.txt','r')
puzzle_input = f.read().split('\n')
f.close()

example = ['7 6 4 2 1',
'1 2 7 8 9',
'9 7 6 2 1',
'1 3 2 4 5',
'8 6 4 4 1',
'1 3 6 7 9']

def parser(input):
    data = []
    for row in input:
        numbers = re.findall('\d+', row)
        integers = [int(num) for num in numbers]
        if len(integers) > 0:
            data.append(integers)
    return data

def safetey_check(data):
    sum = 0
    for row in data:
        l = len(row)
        first = np.array(row[:l-1])
        second = np.array(row[1:])
        diff = first - second
        if (all(4>diff) and all(diff>0)) or (all(diff<0) and all(diff>-4)):
            sum += 1
    return(sum)

test_data = parser(example)

print(safetey_check(test_data))

data = parser(puzzle_input)
print(data)

print(safetey_check(data))