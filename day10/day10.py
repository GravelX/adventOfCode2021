import os

# load input
file_path = os.path.join(os.path.dirname(__file__), "input.txt")
with open(file_path) as f:
    data = f.read().splitlines()

def part1():
    error_total_cost = 0
    corrupted_lines = []
    opening_characters = ["[", "{", "(", "<"]
    closing_characters = ["]", "}", ")", ">"]
    error_costs = [57, 1197, 3, 25137]
    
    for i,line in enumerate(data):
        opened_state = []
        for character in line:
            if character in opening_characters:
                opened_state.append(character)
            elif character in closing_characters:
                if opened_state[-1] != opening_characters[closing_characters.index(character)]:
                    # line is corrupted
                    error_total_cost += error_costs[closing_characters.index(character)]
                    corrupted_lines.append(i)
                    break
                else:
                    opened_state.pop()
            else:
                print("Error")

    return error_total_cost, corrupted_lines

def part2(corrupted_ids):
    lines_scores = []

    # remove current corrupted lines
    for id in reversed(corrupted_ids):
        data.pop(id)

    opening_characters = ["[", "{", "(", "<"]
    closing_characters = ["]", "}", ")", ">"]
    repair_costs = [2, 3, 1, 4]

    for line in data:
        line_score = 0
        opened_state = []
        for character in line:
            if character in opening_characters:
                opened_state.append(character)
            elif character in closing_characters:
                opened_state.pop()
            else:
                print("Error")

        # repair line and compute score for this line
        for character in reversed(opened_state):
            line_score = line_score * 5
            line_score += repair_costs[opening_characters.index(character)]
        lines_scores.append(line_score)

    # return the middle score
    lines_scores.sort()
    return lines_scores[int(((len(lines_scores)-1)/2))]

## Main ##
err_cost, corrupted_lines = part1()
print("Error total cost:", err_cost)
print("Middle repair score is:", part2(corrupted_lines))

def test():
    line = "<{([{{}}[<[[[<>{}]]]>[]]"
    line_score = 0
    opened_state = []
    opening_characters = ["[", "{", "(", "<"]
    closing_characters = ["]", "}", ")", ">"]
    repair_costs = [2, 3, 1, 4]

    for character in line:
        if character in opening_characters:
            opened_state.append(character)
        elif character in closing_characters:
            opened_state.pop()
        else:
            print("Error")

    # repair line and compute score for this line
    print("What is still open:",opened_state)
    for character in reversed(opened_state):
        line_score = line_score * 5
        line_score += repair_costs[opening_characters.index(character)]

    print(line_score)

#test()