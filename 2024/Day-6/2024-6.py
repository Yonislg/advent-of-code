import re
import copy
import time
f = open('2024/Day-6/2024-6-input.txt','r')
puzzle_input = f.read().split('\n')
f.close()

f2 = open('2024/Day-6/example.txt','r')
example = f2.read().split('\n')
f2.close()



def information(input):
    guards = []
    start = []
    length = len(input)
    for y, row in enumerate(input):
        matches = re.finditer('#',row)
        for match in matches:
            x,_ = match.span()
            guards.append((x,y))
        pos = row.find('^')
        if pos > 0:
            start = [pos, y]
    return start, guards, length
        

def advance(position,direction,guards):
    ahead = [position[0] + direction[0],position[1] + direction[1]]
    check = tuple(ahead)
    if type(guards) == 'NoneType':
        print(guards)
    if check in guards:
        rot = [-direction[1], direction[0]]
        for i in range(2):
            direction[i] = rot[i]
        next = position
    else:
        next = ahead
    return next, direction

def explore(input):
    position, guards, length = information(input)
    direction = [0,-1]
    past = [position]
    options = []
    print(length)
    while 0 < position[0] < length-1 and 0 <position[1] < length-1:
        prev_position = copy.copy(position)
        position, direction = advance(position,direction,guards)
        if position not in past:
            past.append(position)
            match direction:
                case [1,0]: # look at [0,1]
                    rest_of_row = [tup for tup in guards if tup[0] == prev_position[0] and tup[1] > prev_position[1]]
                case [0,1]: # look at [-1,0]
                    rest_of_row = [tup for tup in guards if tup[1] == prev_position[1] and tup[0] < prev_position[0]]
                case [-1,0]: # look at [0,-1]
                    rest_of_row = [tup for tup in guards if tup[0] == prev_position[0] and tup[1] < prev_position[1]]
                case [0,-1]: # look at [1,0]
                    rest_of_row = [tup for tup in guards if tup[1] == prev_position[1] and tup[0] > prev_position[0]]
            if len(rest_of_row)>0:
                options.append((tuple(position), tuple(prev_position), tuple(direction)))
    return past, options
# part 2


def explorev2(position, direction, guards, length):
    check = False
    past_turns = [(position,direction)]
    position = list(position)
    direction = list(direction)
    while 0 < position[0] < length-1 and 0 <position[1] < length-1:
        prev_direction = copy.copy(direction)
        position, direction = advance(position, direction,guards)
        if direction != prev_direction:
            # print(past_turns)
            # print((tuple(position), tuple(direction)) in past_turns)
            if (tuple(position), tuple(direction)) in past_turns:
                return True
            past_turns.append((tuple(position), tuple(direction)))
            match direction:
                case [1,0]:
                    rest_of_row = [tup for tup in guards if tup[1] == position[1] and tup[0] > position[0]]
                case [0,1]:
                    rest_of_row = [tup for tup in guards if tup[0] == position[0] and tup[1] > position[1]]
                case [-1,0]:
                    rest_of_row = [tup for tup in guards if tup[1] == position[1] and tup[0] < position[0]]
                case [0,-1]:
                    rest_of_row = [tup for tup in guards if tup[0] == position[0] and tup[1] < position[1]]
            if len(rest_of_row)==0:
                break

    return check

def brutus(options,input):
    position, guards, length = information(input)
    answer = 0
    ct = 0
    for option in options:
        # print(option)
        guards.append(option[0])
        ct +=1
        if explorev2(option[1], option[2], guards, length):
            answer += 1
        guards.remove(option[0])
        # if ct%500 == 0:
        #     print(ct,answer)
        
    return answer


        

p1, opt1 = explore(example)
p2, opt2 = explore(puzzle_input)


print(brutus(opt1,example))
print(len(p1),len(opt1))
# print(opt1)
print(len(p2),len(opt2))

start = time.perf_counter()
ans = brutus(opt2, puzzle_input)
end = time.perf_counter()
print('Number of obsutrction positions:',ans)
t = end - start

print('Solution found in: ', t, 'seconds')
