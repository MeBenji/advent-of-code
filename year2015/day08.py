from pathlib import Path
from ast import literal_eval


def part1(digital_list: str) -> int:
    total_len_diff = 0
    for string_literal in digital_list.splitlines():
        string = literal_eval(string_literal)
        total_len_diff += len(string_literal) - len(string)
    return total_len_diff


def part2(digital_list: str) -> int:
    total_len_diff = 0
    for string in digital_list.splitlines():
        string_literal = f'"{string.replace("\\", "\\\\").replace('"', '\\"')}"'
        total_len_diff += len(string_literal) - len(string)
    return total_len_diff


if __name__ == "__main__":
    file = Path(__file__)
    data = file.with_name(f"{file.stem}_input.txt").read_text()
    solution1 = part1(data)
    print(f"Solution 1: {solution1}")
    solution2 = part2(data)
    print(f"Solution 2: {solution2}")
