import pytest
from year2015.day09 import part1, part2

part1_examples: list[tuple[str, int]] = [
    ("London to Dublin = 464\nLondon to Belfast = 518\nDublin to Belfast = 141", 605)
]
part2_examples: list[tuple[str, int]] = [
    ("London to Dublin = 464\nLondon to Belfast = 518\nDublin to Belfast = 141", 982)
]


@pytest.mark.parametrize(("data", "expected"), part1_examples)
def test_part1_examples(data, expected):
    assert part1(data) == expected


@pytest.mark.parametrize(("data", "expected"), part2_examples)
def test_part2_examples(data, expected):
    assert part2(data) == expected
