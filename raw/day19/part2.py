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
            yield s


def diff(pos1, pos2):
    return tuple(a - b for a, b in zip(pos1, pos2))


class NoMatch(ValueError):
    pass


def match(first_id, second_id):
    first = scanners[first_id]
    for rotation in rotate(second_id):
        diffs = []
        for a, b in product(first, rotation):
            diffs.append(diff(a, b))
        c = Counter(diffs)
        for key, val in c.items():
            if val >= 12:
                delta = key
                scanners[second_id] = [
                    [x + delta[0], y + delta[1], z + delta[2]] for x, y, z in rotation
                ]
                return delta
    raise NoMatch


all_ = set(range(len(scanners)))
rotated = {0}

deltas = {0: (0, 0, 0)}

while len(all_) - len(rotated):
    matched = False
    for reference in list(rotated):
        if matched:
            break
        for pick in list(all_ - rotated):
            try:
                relative_delta = match(reference, pick)
                abs_delta = tuple(
                    a + b for a, b in zip(deltas[reference], relative_delta)
                )
                # deltas[pick] = abs_delta
                deltas[pick] = relative_delta
                print(reference, pick, relative_delta, deltas[reference], abs_delta)
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

print(len(beacons))

ds = []
for first, second in permutations(all_, 2):
    d = sum(abs(a - b) for a, b in zip(deltas[first], deltas[second]))
    ds.append(d)
print(max(ds))
