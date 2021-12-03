from pathlib import Path
import math

puzzle_input = Path("./input").read_text().strip()


def surface_area(width, length, height):
    sides = [length * width, width * height, height * length]
    # Add margin of error: size of smallest side
    return sum(sides) * 2 + min(sides)


def ribbon_length(dimensions):
    bow = math.prod(dimensions)
    dimensions.remove(max(dimensions))
    return 2 * sum(dimensions) + bow


def part1(puzzle):
    total_sq_feet = 0
    for line in puzzle.splitlines():
        dimensions = [int(i) for i in line.split("x")]
        total_sq_feet += surface_area(*dimensions)
    return total_sq_feet


def part2(puzzle):
    total_ribbon = 0
    for line in puzzle.splitlines():
        dimensions = [int(i) for i in line.split("x")]
        total_ribbon += ribbon_length(dimensions)
    return total_ribbon


assert surface_area(2, 3, 4) == 58
assert surface_area(1, 1, 10) == 43
assert ribbon_length([2, 3, 4]) == 34
assert ribbon_length([1, 1, 10]) == 14

result = part1(puzzle_input)
print(f"Part 1 {result} square feet")
result = part2(puzzle_input)
print(f"Part 2 {result} feet of ribbon")
