# https://adventofcode.com/2015/day/1
# Now, given the same instructions, find the position of the first character that causes him to enter the basement (floor -1). 
# The first character in the instructions has position 1, the second character has position 2, and so on.


a = open('2015/2015-1-input.txt','r')


f = a.read()
a.close()

idx = 0
lvl = 0
basement = 0

# A simple floor loop that keeps track of the current floor Santa is at.
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
        
