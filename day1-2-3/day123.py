import os
import numpy as np

def day1(part):
    file_path = os.path.join(os.path.dirname(__file__), "input_1.txt")
    with open(file_path) as f:
        data = f.readlines()

    depths = [int(x.strip()) for x in data]
    increases = 0

    if part == 1:
        for i in range(1, len(depths)):
            if (depths[i] > depths[i - 1]):
                increases += 1
    elif part == 2:
        sums = []
        for i in range(1, len(depths)-1):
            sums.append(depths[i-1] + depths[i] + depths[i+1])
        
        for i in range(1, len(sums)):
            if (sums[i] > sums[i -1]):
                increases += 1

    return increases

def day2(part):
    file_path = os.path.join(os.path.dirname(__file__), "input_2.txt")
    with open(file_path) as f:
        data = f.readlines()

    h_pos = 0
    depth = 0

    if part == 1:
        for instruction in data:
            value = int(instruction.split(" ")[1])

            if "up" in instruction:
                depth -= value
            elif "down" in instruction:
                depth += value
            elif "forward" in instruction:
                h_pos += value
            else:
                print("Unknown instruction encountered :",instruction)

    elif part == 2:
        aim = 0
        for instruction in data:
            value = int(instruction.split(" ")[1])

            if "up" in instruction:
                aim -= value
            elif "down" in instruction:
                aim += value
            elif "forward" in instruction:
                h_pos += value
                depth += aim * value
            else:
                print("Unknown instruction encountered :",instruction)

    return h_pos * depth

def find_ls_ratings(binary_data, position, most_common):
    if most_common:
        counts = np.bincount(binary_data[position])
        if counts[0] == counts[1]:
            bit = 1
        else:
            bit = np.argmax(np.bincount(binary_data[position]))
    else:
        counts = np.bincount(binary_data[position])
        if counts[0] == counts[1]:
            bit = 0
        else:
            bit = np.argmin(np.bincount(binary_data[position]))

    return bit

def filter_not_matching(arr, bit, position):
    keep_indices = []
    delete_indices = []

    for i, b in enumerate(arr[position]):
        if b == bit:
            keep_indices.append(i)

    for i in range(0, arr[position].size):
        if i not in keep_indices:
            delete_indices.append(i)

    new_arr = np.delete(arr, delete_indices, axis=1)

    return new_arr

def decode_final_bit(arr):
    binary_number = list(arr.transpose()[0])
    
    number = int("".join(str(x) for x in binary_number), 2)
    #print(binary_number, "--->", number)

    return number

def day3(part):
    answer = -1
    file_path = os.path.join(os.path.dirname(__file__), "input_3.txt")
    with open(file_path) as f:
        data = f.readlines()

    binary_data = []
    for line in data:
        binary_row = []
        for char in line.strip():
            binary_row.append(int(char))
        binary_data.append(binary_row)

    binary_data = np.array(binary_data)
    binary_data = binary_data.transpose() #[[all first bits],[all second bits],...]

    if part == 1:
        gamma = []
        epsilon = []

        for position in binary_data:
            gamma.append(np.argmax(np.bincount(position)))
            epsilon.append(np.argmin(np.bincount(position)))

        answer = int("".join(str(x) for x in gamma), 2) * int("".join(str(x) for x in epsilon), 2)

    elif part == 2:
        x, _ = binary_data.shape
        og_rating_candidates = binary_data
        cs_rating_candidates = binary_data
        og_rating = -1
        cs_rating = -1

        for i in range(0, x):
            nb_of_ogrc = og_rating_candidates.shape[1]
            nb_of_csrc = cs_rating_candidates.shape[1]

            if nb_of_ogrc > 1:
                most_common_bit = find_ls_ratings(og_rating_candidates, i, True)
                og_rating_candidates = filter_not_matching(og_rating_candidates, most_common_bit, i)

            if nb_of_csrc > 1:
                least_common_bit = find_ls_ratings(cs_rating_candidates, i, False)
                cs_rating_candidates = filter_not_matching(cs_rating_candidates, least_common_bit, i)

        nb_of_ogrc = og_rating_candidates.shape[1]
        nb_of_csrc = cs_rating_candidates.shape[1]

        if nb_of_ogrc == 1:
            og_rating = decode_final_bit(og_rating_candidates)
        else:
            print("Couldnt find a final candidate for Oxygene Generator Rating")

        if nb_of_csrc == 1:
            cs_rating = decode_final_bit(cs_rating_candidates)
        else:
            print("Couldnt find a final candidate for C02 Scrubber Rating")

        answer = og_rating * cs_rating

    return answer

## MAIN ##
# Day 1
print(day1(2), "measurements were larger than the previous.")
# Day 2
print(day2(2), "is the answer.")
# Day 3
print(day3(2), "is the power consumption.")