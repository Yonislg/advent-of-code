from math import floor


f = open('2024/Day-5/2024-5-input.txt','r')
puzzle_input = f.read().split('\n')
f.close()

f2 = open('2024/Day-5/example.txt','r')
example = f2.read().split('\n')
f2.close()




def sort(input):
    before = {}
    after = {}
    update = []
    fullist = []

    for row in input:
        if len(row) == 5 and row[2] == '|':
            first_num = row[:2]
            second_num = row[3:]
            before.setdefault(first_num,[]).append(second_num)
            after.setdefault(second_num,[]).append(first_num)
        elif len(row) >3 and row[2] == ',':
            update.append(row.split(','))
    return before, after, update, fullist

def after_checker(row, rules):
    check = True
    for i in range(1,len(row)):
        el = row[i]
        if el not in rules:
            continue

        rule = rules[el]
        prelist = row[:i]
        for pre_el in prelist:
            if pre_el in rule:
                check = False
                break
        if not check:
            break
    return check

def rearrange(row, beforules,afterules):
    i = 1
    while i < len(row):
        el = row[i]
        rule = beforules[el]
        prelist = row[:i]
        for pre_el in prelist:
            if pre_el in rule:
                afters = [i]
                afters.extend([row.index(z) for z in row if z in afterules[el]])
                y = max(afters) + 1
                row.remove(pre_el)
                row.insert(y, pre_el)
                i -= 1
    
        i +=1

    return row



def update_check(update, beforules):
    sum = 0
    for row in update:
        if after_checker(row,beforules):
            midpos = floor(len(row)/2)
            sum += int(row[midpos])
    return sum

# def row_sort(row,fullist):
#     sorted = []
#     for el in fullist:
#         if el in row:
#             sorted.append(el)
#     return sorted

def update_fix(update,beforules, fullist):
    sum = 0
    for row in update:
        if not after_checker(row,beforules):
            sorted_row = rearrange(row, beforules, afterules)
            midpos = floor(len(sorted_row)/2)
            sum += int(sorted_row[midpos])
    return sum

beforules, afterules, update, fullist = sort(puzzle_input)

print(len(fullist))
print(after_checker(fullist,beforules))
print(len(update))
print(update_fix(update,beforules,fullist))

print(after_checker(fullist,beforules))

