import pytest
from year2015.day07 import part1, part2

simple_circuit = "123 -> x\n456 -> y\nx AND y -> d\nx OR y -> e\nx LSHIFT 2 -> f\ny RSHIFT 2 -> g\nNOT x -> h\nNOT y -> i"

part1_examples: list[tuple[str, str, int]] = [
    (simple_circuit, "d", 72),
    (simple_circuit, "e", 507),
    (simple_circuit, "f", 492),
    (simple_circuit, "g", 114),
    (simple_circuit, "h", 65412),
    (simple_circuit, "i", 65079),
    (simple_circuit, "x", 123),
    (simple_circuit, "y", 456),
]
part2_examples: list[tuple[str, str, str, int]] = []


@pytest.mark.parametrize(("circuit", "wire", "expected"), part1_examples)
def test_part1_examples(circuit, wire, expected):
    assert part1(circuit, wire) == expected


@pytest.mark.parametrize(("data", "expected"), part2_examples)
def test_part2_examples(data, expected):
    assert part2(data) == expected
