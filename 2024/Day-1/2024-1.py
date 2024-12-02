f = open('2024/Day-1/2024-1-input.txt','r')
puzzle_input = f.read().split('\n')
f.close()

example = ['3   4',
'4   3',
'2   5',
'1   3',
'3   9',
'3   3']

def sorted_lists(input, length):
    list1 = []
    list2 = []
    for row in input:
        if len(row) == 0:
            break
        list1.append(int(row[0:length]))
        list2.append(int(row[-length:]))
    list1.sort()
    list2.sort()
    return list1, list2

def distance(list1,list2):
    sum = 0
    for i in range(len(list1)):
        sum += abs(list1[i]-list2[i])
    return sum


list1, list2 = sorted_lists(example,1)
print(distance(list1,list2))

list3, list4 = sorted_lists(puzzle_input,5)

print(distance(list3,list4))

def similarity(list1,list2):
    sum = 0
    for i in range(len(list1)):
        for j in range(len(list2)):
            if list1[i] == list2[j]:
                sum += list1[i]
    return sum

print(similarity(list1,list2))
print(similarity(list3,list4))