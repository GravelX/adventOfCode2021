import os

file_path = os.path.join(os.path.dirname(__file__), "input.txt")
with open(file_path) as f:
    data = f.readlines()

def part1():
    output_values = []
    for line in data:
        output = line.split(" | ")[1].split("\n")[0].split(" ")
        output_values.append(output)

    targets_count = 0
    for output in output_values: # 2 3 4 7 (1 7 4 8)
        for digit in output:
            if len(digit) in [2, 3, 4, 7]:
                targets_count += 1

    return targets_count

def part2():
    verbose = False
    total_sum = 0
    default_encoding = ["a", "b", "c", "d", "e", "f", "g"]
    unique_signals = []
    decoders = []
    digits = []

    for line in data:
        output_parts = line.split(" | ")
        unique_signals.append(output_parts[0].split(" "))
        digits.append(output_parts[1].split("\n")[0].split(" "))


    ## Logique de décution :
    """
    uniques nb of segments :
        "1":2(c,f),
        "4":4(b,c,d,f),
        "7":3(a,c,f),
        "8":7(*)

    appearences of segments in digits :
        a : 0, 2, 3, 5, 6, 7, 8, 9    (8)x
        b : 0, 4, 5, 6, 8, 9          (6)
        c : 0, 1, 2, 3, 4, 7, 8, 9    (8)x
        d : 2, 3, 4, 5, 6, 8, 9       (7)x
        e : 0, 2, 6, 8                (4)
        f : 0, 1, 3, 4, 5, 6, 7, 8, 9 (9)
        g : 0, 2, 3, 5, 6, 8, 9       (7)x

    deductions order :
        a from 7 - 1
        b from appearences in candidates (6, unique)
        e from appearences in candidates (4, unique)
        f from appearences in candidates (9, unique)
        c from appearences in candidates (8 and not a)
        d from deduction in 4 (minus b,c,f)
        g from deduction in 8 (minus all others)
    """
    for signals in unique_signals:
        solution = ["?", "?", "?", "?", "?", "?", "?"]
        one = ""
        seven = ""
        four = ""
        eight = ""
        appearences = [0, 0, 0, 0, 0, 0, 0, 0] # appearences of scrambled digits in unique signals

        for signal in signals:
            if len(signal) == 2:
                one = signal
            elif len(signal) == 3:
                seven = signal
            elif len(signal) == 4:
                four = signal
            elif len(signal) == 7:
                eight = signal

            for segment in signal:
                appearences[default_encoding.index(segment)] += 1
        
            
        for segment in seven:
            if segment not in one:
                solution[default_encoding.index("a")] = segment
                break
        
        for i,position in enumerate(appearences):
            if position == 6:
                solution[default_encoding.index("b")] = default_encoding[i]
            elif position == 4:
                solution[default_encoding.index("e")] = default_encoding[i]
            elif position == 8:
                if default_encoding[i] != solution[default_encoding.index("a")]:
                    solution[default_encoding.index("c")] = default_encoding[i]
            elif position == 9:
                solution[default_encoding.index("f")] = default_encoding[i]

        bcf = [solution[default_encoding.index("b")], solution[default_encoding.index("c")], solution[default_encoding.index("f")]]
        for segment in four:
            if segment not in bcf:
                solution[default_encoding.index("d")] = segment
                break

        for segment in eight:
            if segment not in solution:
                solution[default_encoding.index("g")] = segment
                break

        decoders.append(solution)

    # Calcule de la solution du puzzle
    regular_display = [
        "abcefg",  # 0
        "cf",      # 1
        "acdeg",   # 2
        "acdfg",   # 3
        "bcdf",    # 4
        "abdfg",   # 5
        "abdefg",  # 6
        "acf",     # 7
        "abcdefg", # 8
        "abcdfg"   # 9
    ]
    # Pour chaque output à décoder
    for i,number in enumerate(digits):
        value = ""
        # Pour chaque chiffre du nombre à décoder
        for digit in number:
            decoded_segments = []
            # Pour chaque segment du chiffre
            for segment in digit:
                decoded_segments.append(default_encoding[decoders[i].index(segment)])
            # Pour chaque série de segments d'un display normal
            for regular_segments in regular_display:
                perfect_match = True
                # Pour chaque segment décodé du chiffre
                for d_segment in decoded_segments:
                    if len(regular_segments) == len(decoded_segments):
                        if d_segment not in regular_segments:
                            perfect_match = False
                            break
                    else:
                        perfect_match = False
                        break
                if perfect_match:
                    value += str(regular_display.index(regular_segments))
                    break

        total_sum += int(value)

        if verbose:
            print("Processing line", i)
            print(" Input:", unique_signals[i])
            print(" Output:", digits[i])
            print(" Regular:", default_encoding)
            print(" Decoder:", decoders[i])
            print(" Decoded output :", value)

    return total_sum


## MAIN ##
print("Digits 1, 4, 7 and 8 appear",part1(),"times in the input.")
print("Total sum of decoded numbers is",part2())