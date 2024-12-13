import re

f = open('2024/Day-4/2024-4-input.txt','r')
puzzle_input = f.read().split('\n')
f.close()
puzzle_input.pop(-1)

example = [
    'MMMSXXMASM',
'MSAMXMSMSA',
'AMXSXMAAMM',
'MSAMASMSMX',
'XMASAMXAMM',
'XXAMMXXAMA',
'SMSMSASXSS',
'SAXAMASAAA',
'MAMMMXMMMM',
'MXMXAXMASX']

def rotate90(mat):
    n = len(mat)

    # Initialize the result matrix with zeros
    res = [[0] * n for _ in range(n)]
    lst = []

    # Flip the matrix clockwise using nested loops
    for i in range(n):
        for j in range(n):
            res[j][n - i - 1] = mat[i][j]

    # flatten
    for i in range(n):
        lst.append(''.join(res[i]))

    return lst

def rotate45(mat):

    n = len(mat)

    m = n

    res = []
    # Counter Variable
    ctr = 0
    while(ctr < 2 * n-1):
        lst = []
 
        # Iterate [0, m]
        for i in range(m):
 
                # Iterate [0, n]
            for j in range(n):
 
                # Diagonal Elements
                # Condition
                if i + j == ctr:
 
                    # Appending the
                    # Diagonal Elements
                    lst.append(mat[i][j])
        res.append(''.join(lst))

        ctr += 1    

    return res

def row_check(row):
    forward = re.findall('MAS',row)
    backward = re.findall('SAM',row)
    return (len(forward) + len(backward)) > 0

def mini_count(mat):
    vertical = rotate90(mat)
    diagnoal = rotate45(mat)
    diagnoal2 = rotate45(vertical)
    sum = 0

    if row_check(diagnoal[2]) and row_check(diagnoal2[2]):
        sum += 1
    return sum

def total_count(mat):
    sum = 0
    n = len(mat)
    print(n)
    for i in range(n-2):
        for j in range(n-2):
                mini_mat = ['000'] * 3
                for k in range(3):
                    mini_mat[k] = mat[i+k][j:j+3]
                sum += mini_count(mini_mat)

    return sum

print(total_count(puzzle_input))