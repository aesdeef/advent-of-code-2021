import re
from collections import Counter, deque
from itertools import chain, count

# READ THE ENTIRE DESCRIPTION FIRST

INPUT_FILE = "../../input/15.txt"
# INPUT_FILE = "test.txt"

with open(INPUT_FILE) as f:
    risk_levels = [[int(x) for x in line.strip()] for line in f]

height = len(risk_levels)
width = len(risk_levels[0])

paths = []
options = deque([(((0, 0),), 0)])
bests = {(0, 0): [((0, 0),), 0]}


def get_new_coords(coords):
    x, y = coords
    options = set()
    for a, b in {
        (x - 1, y),
        (x + 1, y),
        (x, y - 1),
        (x, y + 1),
    }:
        if 0 <= a < width and 0 <= b < height:
            options.add((a, b))
    return options


while options:
    path, risk = options.popleft()
    curr = path[-1]

    for option in get_new_coords(curr):
        x, y = option
        new_risk = risk + risk_levels[y][x]
        new_tuple = (path + (option,), new_risk)
        if option in bests and bests[option][1] <= new_risk:
            continue
        else:
            bests[option] = new_tuple
        options.append(new_tuple)

print(bests[(height - 1, width - 1)][1])
