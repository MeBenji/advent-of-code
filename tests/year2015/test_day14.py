import pytest
from year2015.day14 import part1, part2

part1_examples: list[tuple[str, int, int]] = [
    (
        "Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.\n"
        "Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.",
        1000,
        1120,
    )
]
part2_examples: list[tuple[str, int, int]] = [
    (
        "Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.\n"
        "Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.",
        1000,
        689,
    )
]


@pytest.mark.parametrize(("raindeer_data", "time", "expected"), part1_examples)
def test_part1_examples(raindeer_data, time, expected):
    assert part1(raindeer_data, time) == expected


@pytest.mark.parametrize(("raindeer_data", "time", "expected"), part2_examples)
def test_part2_examples(raindeer_data, time, expected):
    assert part2(raindeer_data, time) == expected
