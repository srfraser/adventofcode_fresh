from os import O_RDONLY
from pathlib import Path

INPUT_FILE = Path(__file__).parent / "../input"
puzzle_input = [int(i) for i in INPUT_FILE.read_text().strip().split(",")]
TEST_INPUT_FILE = Path(__file__).parent / "../test_input"
test_puzzle_input = [int(i) for i in TEST_INPUT_FILE.read_text().strip().split(",")]


def find_smallest(crab_data, fuel_method):

    potential_positions = list(range(min(crab_data), max(crab_data) + 1))
    fuel_used = dict()
    for position in potential_positions:
        fuel_used[position] = sum(
            [fuel_method(abs(crab - position)) for crab in crab_data]
        )

    return fuel_used[min(fuel_used, key=fuel_used.get)]


def part1(crab_data):
    return find_smallest(crab_data, lambda f: f)


def part2(crab_data):
    return find_smallest(crab_data, lambda f: f * (f + 1) // 2)


print(f"Test Part 1: {part1(test_puzzle_input)}")
print(f"Part 1: {part1(puzzle_input)}")
print(f"Test Part 2: {part2(test_puzzle_input)}")
print(f"Part 2: {part2(puzzle_input)}")
