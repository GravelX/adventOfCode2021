import os
import numpy as np

file_path = os.path.join(os.path.dirname(__file__), "input.txt")

with open(file_path) as f:
    data = f.readline()

dbrs = data.split(",")

fishies = []
for value in dbrs:
    fishies.append(int(value))

fishies = np.array(fishies)
fish_par_dbr = np.zeros(9, dtype=float)

for i in range(0,9):
    fish_par_dbr[i] = np.count_nonzero(fishies == i)


def simulation_tick(existing_fish):
    # count how many new fish will be born#
    new_fish = existing_fish[0]
    # all fishes get older
    regular_cycle = existing_fish[:7]
    regular_cycle = np.roll(regular_cycle, -1)
    age_7 = existing_fish[7]
    age_8 = existing_fish[8]
    regular_cycle[6] += age_7

    return np.append(np.append(regular_cycle, age_8), new_fish)


simulation_days = 256

for i in range(0, simulation_days):
    fish_par_dbr = simulation_tick(fish_par_dbr)
    print("Day",i,": There are now", np.sum(fish_par_dbr), "lantern fish!")
