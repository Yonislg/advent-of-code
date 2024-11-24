# https://adventofcode.com/2023/day/3
# If you can add up all the part numbers in the engine schematic, it should be easy to work out which part is missing.
# The engine schematic (your puzzle input) consists of a visual representation of the engine. 
# There are lots of numbers and symbols you don't really understand, but apparently any number adjacent to a symbol,
# even diagonally, is a "part number" and should be included in your sum. (Periods (.) do not count as a symbol.)

import re
# example = [
# '467..114..',
# '...*......',
# '..35..633.',
# '......#..@',
# '617.......',
# '.....+.58.',
# '..592.....',
# '......755.',
# '...$.*....',
# '.664.598..',
# ]
sum = 0

def symbolfinder(row):
    return len(re.findall('[^0-9^\.]', row)) > 0


def checkrows(row1, row2, row3):
    rowlist = [row1, row2, row3]
    symbolist = [symbolfinder(row) for row in rowlist]
    return any(symbolist)

symb = ['#', '$', '%', '&', '*', '+', '-', '/', '=', '@']
symb_test = [symbolfinder(it) for it in symb]
numz = []
blurb = []
f = open('2023/Day-3/2023-3-input.txt','r')
example = f.read().split('\n')
h = len(example)
l = len(example[0])
f.close()
print(example)
print(h,l)
for n, row in enumerate(example):
    print('row:',n)
    print(row)
    matches = re.finditer('\d+',row)
    for match in matches:
        start, end = match.span()
        num = match.group()
        top = example[max(0,n-1)][max(0,start-1):min(l,end+1)]
        mid = example[n][max(0,start-1):min(l,end+1)]
        bottom = example[min(h-1,n+1)][max(0,start-1):min(l,end+1)]
        if checkrows(top, mid, bottom):    
            sum += int(num)

print(sum)
