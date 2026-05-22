from pathlib import Path


def part1(data: str) -> int | str:
    pass


def part2(data: str) -> int | str:
    pass


if __name__ == "__main__":
    file = Path(__file__)
    data = file.with_name(f"{file.stem}_input.txt").read_text()
    solution1 = part1(data)
    solution2 = part2(data)
    print(f"Solution 1: {solution1}")
    print(f"Solution 2: {solution2}")
