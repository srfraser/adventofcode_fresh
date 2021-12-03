from pathlib import Path
from collections import defaultdict
from functools import lru_cache

puzzle_input = (Path(__file__).parent.parent / Path("input")).read_text().strip()


def resolve_value(value, wires):
    if value.isnumeric():
        return int(value)
    else:
        return wires.get(value, 0)



def process_connections(conn, puzzle):
    try:
        return int(conn)
    except (ValueError, TypeError):
        pass

    print(f"Turning {conn} into {puzzle[conn]}")
    conn = puzzle[conn]
    if len(conn) == 1:
        if conn[0].isnumeric():
            return int(conn[0])
        return process_connections(conn[0], puzzle)
    elif len(conn) == 2 and conn[0].startswith("NOT"):
        # No 16 bit numbers in python
        # print(f"NOT operation, on value {find_by_output(conn[1], puzzle)}")
        return 65536 + ~process_connections(conn[1], puzzle)
    elif len(conn) == 3:
        # print(f"Three part operation {conn}")
        x, op, y = conn
        #x = find_by_output(x, puzzle)
        #y = find_by_output(y, puzzle)
        #print(f"Working out {x} {op} {y}")
        if op == "AND":
            return process_connections(x, puzzle) & process_connections(y, puzzle)
        elif op == "OR":
            return process_connections(x, puzzle) | process_connections(y, puzzle)
        elif op == "LSHIFT":
            return process_connections(x, puzzle) << process_connections(y, puzzle)
        else:  # RSHIFT
            return process_connections(x, puzzle) >> process_connections(y, puzzle)


def cheating_circuit(puzzle, target_wire="a"):
    new_puzzle = dict()
    for line in puzzle.splitlines():
        operation, output_wire = line.split(" -> ")
        new_puzzle[output_wire] = operation.split()
    puzzle = new_puzzle
    return process_connections(target_wire, puzzle)


def process_circuit(puzzle):
    wires = defaultdict(int)
    for line in puzzle.splitlines():
        operation, output_wire = line.split(" -> ")
        operation = operation.split()
        if len(operation) == 1:
            print(operation, output_wire)
            operation = resolve_value(operation[0], wires)
            print(operation, output_wire)
            wires[output_wire] = operation
            continue
        elif len(operation) == 2 and operation[0].startswith("NOT"):
            input_wire = operation[1]
            # No 16 bit numbers in python
            wires[output_wire] = 65536 + ~resolve_value(input_wire, wires)
            continue

        # print(operation)
        op = operation[1]
        x = resolve_value(operation[0], wires)
        y = resolve_value(operation[2], wires)

        if op == "AND":
            wires[output_wire] = x & y
        elif op == "OR":
            wires[output_wire] = x | y
        elif op == "LSHIFT":
            wires[output_wire] = x << y
        else:  # RSHIFT
            wires[output_wire] = x >> y

    return dict(sorted(wires.items()))


"""
x << y
    Returns x with the bits shifted to the left by y places (and new bits on the right-hand-side are zeros). This is the same as multiplying x by 2**y. 
x >> y
    Returns x with the bits shifted to the right by y places. This is the same as //'ing x by 2**y. 
x & y
    Does a "bitwise and". Each bit of the output is 1 if the corresponding bit of x AND of y is 1, otherwise it's 0. 
x | y
    Does a "bitwise or". Each bit of the output is 0 if the corresponding bit of x AND of y is 0, otherwise it's 1. 
~ x
    Returns the complement of x - the number you get by switching each 1 for a 0 and each 0 for a 1. This is the same as -x - 1. 
x ^ y
    Does a "bitwise exclusive or". Each bit of the output is the same as the corresponding bit in x if that bit in y is 0, and it's the complement of the bit in x if that bit in y is 1. 
"""
test_circuit = """123 -> x
456 -> y
x AND y -> d
x OR y -> e
x LSHIFT 2 -> f
y RSHIFT 2 -> g
NOT x -> h
NOT y -> i"""

test_output = {
    "d": 72,
    "e": 507,
    "f": 492,
    "g": 114,
    "h": 65412,
    "i": 65079,
    "x": 123,
    "y": 456,
}

for wire, output in test_output.items():
    print(f"Checking {wire}, {output} == {cheating_circuit(test_circuit, wire)}")
    assert cheating_circuit(test_circuit, wire) == output
# assert process_circuit(test_circuit) == test_output
print("Now doing part 1")
print(f"Part 1, wire a is {cheating_circuit(puzzle_input, 'a')}")
