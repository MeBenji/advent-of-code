from pathlib import Path


def part1(instructions: str) -> int:
    floor = 0
    for c in instructions:
        if c == "(":
            floor += 1
        elif c == ")":
            floor -= 1
    return floor


def part2(instructions: str) -> int:
    floor = 0
    for i, c in enumerate(instructions, 1):
        if c == "(":
            floor += 1
        elif c == ")":
            floor -= 1
        if floor < 0:
            return i


if __name__ == "__main__":
    file = Path(__file__)
    data = file.with_name(f"{file.stem}_input.txt").read_text()
    solution1 = part1(data)
    print(f"Solution 1: {solution1}")
    solution2 = part2(data)
    print(f"Solution 2: {solution2}")
