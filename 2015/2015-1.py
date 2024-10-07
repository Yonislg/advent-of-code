#  https://adventofcode.com/2015/day/1
# Santa receiives a coded message which tells him which floor to go to. 
# He starts on the ground floor (floor 0) and then follows the instructions one character at a time.
# An opening parenthesis, (, means he should go up one floor, and a closing parenthesis, ), means he should go down one floor
# To what floor do the instructions take Santa?

# Open instructions
a = open('2015/2015-1-input.txt','r')

f = a.read()
a.close()

up = f.count('(')
down = f.count(')')

# print final floor
ans = up - down

print(ans)