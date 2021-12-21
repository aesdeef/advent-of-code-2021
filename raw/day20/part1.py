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

INPUT_FILE = "../../input/20.txt"
# INPUT_FILE = "test.txt"

with open(INPUT_FILE) as f:
    algo = f.readline().strip()
    f.readline()
    image = [line.strip() for line in f]
    imgdict = defaultdict(int)
    for y, row in enumerate(image):
        for x, cell in enumerate(row):
            imgdict[(x, y)] = 1


def get_new(tiles):
    """ignore"""
    num = re.sub(r"\.", "0", re.sub(r"#", "1", tiles))
    return algo[int(num, 2)]


def new_tile(tilesdict, x, y):
    tiles = []
    for a in (-1, 0, 1):
        for b in (-1, 0, 1):
            tiles.append(str(tilesdict[(x + b, y + a)]))

    return 1 if algo[int("".join(tiles), 2)] == "#" else 0


def step(imgdict, default=0):
    min_y = min(x[1] for x in imgdict.keys()) - 1
    max_y = max(x[1] for x in imgdict.keys()) + 1
    min_x = min(x[0] for x in imgdict.keys()) - 1
    max_x = max(x[0] for x in imgdict.keys()) + 1

    if algo[0] == "#":
        default = 1 - default

    newdict = defaultdict(lambda: default)
    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):
            new = new_tile(imgdict, x, y)
            newdict[(x, y)] = new
    return newdict, default


after_one, default = step(imgdict)
after_two, default = step(after_one, default)
print(sum(x == 1 for x in after_two.values()))
