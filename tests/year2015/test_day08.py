import pytest
from year2015.day08 import part1, part2

part1_examples: list[tuple[str, int]] = [
    ('""', 2),
    ('"abc"', 2),
    ('"aaa\\"aaa"', 3),
    ('"\\x27"', 5),
    ('""\n"abc"\n"aaa\\"aaa"\n"\\x27"', 12),
]
part2_examples: list[tuple[str, int]] = [
    ('""', 4),
    ('"abc"', 4),
    ('"aaa\\"aaa"', 6),
    ('"\\x27"', 5),
    ('""\n"abc"\n"aaa\\"aaa"\n"\\x27"', 19),
]


@pytest.mark.parametrize(("data", "expected"), part1_examples)
def test_part1_examples(data, expected):
    assert part1(data) == expected


@pytest.mark.parametrize(("data", "expected"), part2_examples)
def test_part2_examples(data, expected):
    assert part2(data) == expected
