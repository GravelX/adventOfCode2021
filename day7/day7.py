import os
from numpy import inf

file_path = os.path.join(os.path.dirname(__file__), "input.txt")
with open(file_path) as f:
    data = f.readline()

crabs = [int(x) for x in data.split(",")]

def part1():
    best_gas = inf
    for i in range(min(crabs), max(crabs)):
        total_gas = 0
        for j in range(0, len(crabs)):
            total_gas += abs(i-crabs[j])
        if total_gas < best_gas:
            best_gas = total_gas

    print("Pt1 best gas:",best_gas)

def part2():
    best_gas = inf
    
    for i in range(min(crabs), max(crabs)+1):
        if i % 100 == 0:
            print("Computing shortest gas...",i,"out of",max(crabs),"positions tested...")
        total_gas = 0
        for j in range(0, len(crabs)):
            steps = abs(i-crabs[j])
            for k in range(1, steps+1):
                total_gas += k

        if total_gas < best_gas:
            best_gas = total_gas

    print("Pt2 best gas:",best_gas)

part1()
part2()