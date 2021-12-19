import re
from collections import Counter, defaultdict, deque
from functools import cache
from itertools import (
    chain,
    combinations,
    combinations_with_replacement,
    count,
    cycle,
    permutations,
    product,
)

# READ THE ENTIRE DESCRIPTION FIRST

INPUT_FILE = "../../input/19.txt"
# INPUT_FILE = "test.txt"

with open(INPUT_FILE) as f:
    scans = f.read().strip().split("\n\n")
    scanners = []
    for scan in scans:
        s = {
            tuple(int(x) for x in line.strip().split(","))
            for line in scan.split("\n")[1:]
        }
        scanners.append(s)


def rotate(scanner_id):
    scanner = scanners[scanner_id]
    for order in permutations([0, 1, 2], 3):
        for signs in {
            (1, 1, 1),
            (1, 1, -1),
            (1, -1, 1),
            (1, -1, -1),
            (-1, 1, 1),
            (-1, 1, -1),
            (-1, -1, 1),
            (-1, -1, -1),
        }:
            # skip indirect symmetries
            # if (sum(a == b for a, b in zip(order, (0, 1, 2))) + signs.count(-1)) % 2:
            #    continue
            s = {
                (
                    signs[0] * line[order[0]],
                    signs[1] * line[order[1]],
                    signs[2] * line[order[2]],
                )
                for line in scanner
            }
            yield s, order, signs


def diff(pos1, pos2):
    return tuple(a - b for a, b in zip(pos1, pos2))


class NoMatch(ValueError):
    pass


def match(first_id, second_id):
    first = scanners[first_id]
    for rotation, order, signs in rotate(second_id):
        diffs = []
        for a, b in product(first, rotation):
            diffs.append(diff(a, b))
        c = Counter(diffs)
        if any(x >= 12 for x in c.values()):
            delta = max(c.keys(), key=lambda x: c[x])
            scanners[second_id] = [
                [x + delta[0], y + delta[1], z + delta[2]] for x, y, z in rotation
            ]
            return c, order, signs
    raise NoMatch


all_ = set(range(len(scanners)))
rotated = {0}

while len(all_) - len(rotated):
    matched = False
    for reference in list(rotated):
        if matched:
            break
        for pick in list(all_ - rotated):
            try:
                match(reference, pick)
                print(reference, pick)
                rotated.add(pick)
                matched = True
                break
            except NoMatch:
                continue
    if not matched:
        raise ValueError

beacons = set()
for s in scanners:
    for b in s:
        beacons.add(tuple(b))

print(beacons)
print(len(beacons))
