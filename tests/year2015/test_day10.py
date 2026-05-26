import pytest
from year2015.day10 import part1, part2

part1_examples: list[tuple[str, int, int]] = [
    ("1", 1, 2),
    ("11", 1, 2),
    ("21", 1, 4),
    ("1211", 1, 6),
    ("111221", 1, 6),
    ("1", 2, 2),
    ("1", 3, 4),
    ("1", 4, 6),
    ("1", 5, 6),
]
part2_examples: list[tuple[str, int, int]] = [
    ("1", 1, 2),
    ("11", 1, 2),
    ("21", 1, 4),
    ("1211", 1, 6),
    ("111221", 1, 6),
    ("1", 2, 2),
    ("1", 3, 4),
    ("1", 4, 6),
    ("1", 5, 6),
]


@pytest.mark.parametrize(("sequence", "iterations", "expected"), part1_examples)
def test_part1_examples(sequence, iterations, expected):
    assert part1(sequence, iterations) == expected


@pytest.mark.parametrize(("sequence", "iterations", "expected"), part2_examples)
def test_part2_examples(sequence, iterations, expected):
    assert part2(sequence, iterations) == expected
