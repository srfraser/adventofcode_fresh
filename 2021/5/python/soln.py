from os import O_RDONLY
from pathlib import Path
from collections import defaultdict

INPUT_FILE = Path(__file__).parent / "../input"
puzzle_input = INPUT_FILE.read_text().strip().splitlines()
TEST_INPUT_FILE = Path(__file__).parent / "../test_input"
test_puzzle_input = TEST_INPUT_FILE.read_text().strip().splitlines()


def is_horizontal_or_vertical(start, end):
    return start[0] == end[0] or start[1] == end[1]


def line_to_coord_pair(line):
    """0,9 -> 5,9"""
    start, end = line.split(" -> ")
    start_x, start_y = [int(i) for i in start.split(",")]
    end_x, end_y = [int(i) for i in end.split(",")]
    return (start_x, start_y), (end_x, end_y)


def expand_coords(start, end):
    coords = [start]
    x, y = start
    while end != (x, y):
        if x < end[0]:
            x += 1
        elif x > end[0]:
            x -= 1
        if y < end[1]:
            y += 1
        elif y > end[1]:
            y -= 1
        coords.append((x, y))
    return coords


def find_dangerous_vents(data, only_orthogonal=False):
    visited = defaultdict(int)
    for line in data:
        start, end = line_to_coord_pair(line)
        if only_orthogonal and not is_horizontal_or_vertical(start, end):
            continue
        for coord in expand_coords(start, end):
            visited[coord] += 1
    return len(list(filter(lambda x: x >= 2, visited.values())))


print(f"Test Part 1: {find_dangerous_vents(test_puzzle_input, only_orthogonal=True)}")
print(f"Part 1: {find_dangerous_vents(puzzle_input, only_orthogonal=True)}")
print(f"Test Part 2: {find_dangerous_vents(test_puzzle_input)}")
print(f"Part 2: {find_dangerous_vents(puzzle_input)}")
