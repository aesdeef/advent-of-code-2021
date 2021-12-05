import re
from collections import Counter

INPUT_FILE = "../../input/05.txt"


with open(INPUT_FILE) as f:
    data = [line.strip() for line in f]

covered = Counter()

for line in data:
    x1, y1, x2, y2 = [int(x) for x in re.findall(r"[0-9]+", line)]
    if x1 == x2:
        for y in range(min(y1, y2), max(y1, y2) + 1):
            covered[(x1, y)] += 1
    elif y1 == y2:
        for x in range(min(x1, x2), max(x1, x2) + 1):
            covered[(x, y1)] += 1
print(sum(1 for x in covered.values() if x > 1))

covered = Counter()
for line in data:
    x1, y1, x2, y2 = [int(x) for x in re.findall(r"[0-9]+", line)]
    if x1 == x2:
        for y in range(min(y1, y2), max(y1, y2) + 1):
            covered[(x1, y)] += 1
    elif y1 == y2:
        for x in range(min(x1, x2), max(x1, x2) + 1):
            covered[(x, y1)] += 1
    else:
        if x1 < x2 and y1 < y2:
            for i in range(x2 - x1 + 1):
                covered[(x1 + i, y1 + i)] += 1
        elif x1 < x2 and y1 > y2:
            for i in range(abs(x1 - x2) + 1):
                covered[(x1 + i, y1 - i)] += 1
        elif x1 > x2 and y1 < y2:
            for i in range(abs(x1 - x2) + 1):
                covered[(x1 - i, y1 + i)] += 1
        else:
            for i in range(abs(x1 - x2) + 1):
                covered[(x1 - i, y1 - i)] += 1


print(sum(1 for x in covered.values() if x > 1))
