from pathlib import Path
import math

INPUT_FILE = Path(__file__).parent / "../input"
puzzle_input = [[int(i) for i in line] for line in INPUT_FILE.read_text().splitlines()]

TEST_INPUT_FILE = Path(__file__).parent / "../test_input"
test_puzzle_input = [
    [int(i) for i in line] for line in TEST_INPUT_FILE.read_text().splitlines()
]


def neighbour_coords(data, x, y):
    for x_mod in range(-1, 2):
        for y_mod in range(-1, 2):
            new_x = x + x_mod
            new_y = y + y_mod
            if new_x < 0 or new_x >= len(data[0]) or new_y < 0 or new_y >= len(data):
                continue
            yield new_x, new_y


def coords_of_nines(data):
    for y, line in enumerate(data):
        for x, entry in enumerate(line):
            if entry > 9:
                yield (x, y)


def increment_all(data):
    return [[i + 1 for i in line] for line in data]


def step(data):
    data = increment_all(data)
    nines = list(coords_of_nines(data))
    flashed = list(nines)
    while nines:
        current = nines.pop(0)
        for x, y in neighbour_coords(data, current[0], current[1]):
            data[y][x] += 1
            if data[y][x] > 9 and (x, y) not in flashed:
                nines.append((x, y))
                flashed.append((x, y))
    for fl in flashed:
        data[fl[1]][fl[0]] = 0

    return data, len(flashed)


def part1(data):
    flash_count = 0
    for _ in range(100):
        data, flashes = step(data)
        flash_count += flashes
    return flash_count


def part2(data):
    iteration_count = 0
    total_size = len(data) * len(data[0])
    flashes = 0
    while flashes != total_size:
        iteration_count += 1
        data, flashes = step(data)
    return iteration_count


print(f"Test Part 1: {part1(test_puzzle_input)}")
print(f"Part 1: {part1(puzzle_input)}")
print(f"Test Part 2: {part2(test_puzzle_input)}")
print(f"Part 2: {part2(puzzle_input)}")
