from os import O_RDONLY
from pathlib import Path

INPUT_FILE = Path(__file__).parent / "../input"
puzzle_input = INPUT_FILE.read_text().splitlines()
TEST_INPUT_FILE = Path(__file__).parent / "../test_input"
test_puzzle_input = TEST_INPUT_FILE.read_text().splitlines()

short_test_puzzle_input = "acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf"

"""
  0:      1:      2:      3:      4:
 aaaa    ....    aaaa    aaaa    ....
b    c  .    c  .    c  .    c  b    c
b    c  .    c  .    c  .    c  b    c
 ....    ....    dddd    dddd    dddd
e    f  .    f  e    .  .    f  .    f
e    f  .    f  e    .  .    f  .    f
 gggg    ....    gggg    gggg    ....

  5:      6:      7:      8:      9:
 aaaa    aaaa    aaaa    aaaa    aaaa
b    .  b    .  .    c  b    c  b    c
b    .  b    .  .    c  b    c  b    c
 dddd    dddd    ....    dddd    dddd
.    f  e    f  .    f  e    f  .    f
.    f  e    f  .    f  e    f  .    f
 gggg    gggg    ....    gggg    gggg
 
 1 is a subset of 0 3 4 7 8 9
 7 is a subset of 0 3 8 9
 4 is a subset of 8 9
 8 is a subset of nothing
 
 0 has 6
 1 has 2
 2 has 5
 3 has 5
 4 has 4
 5 has 5
 6 has 6
 7 has 3
 8 has 7
 9 has 6

 8-1 gives middle bar

 """


def process_input_line(line):
    wires, output = line.split(" | ")
    wires = ["".join(sorted(w)) for w in wires.split()]
    output = ["".join(sorted(o)) for o in output.split()]
    return wires, output


def count_easy_digits(data):
    easy_signals = [
        2,  # 1
        3,  # 7
        4,  # 4
        7,  # 8
    ]
    return len(list(filter(lambda x: len(x) in easy_signals, data)))


def sequence_easy_digits(data):
    easy_signals = {  # length: corresponding digit
        2: 1,
        3: 7,
        4: 4,
        7: 8,
    }
    found = dict()
    for entry in data:
        if easy_signals.get(len(entry)):
            found[entry] = easy_signals[len(entry)]
    return found


def part1(data):
    easy_count = 0
    for line in data:
        _, output = process_input_line(line)
        easy_count += count_easy_digits(output)
    return easy_count


def generate_solve_map(wires):
    easy_map = sequence_easy_digits(wires)

    found = {v: set(k) for k, v in easy_map.items()}
    remaining = set(wires) - set(easy_map.keys())

    bd_segment = found[4] - found[1]
    five_six_nine = set([r for r in remaining if bd_segment.issubset(r)])
    zero_two_three = set([r for r in remaining if not bd_segment.issubset(r)])

    found[5] = list(filter(lambda x: len(x) == 5, five_six_nine))[0]
    found[0] = list(filter(lambda x: len(x) == 6, zero_two_three))[0]

    zero_two_three.remove(found[0])
    found[3] = [r for r in zero_two_three if found[1].issubset(r)][0]
    found[2] = [r for r in zero_two_three if not found[1].issubset(r)][0]

    five_six_nine.remove(found[5])
    found[6] = [r for r in five_six_nine if not found[1].issubset(r)][0]
    found[9] = [r for r in five_six_nine if found[1].issubset(r)][0]

    # fix temporary sets. Need a better data structure for this
    for key, value in found.items():
        if isinstance(value, set):
            found[key] = "".join(sorted(value))

    return {v: k for k, v in found.items()}


def part2(data):
    total = 0
    for line in data:

        wires, output = process_input_line(line)
        solve_map = generate_solve_map(wires)
        output_str = "".join(str(solve_map[o]) for o in output)
        total += int(output_str)
    return total


print(f"Test Part 1: {part1(test_puzzle_input)}")
print(f"Part 1: {part1(puzzle_input)}")
print(f"Short part 2 {part2(short_test_puzzle_input.splitlines())}")
print(f"Test Part 2: {part2(test_puzzle_input)}")
print(f"Part 2: {part2(puzzle_input)}")
