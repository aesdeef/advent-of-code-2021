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

INPUT_FILE = "../../input/21.txt"
# INPUT_FILE = "test.txt"

with open(INPUT_FILE) as f:
    positions = []
    for line in f.read().splitlines():
        positions.append(int(line.split(": ")[-1]))

scores = [0, 0]

die = cycle(range(1, 101))

for turn in count():
    rolls = sum(die.__next__() for _ in range(3))
    player = turn % 2
    new_pos = (positions[player] + rolls) % 10 or 10
    positions[player] = new_pos
    scores[player] += new_pos
    if scores[player] >= 1000:
        part1 = min(scores) * (turn + 1) * 3
        break

print(part1)
