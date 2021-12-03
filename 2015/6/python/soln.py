from pathlib import Path

puzzle_input = (Path(__file__).parent.parent / Path("input")).read_text().strip()

part1_operations = {
    "turn on": lambda x: 1,
    "turn off": lambda x: 0,
    "toggle": lambda x: 0 if x else 1,
}

part2_operations = {
    "turn on": lambda x: x + 1,
    "turn off": lambda x: max(x - 1, 0),
    "toggle": lambda x: x + 2,
}


def process_line(line, grid, operations):
    for op in operations.keys():
        if line.startswith(op):
            operation = operations[op]
            start, _, end = line.strip(op).split()
            break

    start_x, start_y = [int(i) for i in start.split(",")]
    end_x, end_y = [int(i) for i in end.split(",")]
    for y in range(start_y, end_y + 1):
        for x in range(start_x, end_x + 1):
            grid[y][x] = operation(grid[y][x])

    return grid


def count_illuminated(grid):
    total = 0
    for y in grid:
        total += sum(y)
    return total


def process_grid(puzzle, operations):
    grid_size = 1000
    grid = [[0] * grid_size for _ in range(grid_size)]
    for line in puzzle.splitlines():
        grid = process_line(line, grid, operations)

    return count_illuminated(grid)


assert process_grid("turn on 0,0 through 999,999", part1_operations) == 1_000_000
assert process_grid("toggle 0,0 through 999,0", part1_operations) == 1_000

print(f"Lights lit after part 1: {process_grid(puzzle_input, part1_operations)}")
print(f"Lights lit after part 2: {process_grid(puzzle_input, part2_operations)}")
