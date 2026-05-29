from pathlib import Path
import re
from itertools import pairwise
import math


HappinessMatrix = dict[str, dict[str, int]]


seating_preference_pattern = re.compile(
    r"^(?P<person>\w+) would (?P<polarity>gain|lose) (?P<amount>\d+) happiness units by sitting next to (?P<neighbor>\w+)\.$",
    re.MULTILINE,
)


def build_happiness_matrix(seating_preferences: str) -> HappinessMatrix:
    happiness_matrix: HappinessMatrix = {}
    for seating_preference in seating_preference_pattern.finditer(seating_preferences):
        person = seating_preference["person"]
        neighbor = seating_preference["neighbor"]
        value = (1 - 2 * (seating_preference["polarity"] == "lose")) * int(
            seating_preference["amount"]
        )
        if person not in happiness_matrix:
            happiness_matrix[person] = {}
        happiness_matrix[person][neighbor] = value
    return happiness_matrix


def compute_happiness(happiness_matrix: HappinessMatrix, person1: str, person2: str):
    return happiness_matrix[person1][person2] + happiness_matrix[person2][person1]


def assign_seat(
    happiness_matrix: HappinessMatrix, arrangement: list[str], unseated: set[str]
) -> int:
    if not unseated:
        happiness = compute_happiness(happiness_matrix, arrangement[-1], arrangement[0])
        for person1, person2 in pairwise(arrangement):
            happiness += compute_happiness(happiness_matrix, person1, person2)
        return happiness
    max_happiness = -math.inf
    for person in unseated:
        happiness = assign_seat(
            happiness_matrix, [*arrangement, person], unseated - {person}
        )
        max_happiness = max(happiness, max_happiness)
    return max_happiness


def part1(seating_preferences: str) -> int:
    happiness_matrix = build_happiness_matrix(seating_preferences)
    return assign_seat(happiness_matrix, [], set(happiness_matrix.keys()))


def part2(seating_preferences: str) -> int:
    happiness_matrix = build_happiness_matrix(seating_preferences)
    happiness_matrix["Me"] = {}
    for person in happiness_matrix:
        happiness_matrix["Me"][person] = 0
        happiness_matrix[person]["Me"] = 0
    return assign_seat(happiness_matrix, [], set(happiness_matrix.keys()))


if __name__ == "__main__":
    file = Path(__file__)
    data = file.with_name(f"{file.stem}_input.txt").read_text()
    solution1 = part1(data)
    print(f"Solution 1: {solution1}")
    solution2 = part2(data)
    print(f"Solution 2: {solution2}")
