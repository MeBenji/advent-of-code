import pytest
from year2015.day06 import part1, part2

part1_examples: list[tuple[str, int]] = [
    ("turn on 0,0 through 999,999", 1000000),
    ("toggle 0,0 through 999,0", 1000),
    ("turn off 499,499 through 500,500", 0),
]
part2_examples: list[tuple[str, int]] = [
    ("turn on 0,0 through 0,0", 1),
    ("toggle 0,0 through 999,999", 2000000),
]


@pytest.mark.parametrize(("data", "expected"), part1_examples)
def test_part1_examples(data, expected):
    assert part1(data) == expected


@pytest.mark.parametrize(("data", "expected"), part2_examples)
def test_part2_examples(data, expected):
    assert part2(data) == expected
