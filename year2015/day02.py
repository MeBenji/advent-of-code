from pathlib import Path


def wrapping_paper(present: str) -> int:
    length, width, height = (int(d) for d in present.split("x"))
    sides = (length * width, width * height, height * length)
    surface_area = 2 * sum(sides)
    slack = min(sides)
    return surface_area + slack


def part1(presents: str) -> int:
    return sum(wrapping_paper(present) for present in presents.splitlines())


def ribbon(present: str) -> int:
    length, width, height = (int(d) for d in present.split("x"))
    perimiters = (2 * (length + width), 2 * (width + height), 2 * (height + length))
    wrap = min(perimiters)
    bow = length * width * height
    return wrap + bow


def part2(presents: str) -> int:
    return sum(ribbon(present) for present in presents.splitlines())


if __name__ == "__main__":
    file = Path(__file__)
    data = file.with_name(f"{file.stem}_input.txt").read_text()
    solution1 = part1(data)
    print(f"Solution 1: {solution1}")
    solution2 = part2(data)
    print(f"Solution 2: {solution2}")
