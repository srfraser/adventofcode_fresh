from pathlib import Path


INPUT_FILE = Path(__file__).parent / "../input"
puzzle_input = INPUT_FILE.read_text().strip().splitlines()


def part1(data):
    forward, depth = 0, 0
    for line in data:
        direction, amount = line.split()
        if direction == "forward":
            forward += int(amount)
        elif direction == "up":
            depth -= int(amount)
        elif direction == "down":
            depth += int(amount)
    return forward, depth


def part2(data):
    forward, depth, aim = 0, 0, 0
    for line in data:
        direction, amount = line.split()
        if direction == "forward":
            forward += int(amount)
            depth += int(amount) * aim
        elif direction == "up":
            aim -= int(amount)
        elif direction == "down":
            aim += int(amount)
    return forward, depth


forward, depth = part1(puzzle_input)
print(f"Part 1 {forward} * {depth} = {forward * depth}")
forward, depth = part2(puzzle_input)
print(f"Part 2 {forward} * {depth} = {forward * depth}")
