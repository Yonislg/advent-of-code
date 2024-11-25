
import re
example = [
'467..114..',
'...*......',
'..35..633.',
'......#..@',
'617.......',
'.....+.58.',
'..592.....',
'......755.',
'...$.*....',
'.664.598..',
]
sum = 0

def gearfinder(row,rownum,start):
    gears = re.finditer('[*]', row)
    locs = [(rownum, gear.span()[0]+start) for gear in gears]
    return locs

def flatten(xss):
    return [x for xs in xss for x in xs]

def checkrows(row1, row2, row3,n,start):
    rowlist = [row1, row2, row3]
    symbolist = [gearfinder(row, n-1+i,start) for i,row in enumerate(rowlist) if len(gearfinder(row,n-1+i,start))>0]
    return flatten(symbolist)

f = open('2023/Day-3/2023-3-input.txt','r')
example = f.read().split('\n')
h = len(example)
l = len(example[0])
f.close()
print(example)
print(h,l)
geardict = {}


for n, row in enumerate(example):
    matches = re.finditer('\d+',row)
    for match in matches:
        start, end = match.span()
        start = max(0,start-1)
        end = min(l,end+1)
        num = match.group()
        top = example[max(0,n-1)][start:end]
        mid = example[n][start:end]
        bottom = example[min(h-1,n+1)][start:end]
        adjacent_gears = checkrows(top, mid, bottom,n,start)
        print(adjacent_gears)
        if len(adjacent_gears)>0:
            for gear in adjacent_gears:
                geardict.setdefault(gear,[]).append(num)

print(geardict)

for gear in geardict:
    gearnums = geardict[gear]
    if len(gearnums) == 2:
        no1 , no2 = [int(no) for no in gearnums]
        sum += no1*no2

print(sum)


            
