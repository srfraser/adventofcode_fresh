from pathlib import Path


class Board:
    def __init__(self, lines):
        self.selections = [set(x) for x in lines]
        self.transposed = []
        for i in range(len(lines[0])):
            self.transposed.append(set([line[i] for line in lines]))

    def __repr__(self):
        return f"{self.selections}"

    def has_won(self, drawn_numbers):
        drawn = set(drawn_numbers)
        return any([d <= drawn for d in self.selections]) or any(
            [d <= drawn for d in self.transposed]
        )

    def board_total(self, drawn_numbers):
        all_of_board = set()
        for line in self.selections:
            all_of_board.update(line)
        all_of_board -= set(drawn_numbers)
        return sum(all_of_board)


def process_puzzle_input(data):
    draw_line, _, *text_boards = data.splitlines()
    draw_list = [int(i) for i in draw_line.split(",")]

    boards = list()

    current_board = list()
    for line in text_boards:
        if line == "":
            boards.append(Board(current_board))
            current_board = list()
            continue
        current_board.append([int(i) for i in line.rstrip().split()])
    boards.append(Board(current_board))

    return draw_list, boards


def part1(draw, boards):
    drawn = list()
    for d in draw:
        drawn.append(d)
        for b in boards:
            if b.has_won(drawn):
                return b.board_total(drawn) * d


def part2(draw, boards):
    drawn = list()
    for d in draw:
        drawn.append(d)
        new_boards = list()
        for b in boards:
            if b.has_won(drawn) and len(boards) == 1:
                return b.board_total(drawn) * d
            if not b.has_won(drawn):
                new_boards.append(b)
        boards = new_boards


INPUT_FILE = Path(__file__).parent / "../input"
draw, boards = process_puzzle_input(INPUT_FILE.read_text())
TEST_INPUT_FILE = Path(__file__).parent / "../test_input"
test_draw, test_boards = process_puzzle_input(TEST_INPUT_FILE.read_text())


print(f"Test Part 1 {part1(test_draw, test_boards)}")
print(f"Part 1 {part1(draw, boards)}")


print(f"Test Part 2 {part2(test_draw, test_boards)}")
print(f"Part 2 {part2(draw, boards)}")
