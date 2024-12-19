import re

f = open('2024/Day-8/2024-8-input.txt','r')
puzzle_input = f.read().split('\n')
f.close()

f2 = open('2024/Day-8/example.txt','r')
example = f2.read().split('\n')
f2.close()

def antennasort(input):
    dimension = len(input)
    antennas = {}
    for y,row in enumerate(input):
        matches = re.finditer('\w',row)
        for match in matches:
            antenna = match.group()
            x,_ = match.span()
            antennas.setdefault(antenna,[]).append((x,y))
    return antennas, dimension
        
def antinodalize(input):
    antennas, dimension = antennasort(input)
    antinodes = []
    for antenna in antennas:
        coordinates = antennas[antenna]
        num_of_coordinates = len(coordinates)
        for i in range(num_of_coordinates):
            firstco = coordinates[i]
            
            for ii in range(i+1, num_of_coordinates):
                distance = [0,0]
                node1 = [0,0]
                node2 = [0,0]
                secondco = coordinates[ii]
                print(firstco,secondco)
                for j in range(2):
                    distance[j] = firstco[j] - secondco[j]
                    node1[j] = firstco[j] + distance[j]
                    node2[j] = secondco[j] - distance[j]
                for node in [node1,node2]:
                    if -1 < node[0] <dimension and -1 < node[1] <dimension and node not in antinodes:
                        antinodes.append(node)
    return antinodes
                    



print(antennasort(puzzle_input))
antinodes = antinodalize(puzzle_input)
print(len(antinodes))