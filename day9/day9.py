import os
import numpy as np

# load input
file_path = os.path.join(os.path.dirname(__file__), "input.txt")
with open(file_path) as f:
    data = f.readlines()

height_map = np.full((len(data)+2, len(data[0])+1), 9, dtype=int) # +2 for borders (padding)

# fill numpy height map
for i in range(len(data)):
    for j in range(len(data[0])):
        if (j<len(data[i])):
            if data[i][j] != "\n":
                height_map[i+1][j+1] = int(data[i][j])

def part1():
    risk_level = 0
    
    # find low points and sum risk level
    for i in range (1, height_map.shape[0]-1):
        for j in range (1, height_map.shape[1]-1):
            if height_map[i][j] < height_map[i-1][j] and height_map[i][j] < height_map[i+1][j] and height_map[i][j] < height_map[i][j-1] and height_map[i][j] < height_map[i][j+1]:
                risk_level += (height_map[i][j]+1)

    return risk_level

def part2():
    # find the low points
    low_points = []
    for i in range (1, height_map.shape[0]-1):
        for j in range (1, height_map.shape[1]-1):
            if height_map[i][j] < height_map[i-1][j] and height_map[i][j] < height_map[i+1][j] and height_map[i][j] < height_map[i][j-1] and height_map[i][j] < height_map[i][j+1]:
                low_points.append((i,j))

    # for all non-nine values, find corresponding low point
    basins = [0 for i in range(len(low_points))]
    for i in range (1, height_map.shape[0]-1):
        for j in range (1, height_map.shape[1]-1):
            if height_map[i][j] != 9:
                x = i
                y = j
                while (x,y) not in low_points:
                    if height_map[x-1][y] < height_map[x][y]:
                        x -= 1
                    elif height_map[x+1][y] < height_map[x][y]:
                        x += 1
                    elif height_map[x][y-1] < height_map[x][y]:
                        y -= 1
                    elif height_map[x][y+1] < height_map[x][y]:
                        y += 1
                    else:
                        print("Error")
                # increment size of corresponding basin by 1
                basins[low_points.index((x,y))] += 1
    # compute answer
    basins.sort(reverse=True)
    return basins[0]*basins[1]*basins[2]

## Main ##
print("The sum of the risk levels of all low points on your heightmap is", part1())
print("Product of top 3 largest basins areas is", part2())