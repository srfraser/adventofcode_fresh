from pathlib import Path
from collections import defaultdict

INPUT_FILE = Path(__file__).parent / "../input"
puzzle_input = INPUT_FILE.read_text()


test_puzzle_input_1 = """start-A
start-b
A-c
A-b
b-d
A-end
b-end"""

test_puzzle_output_1 = """start,A,b,A,c,A,end
start,A,b,A,end
start,A,b,end
start,A,c,A,b,A,end
start,A,c,A,b,end
start,A,c,A,end
start,A,end
start,b,A,c,A,end
start,b,A,end
start,b,end"""

test_puzzle_input_2 = """dc-end
HN-start
start-kj
dc-start
dc-HN
LN-dc
HN-end
kj-sa
kj-HN
kj-dc"""


test_puzzle_input_3 = """fs-end
he-DX
fs-he
start-DX
pj-DX
end-zg
zg-sl
zg-pj
pj-he
RW-he
fs-DX
pj-RW
zg-RW
start-pj
he-WI
zg-he
pj-fs
start-RW"""


def build_map(data):
    cave_map = defaultdict(list)
    for line in data.splitlines():
        a, b = line.split("-")
        if b != "start":
            cave_map[a].append(b)
        if a != "start":
            cave_map[b].append(a)
    return cave_map


def find_paths(current_location, path, cave_map, visited=None, path_list=None):
    if not visited:
        visited = set()
    if not path_list:
        path_list = set()
    visited = set(visited)
    path = list(path)
    visited.add(current_location)
    path.append(current_location)
    if current_location == "end":
        path_list.add(",".join(path))
        return path_list
    for exit_path in cave_map[current_location]:
        if exit_path in visited and exit_path.islower():
            continue
        path_list.update(find_paths(exit_path, path, cave_map, visited, path_list))
    return path_list


def part1(data):
    cave_map = build_map(data)
    paths_found = find_paths("start", [], cave_map)

    return len(paths_found)


def has_duplicate_lowers(path):
    lowers = [p for p in path if p.islower()]
    return len(lowers) != len(set(lowers))


def find_paths2(
    current_location,
    path,
    cave_map,
    visited=None,
    path_list=None,
):
    if not visited:
        visited = set()
    if not path_list:
        path_list = set()
    visited = set(visited)
    path = list(path)
    visited.add(current_location)
    path.append(current_location)
    if current_location == "end":
        path_list.add(",".join(path))
        return path_list
    for exit_path in cave_map[current_location]:
        if exit_path in visited and exit_path.islower() and has_duplicate_lowers(path):
            continue
        path_list.update(find_paths2(exit_path, path, cave_map, visited, path_list))
    return path_list


def part2(data):

    cave_map = build_map(data)
    paths_found = find_paths2("start", [], cave_map)

    return len(paths_found)


assert part1(test_puzzle_input_1) == 10
assert part1(test_puzzle_input_2) == 19
assert part1(test_puzzle_input_3) == 226


print(f"Part 1: {part1(puzzle_input)}")

assert part2(test_puzzle_input_1) == 36
assert part2(test_puzzle_input_2) == 103
assert part2(test_puzzle_input_3) == 3509


print(f"Part 2: {part2(puzzle_input)}")
