from pathlib import Path
import math

INPUT_FILE = Path(__file__).parent / "../input"
puzzle_input = INPUT_FILE.read_text().splitlines()

TEST_INPUT_FILE = Path(__file__).parent / "../test_input"
test_puzzle_input = TEST_INPUT_FILE.read_text().splitlines()

MATCHING_CLOSE = {
    ")": "(",
    "}": "{",
    "]": "[",
    ">": "<",
}

MATCHING_OPEN = {
    "(": ")",
    "{": "}",
    "[": "]",
    "<": ">",
}

OPENERS = MATCHING_CLOSE.values()
CLOSERS = MATCHING_CLOSE.keys()

SCORE_CORRUPTED = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}

SCORE_INCOMPLETE = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4,
}


def identify_corrupted(line):
    stack = list()
    for bracket in line:
        if bracket in OPENERS:
            stack.append(bracket)
            continue
        if bracket in CLOSERS:
            if MATCHING_CLOSE[bracket] != stack[-1]:
                return bracket
            else:
                stack.pop()
    return False


def part1(data):
    score = 0
    for line in data:
        char = identify_corrupted(line)
        if char:
            score += SCORE_CORRUPTED[char]
    return score


def identify_closing(line):
    """We've already filtered out corrupted"""
    stack = list()
    for bracket in line:
        if bracket in OPENERS:
            stack.append(bracket)
            continue
        elif bracket in CLOSERS:
            stack.pop()

    score = 0
    for b in stack[::-1]:
        score *= 5
        score += SCORE_INCOMPLETE[MATCHING_OPEN[b]]
    return score


def part2(data):
    incomplete_lines = list(filter(lambda x: not identify_corrupted(x), data))
    scores = sorted([identify_closing(line) for line in incomplete_lines])
    return scores[(len(scores) // 2)]


print(f"Test Part 1: {part1(test_puzzle_input)}")
print(f"Part 1: {part1(puzzle_input)}")
print(f"Test Part 2: {part2(test_puzzle_input)}")
print(f"Part 2: {part2(puzzle_input)}")
