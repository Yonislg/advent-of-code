import re

f = open('2024/Day-3/2024-3-input.txt','r')
puzzle_input = f.read()
f.close()

example = 'xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5)mul(,r))'

mulls = re.findall('mul\(\d+,\d+\)',puzzle_input)

sum = 0
for mul in mulls:
    s1, s2 = re.findall('\d+',mul)
    sum += int(s1)*int(s2)

print(sum)

oneline = ''.join(puzzle_input.split('\n'))

filtered_data = re.split("don't\(\).*?do\(\)",oneline)
refilter = re.split("don't\(\).*",''.join(filtered_data))
print(refilter)

mulls = re.findall('mul\(\d+,\d+\)',refilter[0])

sum = 0
for mul in mulls:
    s1, s2 = re.findall('\d+',mul)
    sum += int(s1)*int(s2)

print(sum)