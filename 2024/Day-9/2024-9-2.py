example = '2333133121414131402'

f = open('2024/Day-9/2024-9-input.txt','r')
puzzle_input = f.read()
f.close()

def filenums(group,start,space):
    end = int(space)
    group.append([start + k for k in range(end)])
    start += end
    return group, start

def checksum(diskmap):
    input =[]
    for char in diskmap:
        input.append(int(char))
    
    sum = 0

    blocks =[]
    empty=[]
    
    j = 0
    for i in range(len(diskmap)):
        if i%2==0:
            blocks, j = filenums(blocks, j, diskmap[i])
        else:
            empty, j = filenums(empty, j, diskmap[i])
    
    
    for n in range(len(blocks)-1,-1,-1):
        block = blocks[n]
        potential = [space for space in empty if len(space) >= len(block)]
        if len(potential)>0 and potential[0][0] < block[0]:
            for l in range(len(block)):
                sum += n * potential[0][0]
                potential[0].pop(0)
        else:
            for l in range(len(block)):
                sum += n * block[l]  

                  
            

    return sum

print(checksum(puzzle_input))