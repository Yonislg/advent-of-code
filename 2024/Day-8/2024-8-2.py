import re
import copy

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
                secondco = coordinates[ii]
                # print(firstco,secondco)
                for j in range(2):
                    distance[j] = firstco[j] - secondco[j]
                antinodes = nodulator(firstco, 1, distance, dimension, antinodes)
                antinodes = nodulator(secondco, -1, distance, dimension, antinodes)
                
    return antinodes                

def nodulator(innode, dir, distance, dimension, antinodes):
    k = 0
    node = copy.copy(innode)
    while -1 < innode[0] + k* distance[0] <dimension and -1 < innode[1] + k* distance[1] <dimension:
        node = list(node)
        for j in range(2):
            node[j] = innode[j] + k * distance[j]
        node = tuple(node)
        if node not in antinodes:
            antinodes.append(node)
        k += dir
    return antinodes


antennas,_ = antennasort(puzzle_input)
antinodes = antinodalize(puzzle_input)
print(antinodes)
print(len(antinodes))
print(antennas)
for antenna in antennas:
    coordinates = antennas[antenna]
    for coordinate in coordinates:
        if coordinate not in antinodes:
            print(coordinate)