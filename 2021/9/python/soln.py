from pathlib import Path
import math

INPUT_FILE = Path(__file__).parent / "../input"
puzzle_input = [
    [int(i) for i in list(line)] for line in INPUT_FILE.read_text().splitlines()
]
TEST_INPUT_FILE = Path(__file__).parent / "../test_input"
test_puzzle_input = [
    [int(i) for i in list(line)] for line in TEST_INPUT_FILE.read_text().splitlines()
]


def neighbours(data, x, y):
    if x > 0:
        yield data[y][x - 1]
    if x < len(data[0]) - 1:
        yield data[y][x + 1]
    if y > 0:
        yield data[y - 1][x]
    if y < len(data) - 1:
        yield data[y + 1][x]


def neighbour_coords(data, x, y):
    if x > 0:
        yield x - 1, y
    if x < len(data[0]) - 1:
        yield x + 1, y
    if y > 0:
        yield x, y - 1
    if y < len(data) - 1:
        yield x, y + 1


def discover_basin(data, x, y, visited):
    basin = list()
    explore = [(x, y)]
    while explore:
        x, y = explore.pop(0)
        ne = [
            n
            for n in neighbour_coords(data, x, y)
            if data[n[1]][n[0]] != 9 and n not in visited
        ]
        # print(f"{x},{y} neighbours are {ne}")
        if len(ne) == 0:
            continue
        basin.extend(ne)
        visited.extend(ne)
        explore.extend(ne)
    return basin


def calculate_risk(heights):
    return sum([i + 1 for i in heights])


def part1(data):
    lowest = list()
    for y in range(len(data)):
        for x in range(len(data[0])):
            if all([data[y][x] < ne for ne in neighbours(data, x, y)]):
                lowest.append(data[y][x])
                # print(f"Lowest at {x},{y} {data[y][x]}")
    return calculate_risk(lowest)


def part2(data):
    visited = list()
    basins = list()
    for y in range(len(data)):
        for x in range(len(data[0])):
            if (x, y) in visited:
                continue
            new_basin = discover_basin(data, x, y, visited)
            if new_basin:
                basins.append(new_basin)

    basin_sizes = sorted([len(b) for b in basins])
    return math.prod(basin_sizes[-3:])


print(f"Test Part 1: {part1(test_puzzle_input)}")
print(f"Part 1: {part1(puzzle_input)}")
print(f"Test Part 2: {part2(test_puzzle_input)}")
print(f"Part 2: {part2(puzzle_input)}")
