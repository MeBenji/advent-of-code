from pathlib import Path
import re


instruction_pattern = r"(?P<command>turn on|turn off|toggle)\s(?P<cord1>\d+,\d+)\sthrough\s(?P<cord2>\d+,\d+)"


def turn_on(lights, cord1, cord2):
    for x in range(cord1[0], cord2[0] + 1):
        for y in range(cord1[1], cord2[1] + 1):
            lights[x][y] = 1


def turn_off(lights, cord1, cord2):
    for x in range(cord1[0], cord2[0] + 1):
        for y in range(cord1[1], cord2[1] + 1):
            lights[x][y] = 0


def toggle(lights, cord1, cord2):
    for x in range(cord1[0], cord2[0] + 1):
        for y in range(cord1[1], cord2[1] + 1):
            lights[x][y] = not lights[x][y]


def part1(instructions: str) -> int:
    commands = {"turn on": turn_on, "turn off": turn_off, "toggle": toggle}
    lights = [[False for _ in range(1000)] for _ in range(1000)]
    for instruction in instructions.splitlines():
        instruction_match = re.fullmatch(instruction_pattern, instruction)
        command = instruction_match["command"]
        cord1 = [int(c) for c in instruction_match["cord1"].split(",")]
        cord2 = [int(c) for c in instruction_match["cord2"].split(",")]
        commands[command](lights, cord1, cord2)
    return sum(sum(x) for x in lights)


def increase_brightness(lights, cord1, cord2, amount):
    for x in range(cord1[0], cord2[0] + 1):
        for y in range(cord1[1], cord2[1] + 1):
            lights[x][y] += amount


def decrease_brightness(lights, cord1, cord2):
    for x in range(cord1[0], cord2[0] + 1):
        for y in range(cord1[1], cord2[1] + 1):
            lights[x][y] = max(lights[x][y] - 1, 0)


def part2(instructions: str) -> int:
    commands = {
        "turn on": lambda *args: increase_brightness(*args, amount=1),
        "turn off": decrease_brightness,
        "toggle": lambda *args: increase_brightness(*args, amount=2),
    }
    lights = [[False for _ in range(1000)] for _ in range(1000)]
    for instruction in instructions.splitlines():
        instruction_match = re.fullmatch(instruction_pattern, instruction)
        command = instruction_match["command"]
        cord1 = [int(c) for c in instruction_match["cord1"].split(",")]
        cord2 = [int(c) for c in instruction_match["cord2"].split(",")]
        commands[command](lights, cord1, cord2)
    return sum(sum(x) for x in lights)


if __name__ == "__main__":
    file = Path(__file__)
    data = file.with_name(f"{file.stem}_input.txt").read_text()
    solution1 = part1(data)
    print(f"Solution 1: {solution1}")
    solution2 = part2(data)
    print(f"Solution 2: {solution2}")
