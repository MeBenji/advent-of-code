from pathlib import Path


naughty_strings = {"ab", "cd", "pq", "xy"}


def has_three_vowels(string: str) -> bool:
    vowel_count = 0
    for c in string:
        if c in "aeiou":
            vowel_count += 1
            if vowel_count >= 3:
                return True
    return False


def has_repeat(string: str) -> bool:
    return any(string[i] == string[i - 1] for i in range(1, len(string)))


def has_naughty_string(string: str) -> bool:
    return any(ns in string for ns in naughty_strings)


def part1(strings: str) -> int:
    def is_nice(string: str) -> bool:
        return all(
            (
                has_three_vowels(string),
                has_repeat(string),
                not has_naughty_string(string),
            )
        )

    return sum(is_nice(s) for s in strings.splitlines())


def has_repeat_pair(string: str) -> bool:
    return any(string[i : i + 2] in string[i + 2 :] for i in range(0, len(string) - 3))


def has_one_gap_repeat(string: str) -> bool:
    return any(string[i] == string[i + 2] for i in range(0, len(string) - 2))


def part2(strings: str) -> int:
    def is_nice(string: str) -> bool:
        return all(
            (
                has_repeat_pair(string),
                has_one_gap_repeat(string),
            )
        )

    return sum(is_nice(s) for s in strings.split("\n"))


if __name__ == "__main__":
    file = Path(__file__)
    data = file.with_name(f"{file.stem}_input.txt").read_text()
    solution1 = part1(data)
    print(f"Solution 1: {solution1}")
    solution2 = part2(data)
    print(f"Solution 2: {solution2}")
