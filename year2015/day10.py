from pathlib import Path
from itertools import pairwise


def look_and_say(sequence: str) -> str:
    new_sequence = ""
    count = 1
    for curr, next_ in pairwise(sequence):
        if curr == next_:
            count += 1
            continue
        new_sequence += f"{count}{curr}"
        count = 1
    new_sequence += f"{count}{sequence[-1]}"
    return new_sequence


def part1(sequence: str, iterations: int) -> int:
    for _ in range(iterations):
        sequence = look_and_say(sequence)
    return len(sequence)


def part2(sequence: str, iterations: int) -> int:
    for _ in range(iterations):
        sequence = look_and_say(sequence)
    return len(sequence)


if __name__ == "__main__":
    file = Path(__file__)
    data = file.with_name(f"{file.stem}_input.txt").read_text()
    solution1 = part1(data, 40)
    print(f"Solution 1: {solution1}")
    solution2 = part2(data, 50)
    print(f"Solution 2: {solution2}")
