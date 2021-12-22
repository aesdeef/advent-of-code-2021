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
# INPUT_FILE = "test.txt"
# INPUT_FILE = "test2.txt"
# INPUT_FILE = "test3.txt"

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

    if a_max < b_min or b_max < a_min:
        return (a,), (True,)

    if b_min <= a_min < a_max <= b_max:
        return (a,), (False,)

    if a_min == a_max:
        t = not (b_min <= a_min <= b_max)
        return (a,), (t,)

    if b_min == b_max:
        if a_min == b_min:
            return (b, (a_min + 1, a_max)), (False, True)
        if a_max == b_min:
            return ((a_min, a_max - 1), b), (True, False)
        if a_min < b_min < a_max:
            return ((a_min, b_min - 1), b, (b_min + 1, a_max)), (True, False, True)
        else:
            return (a,), (True,)

    if a_max == b_min:
        return ((a_min, b_min - 1), (b_min, a_max)), (True, False)

    if b_max == a_min:
        return ((a_min, b_max), (a_min + 1, a_max)), (False, True)

    if a_min == b_min:
        if b_max < a_max:
            return (b, (b_max + 1, a_max)), (False, True)

        else:
            raise ValueError

    if a_max == b_max:
        if a_min < b_min:
            return ((a_min, b_min - 1), b), (True, False)

        else:
            raise ValueError

    if a_min < b_min < b_max < a_max:
        return ((a_min, b_min - 1), b, (b_max + 1, a_max)), (True, False, True)

    if a_min < b_min < a_max < b_max:
        return ((a_min, b_min - 1), (b_min, a_max)), (True, False)

    if b_min < a_min < b_max < a_max:
        return ((a_min, b_max), (b_max + 1, a_max)), (False, True)


def subtract(a: Cuboid, b: Cuboid) -> set[Cuboid]:
    remaining = set()
    cut_x = cut_y = None
    for x_axis, x_in in zip(*subtract_axis(a[0], b[0])):
        if x_in:
            remaining.add((x_axis, a[1], a[2]))
        else:
            cut_x = x_axis
    if not cut_x:
        return remaining

    for y_axis, y_in in zip(*subtract_axis(a[1], b[1])):
        if y_in:
            remaining.add((cut_x, y_axis, a[2]))
        else:
            cut_y = y_axis
    if not cut_y:
        return remaining

    for z_axis, z_in in zip(*subtract_axis(a[2], b[2])):
        if z_in:
            remaining.add((cut_x, cut_y, z_axis))
    return remaining


def size(cuboid):
    x_len = cuboid[0][1] + 1 - cuboid[0][0]
    y_len = cuboid[1][1] + 1 - cuboid[1][0]
    z_len = cuboid[2][1] + 1 - cuboid[2][0]
    return x_len * y_len * z_len


cuboids_on = set()

for inst in instr:
    # print(sorted(cuboids_on))
    # print(sum(size(c) for c in cuboids_on))
    cmd, cuboid = inst

    new_cuboids_on = set()
    for c_on in cuboids_on:
        result = subtract(c_on, cuboid)
        """
        for c in result:
            for w in c:
                if w[0] > w[1]:
                    print("subtracting", c_on, cuboid)
                    print("result", result)
                    print(c, w)
                    raise NotImplementedError
        """
        new_cuboids_on |= result

    cuboids_on = new_cuboids_on
    # print(sorted(cuboids_on))
    # print(sum(size(c) for c in cuboids_on))

    if cmd == "on":
        cuboids_on.add(cuboid)
        # print(sum(size(c) for c in cuboids_on))
        continue


lit = sum(size(cuboid) for cuboid in cuboids_on)
print(lit)
