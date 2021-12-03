from pathlib import Path
import math

puzzle_input = Path("./input").read_text().strip()

DIRECTIONS = {
    ">": (1, 0),
    "v": (0, 1),
    "<": (-1, 0),
    "^": (0, -1),
}


def visited_houses(puzzle):
    current_coords = (0, 0)
    visited = list()

    visited.append(current_coords)
    for direction in puzzle:
        current_coords = (
            current_coords[0] + DIRECTIONS[direction][0],
            current_coords[1] + DIRECTIONS[direction][1],
        )
        visited.append(current_coords)
    return visited


def part1(puzzle):
    return len(set(visited_houses(puzzle)))


def part2(puzzle):
    santa = puzzle[0::2]
    robo = puzzle[1::2]
    return len(set(visited_houses(santa) + visited_houses(robo)))


assert visited_houses(">") == [(0, 0), (1, 0)]
assert visited_houses("^>v<") == [(0, 0), (0, -1), (1, -1), (1, 0), (0, 0)]
assert part1(">") == 2
assert part1("^>v<") == 4
assert part1("^v^v^v^v^v") == 2
assert part2("^>v<") == 3
assert part2("^v^v^v^v^v") == 11

result = part1(puzzle_input)
print(f"Part 1 {result} houses")
result = part2(puzzle_input)
print(f"Part 2 {result} houses")
