from pathlib import Path
import re


raindeer_pattern = r"^(?P<name>\w+) can fly (?P<speed>\d+) km/s for (?P<duration>\d+) seconds, but then must rest for (?P<rest>\d+) seconds.$"


def raindeer_pos(raindeer_data: str, time: int) -> dict[str, int]:
    raindeer = {}
    for raindeer_stats in re.finditer(raindeer_pattern, raindeer_data, re.MULTILINE):
        name = raindeer_stats["name"]
        speed = int(raindeer_stats["speed"])
        duration = int(raindeer_stats["duration"])
        rest = int(raindeer_stats["rest"])
        cycle_distance = speed * duration
        cycle_duration = duration + rest
        num_cycles = time // cycle_duration
        res_cycle = time % cycle_duration
        distance = cycle_distance * num_cycles + min(duration, res_cycle) * speed
        raindeer[name] = distance
    return raindeer


def part1(raindeer_data: str, time: int) -> int:
    return max(raindeer_pos(raindeer_data, time).values())


def part2(raindeer_data: str, time: int) -> int:
    raindeer = {}
    for t in range(1, time + 1):
        lead_names = []
        lead_pos = 0
        for name, pos in raindeer_pos(raindeer_data, t).items():
            if pos > lead_pos:
                lead_pos = pos
                lead_names = [name]
            elif pos == lead_pos:
                lead_names.append(name)
        for name in lead_names:
            if name not in raindeer:
                raindeer[name] = 0
            raindeer[name] += 1
    return max(raindeer.values())


if __name__ == "__main__":
    file = Path(__file__)
    data = file.with_name(f"{file.stem}_input.txt").read_text()
    solution1 = part1(data, 2503)
    print(f"Solution 1: {solution1}")
    solution2 = part2(data, 2503)
    print(f"Solution 2: {solution2}")
