from pathlib import Path
from hashlib import md5


def part1(secret_key: str) -> int:
    number = 1
    md5_hash = md5(f"{secret_key}{number}".encode())
    while not md5_hash.hexdigest().startswith("00000"):
        number += 1
        md5_hash = md5(f"{secret_key}{number}".encode())
    return number


def part2(secret_key: str) -> int:
    number = 1
    md5_hash = md5(f"{secret_key}{number}".encode())
    while not md5_hash.hexdigest().startswith("000000"):
        number += 1
        md5_hash = md5(f"{secret_key}{number}".encode())
    return number


if __name__ == "__main__":
    file = Path(__file__)
    data = file.with_name(f"{file.stem}_input.txt").read_text()
    solution1 = part1(data)
    print(f"Solution 1: {solution1}")
    solution2 = part2(data)
    print(f"Solution 2: {solution2}")
