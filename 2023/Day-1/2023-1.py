# https://adventofcode.com/2023/day/1
# Santa receives a code where lines contain numbers and letters.
# The first and last digit of each line form a two digit number, the callibration value.
# The assignment is to find this number for each line and  add them all.
import re
import time
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

        for id in range(len(row)-1,-1,-1):
            if row[id].isdigit():
                a += int(row[id])
                break
    return a

if (num_finder(test_example) == 142):
    print('code works with example')

start = time.perf_counter()
ans = num_finder(f)
end = time.perf_counter()
t1 = end - start
print('The puzzle answer is:', ans)

f.close()

def simple_num_finder(message):
    a = 0
    for row in message:
        nums = re.findall('\d',row)
        a+= int(nums[0]+nums[-1])
    return a


f = open('2023/Day-1/2023-1-input.txt','r')
start = time.perf_counter()
ans = simple_num_finder(f)
end = time.perf_counter()
print(ans)
f.close

t2 = end - start

print(t1,t2,(t1-t2)/t1*100)

