example = '2333133121414131402'

f = open('2024/Day-9/2024-9-input.txt','r')
puzzle_input = f.read()
f.close()
print(len(example))


def checksum(diskmap):
    input =[]
    for char in diskmap:
        input.append(int(char))
    
    sum = 0
    fileID = 0
    blockID = int((len(input)-1)/2)
    maxID = 0
    for j in range(blockID+1):
        maxID += input[j*2]
    # print(maxID)
    n = 0
    while fileID <= maxID-1:
        block = input[n]
        # print(n,fileID,block,blockID,sum)
        if n%2==0:
            for i in range(int(block)):
                sum += fileID*int(n/2)
                fileID +=1
                if fileID >= maxID-1:
                    break
        else:
            for ii in range(int(block)):
                if input[-1] == 0:
                    blockID -=1
                    input.pop(-1)
                    input.pop(-1)
                sum += fileID*blockID
                fileID +=1
                input[-1] -= 1
                if fileID >=maxID-1:
                    break

        n +=1
    return sum

print(checksum(puzzle_input))

# print(len(example),len(puzzle_input))

# def diskmap(input):
#     files = []
#     empty = []
#     empty_blocks = 0
#     for n, digit in enumerate(input):
#         digit = int(digit)
#         if n%2 == 1:
#             empty_blocks += digit
#             empty.append(digit)
#         else:
#             files.append([int(n/2),digit])
#     filled = []
#     nowait = True
#     while empty_blocks > 0:
#         if nowait:
#             filled.append(files[0])
#             files.pop(0)
#         print(files,empty_blocks)
#         print(empty)
#         free = empty[0]
#         fileID = files[-1][0]
#         if files[-1][1] > free:
#             filled.append([fileID,free])
#             files[-1][1] -= free
#             empty.pop(0)
#             nowait = True
#             empty_blocks -= free
#         elif files[-1][1] == free:
#             filled.append([fileID,free])
#             files.pop(-1)
#             empty.pop(0)
#             nowait = True
#             empty_blocks -= free
#         elif files[-1][1] < free:
#             filled.append([fileID,free])
#             empty[0] -= files[-1][1]
#             nowait = False
#             empty_blocks -= files[-1][1]
#             files.pop(-1)
#     return filled

