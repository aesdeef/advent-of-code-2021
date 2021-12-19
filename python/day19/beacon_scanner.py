from collections import Counter
from itertools import chain, combinations, product
from typing import Generator

INPUT_FILE = "../../input/19.txt"

Vector = tuple[int, int, int]
Scanner = set[Vector]


def parse_input() -> dict[int, Scanner]:
    """
    Parses the input and return a dict of scanner number and their scans as a
    set of position vectors
    """
    with open(INPUT_FILE) as f:
        scans = f.read().strip().split("\n\n")

    scanners: dict[int, Scanner] = {}
    for i, scan in enumerate(scans):
        vectors: set[Vector] = set()
        for line in scan.split("\n")[1:]:
            x, y, z = line.strip().split(",")
            vectors.add((int(x), int(y), int(z)))
        scanners[i] = vectors
    return scanners


def rotate_x(scanner: Scanner) -> Scanner:
    """
    Rotates the scanner through π/2 about the x-axis
    """
    return {(x, z, -y) for x, y, z in scanner}


def rotate_y(scanner: Scanner) -> Scanner:
    """
    Rotates the scanner through π/2 about the y-axis
    """
    return {(-z, y, x) for x, y, z in scanner}


def rotate_z(scanner: Scanner) -> Scanner:
    """
    Rotates the scanner through π/2 about the z-axis
    """
    return {(y, -x, z) for x, y, z in scanner}


def rotate_y_twice(scanner: Scanner) -> Scanner:
    """
    Rotates the scanner through π about the y-axis
    """
    return {(-x, y, -z) for x, y, z in scanner}


def get_direct_symmetries(scanner: Scanner) -> Generator[Scanner, None, None]:
    """
    Generates all orientations of the scanner
    """

    short_cycle = [rotate_x] * 3 + [rotate_y_twice] + [rotate_x] * 3
    full_cycle = short_cycle + [rotate_z] + short_cycle + [rotate_y] + short_cycle

    yield scanner
    for rotate in full_cycle:
        scanner = rotate(scanner)
        yield scanner


def distance(first: Vector, second: Vector) -> Vector:
    """
    Calculates the difference of two position vectors
    """
    return (first[0] - second[0], first[1] - second[1], first[2] - second[2])


def match(
    oriented_scanner: Scanner, other_scanner: Scanner
) -> tuple[Scanner, Vector] | None:
    """
    Returns the scans of the other_scanner relative to the oriented_scanner
    and the position of the other_scanner relative to the oriented_scanner
    or None, if the scanners have less than 12 beacons in common
    """
    for symmetry in get_direct_symmetries(other_scanner):
        distance_counter: Counter[Vector] = Counter()
        for a, b in product(oriented_scanner, symmetry):
            distance_counter[distance(a, b)] += 1
        for vector, count in distance_counter.items():
            if count >= 12:
                absolute_scanner = {
                    (x + vector[0], y + vector[1], z + vector[2])
                    for x, y, z in symmetry
                }
                return absolute_scanner, vector
    return None


def orient_scanners(scanners: dict[int, Scanner]) -> tuple[list[Scanner], set[Vector]]:
    """
    Orients all scanners relative to Scanner 0 and returns a list of oriented
    scanners and a set of the positions of scanners
    """
    oriented_scanners = {0: scanners[0]}
    scanner_positions: dict[int, Vector] = {0: (0, 0, 0)}
    while not_oriented_scanners := set(scanners) - set(oriented_scanners):
        for oriented, new in product(oriented_scanners, not_oriented_scanners):
            oriented_scanner = oriented_scanners[oriented]
            new_scanner = scanners[new]
            if output := match(oriented_scanner, new_scanner):
                scanner, vector = output
                oriented_scanners[new] = scanner
                scanner_positions[new] = vector
                break
    return list(oriented_scanners.values()), set(scanner_positions.values())


def solve_part1(oriented_scanners: list[Scanner]) -> int:
    """
    Calculates the solution for part 1
    """
    beacons = set(chain(*oriented_scanners))
    return len(beacons)


def manhattan_distance(a: Vector, b: Vector) -> int:
    """
    Calculates the Manhattan distance between two position vectors
    """
    return sum(abs(x - y) for x, y in zip(a, b))


def solve_part2(scanner_positions: set[Vector]) -> int:
    """
    Calculates the solution for part 2
    """
    return max(manhattan_distance(a, b) for a, b in combinations(scanner_positions, 2))


if __name__ == "__main__":
    scanners = parse_input()
    oriented_scanners, scanner_positions = orient_scanners(scanners)
    part1 = solve_part1(oriented_scanners)
    part2 = solve_part2(scanner_positions)

    print(part1)
    print(part2)
