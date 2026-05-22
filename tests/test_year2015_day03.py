import pytest
from year2015.day03 import part1, part2

part1_examples: list[tuple[str, int | str]] = [(">", 2), ("^>v<", 4), ("^v^v^v^v^v", 2)]
part2_examples: list[tuple[str, int | str]] = [
    ("^v", 3),
    ("^>v<", 3),
    ("^v^v^v^v^v", 11),
]


@pytest.mark.parametrize(("data", "expected"), part1_examples)
def test_part1_examples(data, expected):
    assert part1(data) == expected


@pytest.mark.parametrize(("data", "expected"), part2_examples)
def test_part2_examples(data, expected):
    assert part2(data) == expected
