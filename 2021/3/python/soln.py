from pathlib import Path


INPUT_FILE = Path(__file__).parent / "../input"
puzzle_input = INPUT_FILE.read_text().strip().splitlines()

test_puzzle_input = """00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010""".splitlines()


def count_bits_in_position(data, position):
    pass


def calculate_gamma(data):
    return calculate_variable(data, lambda x, y: x >= y)


def calculate_epsilon(data):
    return calculate_variable(data, lambda x, y: x <= y)


def calculate_variable(data, condition):
    result = list()
    for i in range(len(data[0])):
        ones = filter(lambda x: x == "1", [d[i] for d in data])
        if condition(len(list(ones)), len(data) / 2):
            result.append("1")
        else:
            result.append("0")
    return int("".join(result), 2)


def most_at_position(data, position, check_most, tie_breaker):
    ones = list(filter(lambda x: x == "1", [d[position] for d in data]))
    if len(ones) == len(data) / 2:
        return tie_breaker
    elif len(ones) > len(data) / 2:
        if check_most:
            return "1"
        else:
            return "0"
    else:
        if check_most:
            return "0"
        else:
            return "1"


def filter_numbers(data, check_most=True, tie_breaker="1"):
    candidates = list(data)
    current_position = 0
    while len(candidates) > 1:
        filter_for = most_at_position(
            candidates, current_position, check_most, tie_breaker
        )
        candidates = list(
            filter(lambda x: x[current_position] == filter_for, candidates)
        )
        current_position += 1
    return candidates[0]


def calculate_oxygen_generator_rating(data):
    return int(filter_numbers(data, check_most=True, tie_breaker="1"), 2)


def calculate_co2_scrubber_rating(data):
    return int(filter_numbers(data, check_most=False, tie_breaker="0"), 2)


assert calculate_gamma(test_puzzle_input) * calculate_epsilon(test_puzzle_input) == 198
assert calculate_oxygen_generator_rating(test_puzzle_input) == 23
assert calculate_co2_scrubber_rating(test_puzzle_input) == 10

print(f"Part 1 {calculate_gamma(puzzle_input) * calculate_epsilon(puzzle_input)}")
print(
    f"Part 2 {calculate_oxygen_generator_rating(puzzle_input) * calculate_co2_scrubber_rating(puzzle_input)}"
)
