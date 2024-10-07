# https://adventofcode.com/2023/day/1
# Santa receives a code where lines contain numbers and letters.
# The first and last digit of each line form a two digit number, the callibration value.
# The assignment is to find this number for each line and  add them all.

f = open('2023/Day-1/2023-1-input.txt','r')

test_example = ['1abc2',
'pqr3stu8vwx',
'a1b2c3d4e5f',
'treb7uchet']

# In this example, the calibration values of these four lines are 12, 38, 15, and 77. Adding these together produces 142.

# The approach is to iterate forwards and backwards over each row to find the first (and last) numbers
def num_finder(message):
    a = 0
    for row in message:
        for i in row:
            if i.isdigit():
                a += int(i)*10
                break

        for i in reversed(row):
            if i.isdigit():
                a += int(i)
                break
    return a

if (num_finder(test_example) == 142):
    print('code works with example')

ans = num_finder(f)
print('The puzzle answer is:', ans)


f.close()