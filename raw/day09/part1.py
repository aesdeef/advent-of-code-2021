import re
from collections import Counter
from itertools import chain

INPUT_FILE = "../../input/09.txt"
# INPUT_FILE = "test.txt"

with open(INPUT_FILE) as f:
    data = [[x for x in line.strip()] for line in f]

heights = {
    (x, y): int(data[y][x]) for x in range(len(data[0])) for y in range(len(data))
}
all_points = set(heights.keys())

risk_level_sum = 0
low_points = set()
for y in range(len(data)):
    for x in range(len(data[0])):
        is_low = True
        for point in {
            # (x - 1, y - 1),
            (x - 1, y),
            # (x - 1, y + 1),
            (x, y - 1),
            (x, y + 1),
            # (x + 1, y - 1),
            (x + 1, y),
            # (x + 1, y + 1),
        } & all_points:
            if heights[point] <= heights[(x, y)]:
                is_low = False

        if is_low:
            low_points.add((x, y))
            risk_level_sum += 1 + heights[(x, y)]

print(risk_level_sum)

basins = []
for point in low_points:
    basin = set()
    surrounding = {
        point,
    }
    while surrounding:
        p = surrounding.pop()
        if heights[p] == 9:
            continue
        x, y = p
        surrounding.update(
            {
                # (x - 1, y - 1),
                (x - 1, y),
                # (x - 1, y + 1),
                (x, y - 1),
                (x, y + 1),
                # (x + 1, y - 1),
                (x + 1, y),
                # (x + 1, y + 1),
            }
            & all_points - basin
        )
        basin.add(p)
    basins.append(basin)

biggest = sorted([len(x) for x in basins])
print(biggest[-3] * biggest[-2] * biggest[-1])
