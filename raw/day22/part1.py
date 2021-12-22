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
INPUT_FILE = "test.txt"

with open(INPUT_FILE) as f:
    instr = list()
    for line in f:
        cmd, coords = line.strip().split()
        parts = coords.split(",")
        coo = []
        for part in parts:
            coo.append([int(x) for x in part[2:].split("..")])
        instr.append((cmd, coo))

cubes = {
    (x, y, z): False
    for x in range(-50, 51)
    for y in range(-50, 51)
    for z in range(-50, 51)
}

for cmd, crds in instr:
    x_r, y_r, z_r = crds
    x_min, x_max = x_r
    y_min, y_may = y_r
    z_min, z_maz = z_r
    for x in range(x_min, x_max + 1):
        for y in range(y_min, y_may + 1):
            for z in range(z_min, z_maz + 1):
                cubes[(x, y, z)] = cmd == "on"

c = Counter(cubes.values())
print(c[False])
