from pathlib import Path


moves = {
    "^": (0, 1),
    ">": (1, 0),
    "v": (0, -1),
    "<": (-1, 0),
}


def make_move(pos: tuple[int, int], move: tuple[int, int]) -> tuple[int, int]:
    return (pos[0] + move[0], pos[1] + move[1])


def part1(data: str) -> int:
    pos = (0, 0)
    visited = {pos}
    for direction in data:
        move = moves[direction]
        pos = make_move(pos, move)
        visited.add(pos)
    return len(visited)


def part2(data: str) -> int:
    pos1 = (0, 0)
    pos2 = (0, 0)
    visited = {pos1, pos2}
    for index, direction in enumerate(data):
        move = moves[direction]
        if index % 2:
            pos1 = make_move(pos1, move)
            visited.add(pos1)
        else:
            pos2 = make_move(pos2, move)
            visited.add(pos2)
    return len(visited)


if __name__ == "__main__":
    file = Path(__file__)
    data = file.with_name(f"{file.stem}_input.txt").read_text()
    solution1 = part1(data)
    solution2 = part2(data)
    print(f"Solution 1: {solution1}")
    print(f"Solution 2: {solution2}")
