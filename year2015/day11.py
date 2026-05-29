from pathlib import Path


CONFUSING_LETTERS = "iol"
ORD_OFFSET = 97
ALPHABET_SIZE = 26


def encode(pw: str) -> list[int]:
    return [ord(c) - ORD_OFFSET for c in pw]


def decode(pw: list[int]) -> str:
    return "".join(chr(num + ORD_OFFSET) for num in pw)


def increment(pw: list[int]) -> None:
    for i in range(len(pw) - 1, -1, -1):
        pw[i] = (pw[i] + 1) % ALPHABET_SIZE
        if not pw[i]:
            continue
        return


def has_increasing_straight(pw_e: list[int]) -> bool:
    for first, second, third in zip(pw_e, pw_e[1:], pw_e[2:]):
        if first + 2 == second + 1 == third:
            return True
    return False


def has_confusing_letters(pw_e: list[int]) -> bool:
    return any(letter in pw_e for letter in encode(CONFUSING_LETTERS))


def has_two_pairs(pw_e: list[int]) -> bool:
    for i in range(len(pw_e) - 3):
        if pw_e[i] == pw_e[i + 1]:
            for j in range(i, len(pw_e) - 1):
                if pw_e[j] == pw_e[j + 1] != pw_e[i]:
                    return True
            return False
    return False


def get_next_password(pw: str) -> str:
    pw_e = encode(pw)
    increment(pw_e)
    while (
        not has_increasing_straight(pw_e)
        or has_confusing_letters(pw_e)
        or not has_two_pairs(pw_e)
    ):
        increment(pw_e)
    return decode(pw_e)


def part1(pw: str) -> str:
    return get_next_password(pw)


def part2(pw: str) -> str:
    return get_next_password(pw)


if __name__ == "__main__":
    file = Path(__file__)
    data = file.with_name(f"{file.stem}_input.txt").read_text()
    solution1 = part1(data)
    print(f"Solution 1: {solution1}")
    solution2 = part2(solution1)
    print(f"Solution 2: {solution2}")
