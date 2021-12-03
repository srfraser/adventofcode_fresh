from pathlib import Path


INPUT_FILE = Path(__file__).parent / "../input"
puzzle_input = [int(i) for i in INPUT_FILE.read_text().strip().splitlines()]


def chunkify(data, n):
    for i in range(0, len(data)):
        yield data[i : i + n]


def part1(data):
    increases = [True if b > a else False for a, b in zip(data, data[1:])]
    return increases.count(True)


def part2_orig(data):
    increases = [
        True if b > a else False
        for a, b in zip(
            [sum(i) for i in chunkify(data, 3)], [sum(i) for i in chunkify(data[1:], 3)]
        )
    ]
    return increases.count(True)


def part2(data):
    increases = [True if b > a else False for a, b in zip(data, data[3:])]
    return increases.count(True)


result = part1(puzzle_input)
print(f"Part 1 number of increases {result}")
result = part2(puzzle_input)
print(f"Part 2 number of sectioned increases {result}")
