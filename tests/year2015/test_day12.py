import pytest
from year2015.day12 import part1, part2

part1_examples: list[tuple[str, int | float]] = [
    ("[1,2,3]", 6),
    ('{"a":2,"b":4}', 6),
    ("[[[3]]]", 3),
    ('{"a":{"b":4},"c":-1}', 3),
    ('{"a":[-1,1]}', 0),
    ('[-1,{"a":1}]', 0),
    ("[]", 0),
    ("{}", 0),
]
part2_examples: list[tuple[str, str, int | float]] = [
    ("[1,2,3]", None, 6),
    ('{"a":2,"b":4}', None, 6),
    ("[[[3]]]", None, 3),
    ('{"a":{"b":4},"c":-1}', None, 3),
    ('{"a":[-1,1]}', None, 0),
    ('[-1,{"a":1}]', None, 0),
    ("[]", None, 0),
    ("{}", None, 0),
]


@pytest.mark.parametrize(("document", "expected"), part1_examples)
def test_part1_examples(document, expected):
    assert part1(document) == expected


@pytest.mark.parametrize(("document", "ignore", "expected"), part2_examples)
def test_part2_examples(document, ignore, expected):
    assert part2(document, ignore) == expected
