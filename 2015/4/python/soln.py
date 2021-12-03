import hashlib


def find_leading_zeroes(secret_key, zeroes=5):
    hashinput = 1
    current = ""
    target = "0" * zeroes
    while not current.startswith(target):
        hashinput += 1
        m = hashlib.md5()
        m.update(bytes(secret_key, "utf-8"))
        m.update(bytes(str(hashinput), "utf-8"))
        current = m.hexdigest()
    return hashinput


assert find_leading_zeroes("abcdef") == 609043
assert find_leading_zeroes("pqrstuv") == 1048970

print(f"Lowest input for part 1 {find_leading_zeroes('bgvyzdsv')}")
print(f"Lowest input for part 1 {find_leading_zeroes('bgvyzdsv', zeroes=6)}")
