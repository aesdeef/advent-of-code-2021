import re
from collections import Counter
from itertools import chain, count

# READ THE ENTIRE DESCRIPTION FIRST

INPUT_FILE = "../../input/13.txt"
# INPUT_FILE = "test.txt"

with open(INPUT_FILE) as f:
    pts, flds = f.read().split("\n\n")

points = set()
for line in pts.split("\n"):
    a, b = line.split(",")
    point = (int(a), int(b))
    points.add(point)

folds = []
for line in flds.split("\n"):
    if not line:
        break
    a, b = line.split("=")
    fold = (a[-1], int(b))
    folds.append(fold)


def apply_fold(pts, fold):
    axis, val = fold
    new_points = set()
    for point in pts:
        x, y = point
        if axis == "x":
            diff = abs(x - val)
            new_x = val - diff
            new_points.add((new_x, y))
        elif axis == "y":
            diff = abs(y - val)
            new_y = val - diff
            new_points.add((x, new_y))
    return new_points


part1 = len(apply_fold(points, folds[0]))
print(part1)

for fold in folds:
    points = apply_fold(points, fold)

height = max(y for _, y in points) + 1
width = max(x for x, _ in points) + 1

for y in range(height):
    for x in range(width):
        if (x, y) in points:
            print("#", end="")
        else:
            print(".", end="")
    print()

# READ THE ENTIRE DESCRIPTION FIRST
