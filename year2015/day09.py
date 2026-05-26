from pathlib import Path
import re
import math


DistanceMatrix = dict[str, dict[str, int]]


def get_dist_matrix(distances: str) -> DistanceMatrix:
    dist_matrix = {}
    for loc_pair_dist in distances.splitlines():
        loc1, loc2, dist = re.split(r" (?:to|=) ", loc_pair_dist)
        if loc1 not in dist_matrix:
            dist_matrix[loc1] = {}
        if loc2 not in dist_matrix:
            dist_matrix[loc2] = {}
        dist_matrix[loc1][loc2] = int(dist)
        dist_matrix[loc2][loc1] = int(dist)
    return dist_matrix


def find_shortest_route_dist(
    dist_matrix: DistanceMatrix, unvisited: set[str], prev: str = ""
) -> int:
    if not unvisited:
        return 0
    min_dist = math.inf
    for loc in unvisited:
        dist = dist_matrix[prev][loc] if prev else 0
        dist += find_shortest_route_dist(dist_matrix, unvisited - {loc}, loc)
        min_dist = min(dist, min_dist)
    return min_dist


def part1(distances: str) -> int:
    dist_matrix = get_dist_matrix(distances)
    return find_shortest_route_dist(dist_matrix, set(dist_matrix.keys()))


def find_longest_route_dist(
    dist_matrix: DistanceMatrix, unvisited: set[str], prev: str = ""
) -> int:
    if not unvisited:
        return 0
    max_dist = 0
    for loc in unvisited:
        dist = dist_matrix[prev][loc] if prev else 0
        dist += find_longest_route_dist(dist_matrix, unvisited - {loc}, loc)
        max_dist = max(dist, max_dist)
    return max_dist


def part2(distances: str) -> int:
    dist_matrix = get_dist_matrix(distances)
    return find_longest_route_dist(dist_matrix, set(dist_matrix.keys()))


if __name__ == "__main__":
    file = Path(__file__)
    data = file.with_name(f"{file.stem}_input.txt").read_text()
    solution1 = part1(data)
    print(f"Solution 1: {solution1}")
    solution2 = part2(data)
    print(f"Solution 2: {solution2}")
