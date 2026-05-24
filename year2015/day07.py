from pathlib import Path
from collections.abc import Callable


operations: dict[str, Callable[[int, int], int]] = {
    "AND": lambda operand1, operand2: operand1 & operand2,
    "OR": lambda operand1, operand2: operand1 | operand2,
    "LSHIFT": lambda operand1, operand2: operand1 << operand2,
    "RSHIFT": lambda operand1, operand2: operand1 >> operand2,
    "NOT": lambda _, operand2: ~operand2,
}


def get_signal(signals: dict[str, int | list[str]], wire: str) -> int:
    source = signals[wire]
    if isinstance(source, int):
        return source
    expression = source.pop()
    expression = (
        int(expression) if expression.isdigit() else get_signal(signals, expression)
    )
    signal = None
    if not source:
        signal = expression
    else:
        operand2 = expression
        gate = source.pop()
        operand1 = None
        if source:
            operand1 = source.pop()
            operand1 = (
                int(operand1) if operand1.isdigit() else get_signal(signals, operand1)
            )
        signal = operations[gate](operand1, operand2) % (2**16)
    signals[wire] = signal
    return signal


def part1(circuit: str, wire: str) -> int:
    signals: dict[str, int | list[str]] = {}
    for connection in circuit.splitlines():
        source, wire_id = connection.split(" -> ")
        signals[wire_id] = source.split()
    return get_signal(signals, wire)


def part2(circuit: str, wire: str, override: str) -> int:
    signals: dict[str, int | list[str]] = {}
    for connection in (f"{circuit}\n{override}").splitlines():
        source, wire_id = connection.split(" -> ")
        signals[wire_id] = source.split()
    return get_signal(signals, wire)


if __name__ == "__main__":
    file = Path(__file__)
    data = file.with_name(f"{file.stem}_input.txt").read_text()
    solution1 = part1(data, "a")
    print(f"Solution 1: {solution1}")
    solution2 = part2(data, "a", f"{solution1} -> b")
    print(f"Solution 2: {solution2}")
