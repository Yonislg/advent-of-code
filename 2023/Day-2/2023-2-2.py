import re
import numpy as np

example = ['Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green',
'Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue', 
'Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red',
'Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red',
'Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green']

f = open('2023/Day-2/2023-2-input.txt','r')

maxdict = {'red': 12, 'green': 12, 'blue': 14}

rdict = {}
ans = 0

for row in f:
    g, record = row.split(':')
    sets = record.split(';')
    game_max = {'red': 1, 'green': 1, 'blue': 1}
    for gset in sets:
        x = gset.split(',')
        for y in x:
            color = re.findall('[a-z]+',y)[0]
            number = int(re.findall('\d+',y)[0])
            if game_max[color] < number:
                game_max[color] = number
    ans += np.prod(list(game_max.values()))

print(ans)