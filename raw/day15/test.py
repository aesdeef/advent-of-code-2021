import re
from collections import Counter, deque
from itertools import chain, count

# READ THE ENTIRE DESCRIPTION FIRST

INPUT_FILE = "../../input/15.txt"
# INPUT_FILE = "test.txt"

with open(INPUT_FILE) as f:
    risk_levels = [[int(x) for x in line.strip()] for line in f]


def add_one(row):
    return [1 if x == 9 else x + 1 for x in row]


scaled_x = []
for row in risk_levels:
    new_row = row
    temp_row = row
    for _ in range(4):
        temp_row = add_one(temp_row)
        new_row.extend(temp_row)
    scaled_x.append(new_row)

risk_levels = scaled_x[:]

temp_tier = scaled_x[:]
for _ in range(4):
    new_tier = []
    for row in temp_tier:
        new_tier.append(add_one(row))
    temp_tier = new_tier
    risk_levels.extend(new_tier)


height = len(risk_levels)
width = len(risk_levels[0])

[print(row) for row in risk_levels]

paths = []
options = {(0, 0): 0}
bests = {(0, 0): 0}


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


def nearest(options):
    return min(options, key=lambda x: (height + width - x[0] - x[1]))


def smallest_risk(options):
    min_risk = min(options.values())
    for x in options:
        if options[x] == min_risk:
            return x


while options:
    # curr = nearest(options.keys())
    curr = smallest_risk(options)
    risk = options[curr]
    del options[curr]

    if (height - 1, width - 1) in bests and bests[(height - 1, width - 1)] < risk:
        continue

    if curr == (height - 1, width - 1):
        print(risk)
        continue

    for option in get_new_coords(curr):
        x, y = option
        new_risk = risk + risk_levels[y][x]
        if option in bests and bests[option] <= new_risk:
            continue
        if option in options and options[option] <= new_risk:
            continue
        bests[option] = new_risk
        options[option] = new_risk

print(bests[(height - 1, width - 1)])
