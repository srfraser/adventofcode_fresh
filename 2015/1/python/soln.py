from pathlib import Path

puzzle_input = Path("./input").read_text().strip()


def part1(data):
    return data.count("(") - data.count(")")


def part2(instructions):
    position = 0
    target = -1
    current = 0
    instructions = [1 if c == "(" else -1 for c in instructions]
    for instruction in instructions:
        current += instruction
        position += 1
        if current == target:
            break
    return position


result = part1(puzzle_input)
print(f"Part 1 ends on floor {result}")
result = part2(puzzle_input)
print(f"Part 2 descends into the basement at position {result}")
