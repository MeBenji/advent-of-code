import pytest
from year2015.day04 import part1, part2

part1_examples: list[tuple[str, int]] = [("abcdef", 609043), ("pqrstuv", 1048970)]
part2_examples: list[tuple[str, int]] = []


@pytest.mark.parametrize(("data", "expected"), part1_examples)
def test_part1_examples(data, expected):
    assert part1(data) == expected


@pytest.mark.parametrize(("data", "expected"), part2_examples)
def test_part2_examples(data, expected):
    assert part2(data) == expected
