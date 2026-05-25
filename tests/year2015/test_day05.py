import pytest
from year2015.day05 import part1, part2

part1_examples: list[tuple[str, int]] = [
    ("ugknbfddgicrmopn", 1),
    ("aaa", 1),
    ("jchzalrnumimnmhp", 0),
    ("haegwjzuvuyypxyu", 0),
    ("dvszwmarrgswjxmb", 0),
]
part2_examples: list[tuple[str, int]] = [
    ("qjhvhtzxzqqjkmpb", 1),
    ("xxyxx", 1),
    ("uurcxstgmygtbstg", 0),
    ("ieodomkazucvgmuy", 0),
]


@pytest.mark.parametrize(("data", "expected"), part1_examples)
def test_part1_examples(data, expected):
    assert part1(data) == expected


@pytest.mark.parametrize(("data", "expected"), part2_examples)
def test_part2_examples(data, expected):
    assert part2(data) == expected
