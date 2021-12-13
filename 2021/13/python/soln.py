from pathlib import Path
from itertools import filterfalse, tee

INPUT_FILE = Path(__file__).parent / "../input"
puzzle_input = INPUT_FILE.read_text()

TEST_INPUT_FILE = Path(__file__).parent / "../test_input"
test_puzzle_input = TEST_INPUT_FILE.read_text()


def process_puzzle_input(data):
    coords, raw_folds = data.split("\n\n")
    coords = [[int(i) for i in coord.split(",")] for coord in coords.splitlines()]
    folds = list()
    for f in raw_folds.splitlines():
        f = f.strip("fold along")
        dimension, line = f.split("=")
        line = int(line)
        folds.append((dimension, line))
    return coords, folds


def split_on(data, dimension, line):
    if dimension == "x":
        dimension = 0
    else:
        dimension = 1
    before_cut, after_cut = tee(data)
    check = lambda x: x[dimension] < line
    return list(filter(check, before_cut)), list(filterfalse(check, after_cut))


def show_grid(coords):
    max_x = max([c[0] for c in coords]) + 1
    max_y = max([c[1] for c in coords]) + 1
    for y in range(max_y):
        for x in range(max_x):
            if [x, y] in coords:
                print("#", end="")
            else:
                print(".", end="")
        print("")
    print("")


def fold(coords, dimension, line):
    new_coords = list()
    if dimension == "y":
        for x, y in coords:
            new_coords.append([x, line - (y - line)])
    else:
        for x, y in coords:
            new_coords.append([line - (x - line), y])
    return new_coords


def perform_folds(data, stop_after=None):

    iteration = 0
    coords, folds = process_puzzle_input(data)
    # show_grid(coords)
    for dimension, line in folds:
        iteration += 1
        if stop_after and iteration > stop_after:
            break
        before, after = split_on(coords, dimension, line)
        # show_grid(before)
        # show_grid(after)

        # print(before)
        # print(after)
        after = fold(after, dimension, line)
        # print(after)
        # show_grid(after)
        coords = before
        for coord in after:
            if coord not in coords:
                coords.append(coord)

        # show_grid(coords)
    return coords


print(f"Test Part 1: {len(perform_folds(test_puzzle_input, stop_after=1))}")
print(f"Part 1: {len(perform_folds(puzzle_input, stop_after=1))}")
coords = perform_folds(test_puzzle_input)

print(f"Test Part 2:")
show_grid(coords)
coords = perform_folds(puzzle_input)

print(f"Part 2:")
show_grid(coords)
