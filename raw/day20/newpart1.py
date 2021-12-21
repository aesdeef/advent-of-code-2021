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
    light_pixels = set()
    for y, row in enumerate(image):
        for x, cell in enumerate(row):
            if cell == "#":
                light_pixels.add((x, y))


def new_tile(light_pixels, x, y):
    key = ""
    for a in (-1, 0, 1):
        for b in (-1, 0, 1):
            key += "1" if (x + b, y + a) in light_pixels else "0"

    return 1 if algo[int(key, 2)] == "#" else 0


def double_new_tile(light_pixels, x, y):
    key = ""
    for a in (-1, 0, 1):
        for b in (-1, 0, 1):
            key += str(new_tile(light_pixels, x + b, y + a))

    return 1 if algo[int(key, 2)] == "#" else 0


def double_step(light_pixels):
    min_y = min(x[1] for x in light_pixels) - 1
    max_y = max(x[1] for x in light_pixels) + 1
    min_x = min(x[0] for x in light_pixels) - 1
    max_x = max(x[0] for x in light_pixels) + 1

    new_light_pixels = set()
    for y in range(min_y - 2, max_y + 3):
        for x in range(min_x - 2, max_x + 3):
            pixel = double_new_tile(light_pixels, x, y)
            if pixel == 1:
                new_light_pixels.add((x, y))
    return new_light_pixels


def print_pixels(light_pixels):
    min_y = min(x[1] for x in light_pixels) - 1
    max_y = max(x[1] for x in light_pixels) + 1
    min_x = min(x[0] for x in light_pixels) - 1
    max_x = max(x[0] for x in light_pixels) + 1
    for y in range(min_y, max_y + 1):
        row = ""
        for x in range(min_x, max_x + 1):
            if (x, y) in light_pixels:
                row += "#"
            else:
                row += "."
        print(row)


# print_pixels(light_pixels)
after_two = double_step(light_pixels)
print(len(after_two))
# print_pixels(after_two)
lp = after_two
for _ in range(24):
    lp = double_step(lp)

print(len(lp))
