import os
import numpy as np

# load input
file_path = os.path.join(os.path.dirname(__file__), "input.txt")
with open(file_path) as f:
    data = f.read().splitlines()

octo_map = np.zeros((len(data), len(data[0])), dtype=int)

for i in range(len(data)):
    for j in range(len(data[0])):
        octo_map[i][j] = int(data[i][j])

def do_the_thing():
    flash_count = 0
    simulated_steps = 100000
    part1 = -1
    part2 = -1

    for step in range(simulated_steps):
        # (An octopus can only flash at most once per step.)
        flash_tracker = np.full(octo_map.shape, False, dtype=bool)
        done_flashing = False

        # First, the energy level of each octopus increases by 1
        uno = np.ones_like(octo_map, dtype=int)
        np.add(octo_map, uno, out=octo_map)

        # Then, any octopus with an energy level greater than 9 flashes.
        # This increases the energy level of all adjacent octopuses by 1,
        # including octopuses that are diagonally adjacent. If this causes
        # an octopus to have an energy level greater than 9, it also flashes.
        # This process continues as long as new octopuses keep having their
        # energy level increased beyond 9.
        new_flashes = []
        for i in range(octo_map.shape[0]):
            for j in range(octo_map.shape[1]):
                if octo_map[i][j] == 10:
                    new_flashes.append((i,j))

        while not done_flashing:
            if len(new_flashes) == 0:
                done_flashing = True
            else:
                new_flashes = compute_flashes(new_flashes, flash_tracker)
            #print(octo_map)

        # Finally, any octopus that flashed during this step has its energy
        # level set to 0, as it used all of its energy to flash.
        for i in range(octo_map.shape[0]):
            for j in range(octo_map.shape[1]):
                if flash_tracker[i][j]:
                    octo_map[i][j] = 0

        # Incrémente le nombre de flash
        flashes = np.count_nonzero(flash_tracker == True)
        if step <= 100:
            flash_count += flashes

        # part1
        if step == 99:
            part1 = flash_count

        # part2
        if (part2 == -1) and (flashes == octo_map.shape[0] * octo_map.shape[1]):
            part2 = step+1
            break

    return part1, part2
        
def compute_flashes(points, tracker):
    new_points = []

    for point in points:
        x = point[0]
        y = point[1]
        tracker[x, y] = True

        if x-1 >= 0:
            octo_map[x-1][y] += 1
            if octo_map[x-1][y] == 10:
                new_points.append((x-1, y))

            if y-1 >= 0:
                octo_map[x-1][y-1] += 1
                if octo_map[x-1][y-1] == 10:
                    new_points.append((x-1, y-1))

            if y+1 < octo_map.shape[1]:
                octo_map[x-1][y+1] += 1
                if octo_map[x-1][y+1] == 10:
                    new_points.append((x-1, y+1))   

        if x+1 < octo_map.shape[0]:
            octo_map[x+1][y] += 1
            if octo_map[x+1][y] == 10:
                new_points.append((x+1, y))

            if y-1 >= 0:
                octo_map[x+1][y-1] += 1
                if octo_map[x+1][y-1] == 10:
                    new_points.append((x+1, y-1))

            if y+1 < octo_map.shape[1]:
                octo_map[x+1][y+1] += 1
                if octo_map[x+1][y+1] == 10:
                    new_points.append((x+1, y+1))

        if y-1 >= 0:
            octo_map[x][y-1] += 1
            if octo_map[x][y-1] == 10:
                new_points.append((x, y-1))

        if y+1 < octo_map.shape[1]:
            octo_map[x][y+1] += 1
            if octo_map[x][y+1] == 10:
                new_points.append((x, y+1))

    return new_points
    
## Main ##
part1, part2 = do_the_thing()
print("Flashes after 100 iterations:", part1)
print("First step with all simultaneous flashes:", part2)