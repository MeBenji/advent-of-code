import pytest
from year2015.day02 import part1, part2

part1_examples: list[tuple[str, int]] = [("2x3x4", 58), ("1x1x10", 43)]
part2_examples: list[tuple[str, int]] = [("2x3x4", 34), ("1x1x10", 14)]


@pytest.mark.parametrize(("data", "expected"), part1_examples)
def test_part1_examples(data, expected):
    assert part1(data) == expected


@pytest.mark.parametrize(("data", "expected"), part2_examples)
def test_part2_examples(data, expected):
    assert part2(data) == expected
