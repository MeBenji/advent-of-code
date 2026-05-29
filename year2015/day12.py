from pathlib import Path
import json


def deep_sum(node: any, ignore: str | None = None) -> int | float:
    if isinstance(node, int | float):
        return node
    if isinstance(node, list):
        return sum(deep_sum(e, ignore) for e in node)
    if isinstance(node, dict):
        if ignore is not None and ignore in node.values():
            return 0
        return sum(deep_sum(v, ignore) for v in node.values())
    return 0


def part1(json_doc: str) -> int | float:
    doc = json.loads(json_doc)
    return deep_sum(doc)


def part2(json_doc: str, ignore: str | None = None) -> int | float:
    doc = json.loads(json_doc)
    return deep_sum(doc, ignore)


if __name__ == "__main__":
    file = Path(__file__)
    data = file.with_name(f"{file.stem}_input.txt").read_text()
    solution1 = part1(data)
    print(f"Solution 1: {solution1}")
    solution2 = part2(data, "red")
    print(f"Solution 2: {solution2}")
