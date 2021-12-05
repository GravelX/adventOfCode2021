import os
import numpy as np

def load_lines():
    file_path = os.path.join(os.path.dirname(__file__), "input.txt")
    lines = [] # x1, y1, x2, y2

    with open(file_path) as f:
        data = f.readlines()

    for line in data:
        points = line.split(" -> ")
        lines.append([int(points[0].split(",")[0]), int(points[0].split(",")[1]), int(points[1].split(",")[0]), int(points[1].split(",")[1])])

    return lines

def apply_lines(lines, compute_diagonals):
    # compute matrix dimensions and fill with zeros
    dim = np.amax(lines)
    matrix = np.zeros((dim+1, dim+1))

    # apply lines
    for line in lines:
        if (line[0] == line[2]): # ligne verticale
            for i in range(min(line[1], line[3]), max(line[1], line[3])+1):
                matrix[line[0], i] += 1
        elif (line[1] == line[3]): # ligne horizontale
            for i in range(min(line[0], line[2]), max(line[0], line[2])+1):
                matrix[i, line[1]] += 1
        else:  # diagonal
            if (compute_diagonals):
                if (line[0] < line[2]):
                    x = list(range(line[0], line[2]+1))
                else:
                    x = list(reversed(range(line[2], line[0]+1)))
                
                if (line[1] < line[3]):
                    y = list(range(line[1], line[3]+1))
                else:
                    y = list(reversed(range(line[3], line[1]+1)))

                if (len(x) != len(y)):
                    print("the fuck??")

                for i in range(0, len(x)):
                    matrix[x[i], y[i]] += 1

    return matrix

def count_overlaps(matrix):
    overlaps = 0
    for row in matrix:
        for value in row:
            if value > 1:
                overlaps += 1
    
    return overlaps

## MAIN ##
lines = load_lines()
matrix = apply_lines(lines, compute_diagonals=True)
print(count_overlaps(matrix))