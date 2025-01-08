import re

example1 = ['0123',
'1234',
'8765',
'9876']

f2 = open('2024/Day-10/example2.txt','r')
example2 = f2.read().split('\n')
f2.close()

f3 = open('2024/Day-10/example3.txt','r')
example3 = f3.read().split('\n')
f3.close()

f4 = open('2024/Day-10/example4.txt','r')
example4 = f4.read().split('\n')
f4.close()

f5 = open('2024/Day-10/example5.txt','r')
example5 = f5.read().split('\n')
f5.close()



def trailHeadCounter(maze):
    sum = 0
    zeros = []
    for y,row in enumerate(maze):
        matches = re.finditer('0',row)
        for match in matches:
            x,_ = match.span()
            # print(x,y)
            zeros.append((y,x))

    for zero in zeros:
        sum += stepper('0',zero,maze)
    return sum
        

            
def stepper(val,pos,maze):
    dim1 = len(maze)
    dim2 = len(maze[0])
    sum = 0
    dirs = [[0,1],[1,0],[-1,0],[0,-1]]
    if (int(val)<9):
        next = str(int(val)+1)
        for dir in dirs:
            # print(dir)
            newpos = [pos[0] + dir[0], pos[1]+dir[1]]
            if 0 <= newpos[0] < dim1 and 0 <= newpos[1] < dim2:
                newval = maze[newpos[0]][newpos[1]]
                # print(newpos)
                if newval==next:
                    # print(newval)
                    sum += stepper(newval,newpos,maze)
                else:
                    continue
    if (int(val)==9):
        sum = 1
    return sum

for example in example1, example2, example3, example4, example5:
    print(trailHeadCounter(example))
