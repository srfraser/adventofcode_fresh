from pathlib import Path

puzzle_input = (Path(__file__).parent.parent / Path("input")).read_text().strip()


def count_vowels(text):
    vowels = "aeiou"
    total_vowels = 0
    for vowel in vowels:
        total_vowels += text.count(vowel)
    return total_vowels


def has_sequential_letters(text):
    for a, b in zip(text, text[1:]):
        if a == b:
            return True
    return False


def has_non_overlapping_pairs(text):
    for a, b in zip(text, text[1:]):
        if text.count(f"{a}{b}") > 1:
            return True
    return False


def has_one_spaced_repeats(text):
    for a, _, c in zip(text, text[1:], text[2:]):
        if a == c:
            return True
    return False


def is_nice(text):
    bad_strings = ["ab", "cd", "pq", "xy"]
    if any(bs in text for bs in bad_strings):
        return False
    if count_vowels(text) <= 2:
        return False
    if not has_sequential_letters(text):
        return False
    return True


def is_nice_part2(text):
    return has_non_overlapping_pairs(text) and has_one_spaced_repeats(text)


def part1(puzzle):
    return len([line for line in puzzle.splitlines() if is_nice(line)])


def part2(puzzle):
    return len([line for line in puzzle.splitlines() if is_nice_part2(line)])


assert is_nice("ugknbfddgicrmopn") is True
assert is_nice("aaa") is True
assert is_nice("jchzalrnumimnmhp") is False
assert is_nice("haegwjzuvuyypxyu") is False
assert is_nice("dvszwmarrgswjxmb") is False

assert is_nice_part2("qjhvhtzxzqqjkmpb") is True
assert is_nice_part2("xxyxx") is True
assert is_nice_part2("uurcxstgmygtbstg") is False
assert is_nice_part2("ieodomkazucvgmuy") is False


print(f"Number of nice entries in part 1 {part1(puzzle_input)}")
print(f"Number of nice entries in part 2 {part2(puzzle_input)}")
