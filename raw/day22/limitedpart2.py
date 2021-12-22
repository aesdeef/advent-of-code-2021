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

INPUT_FILE = "../../input/22.txt"
INPUT_FILE = "test2.txt"

Cuboid = tuple[tuple[int, int], tuple[int, int], tuple[int, int]]

with open(INPUT_FILE) as f:
    instr = list()
    for line in f:
        cmd, coords = line.strip().split()
        parts = coords.split(",")
        coo = []
        for part in parts:
            coo.append(tuple(int(x) for x in part[2:].split("..")))
        instr.append((cmd, tuple(coo)))


def subtract_axis(a, b):
    a_min, a_max = a
    b_min, b_max = b

    if a_min < b_min and b_max < a_max:
        return ((a_min, b_min - 1), b, (b_max + 1, a_max)), (True, False, True)

    if a_min < b_min and a_max < b_max:
        return ((a_min, b_min - 1), (b_min, a_max)), (True, False)

    if b_min < a_min and a_max < b_max:
        return (a,), (False,)

    if b_min < a_min and b_max < a_max:
        return ((a_min, b_max), (b_max + 1, a_max)), (False, True)

    return (a,), (True,)


def subtract(a: Cuboid, b: Cuboid) -> set[Cuboid]:
    remaining = set()
    for x_axis, x_in in zip(*subtract_axis(a[0], b[0])):
        for y_axis, y_in in zip(*subtract_axis(a[1], b[1])):
            for z_axis, z_in in zip(*subtract_axis(a[2], b[2])):
                if any((x_in, y_in, z_in)):
                    remaining.add((x_axis, y_axis, z_axis))
    return remaining


cuboids_on = set()

for inst in instr:
    cmd, cuboid = inst
    if cmd == "on":
        cuboids_on.add(cuboid)
        continue

    new_cuboids_on = set()
    for c_on in cuboids_on:
        new_cuboids_on |= subtract(c_on, cuboid)

    cuboids_on = set()
    for cuboid in new_cuboids_on:
        x, y, z = cuboid
        print(x, y, z)
        if any(w[1] < -50 for w in cuboid) or any(w[0] > 50 for w in cuboid):
            continue
        x = (max(x[0], -50), min(x[1], 50))
        y = (max(y[0], -50), min(y[1], 50))
        z = (max(z[0], -50), min(z[1], 50))
        cuboids_on.add((x, y, z))


def size(cuboid):
    x_len = cuboid[0][1] + 1 - cuboid[0][0]
    y_len = cuboid[1][1] + 1 - cuboid[2][0]
    z_len = cuboid[1][1] + 1 - cuboid[2][0]
    return x_len * y_len * z_len


lit = sum(size(cuboid) for cuboid in cuboids_on)
print(lit)
