from pathlib import Path
from collections import defaultdict

INPUT_FILE = Path(__file__).parent / "../input"
puzzle_input = [int(i) for i in INPUT_FILE.read_text().strip().split(",")]
TEST_INPUT_FILE = Path(__file__).parent / "../test_input"
test_puzzle_input = [int(i) for i in TEST_INPUT_FILE.read_text().strip().split(",")]


def run_simulation(starting_fish, days=80):

    days_remaining = {
        0: 0,
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
        7: 0,
        8: 0,
    }
    for fish in starting_fish:
        days_remaining[fish] += 1
    for _ in range(days):
        new_days = dict()
        for i in range(0, 8):
            new_days[i] = days_remaining[i + 1]
        new_days[8] = days_remaining[0]
        new_days[6] += days_remaining[0]
        days_remaining = new_days
    return sum(days_remaining.values())


print(f"Test Part 1: {run_simulation(test_puzzle_input, days=10)}")
print(f"Test Part 1: {run_simulation(test_puzzle_input, days=80)}")
print(f"Part 1: {run_simulation(puzzle_input, days=80)}")
print(f"Test Part 2: {run_simulation(test_puzzle_input, days=256)}")
print(f"Part 2: {run_simulation(puzzle_input, days=256)}")
