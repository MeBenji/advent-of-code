from pathlib import Path


def wrapping_paper(present: str) -> int:
    length, width, height = (int(d) for d in present.split("x"))
    sides = (length * width, width * height, height * length)
    surface_area = 2 * sum(sides)
    slack = min(sides)
    return surface_area + slack


def part1(data: str) -> int:
    total_wrapping_paper = 0
    for present in data.split("\n"):
        total_wrapping_paper += wrapping_paper(present)
    return total_wrapping_paper


def ribbon(present: str) -> int:
    length, width, height = (int(d) for d in present.split("x"))
    perimiters = (2 * (length + width), 2 * (width + height), 2 * (height + length))
    wrap = min(perimiters)
    bow = length * width * height
    return wrap + bow


def part2(data: str) -> int:
    total_ribbon = 0
    for present in data.split("\n"):
        total_ribbon += ribbon(present)
    return total_ribbon


if __name__ == "__main__":
    file = Path(__file__)
    data = file.with_name(f"{file.stem}_input.txt").read_text()
    solution1 = part1(data)
    solution2 = part2(data)
    print(f"Solution 1: {solution1}")
    print(f"Solution 2: {solution2}")
