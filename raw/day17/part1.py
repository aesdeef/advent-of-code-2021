import re
from collections import Counter, defaultdict, deque
from functools import cache
from itertools import chain, count, product

from help import test_coords

# READ THE ENTIRE DESCRIPTION FIRST

INPUT_FILE = "../../input/17.txt"
# INPUT_FILE = "test.txt"

with open(INPUT_FILE) as f:
    target_x_min, target_x_max, target_y_min, target_y_max = [
        int(x)
        for x in re.match(
            r"target area: x=(\d*)..(\d*), y=(-?\d*)..(-?\d*)", f.readline()
        ).groups()
    ]


def step_x(x_vel):
    total = 0
    xs = []
    for x_v in range(x_vel, -1, -1):
        total += x_v
        xs.append(total)
    return xs


def step_y(y_vel, target_y_min):
    total = 0
    ys = []
    for i in count():
        total += y_vel - i
        ys.append(total)
        if total < target_y_min:
            break
    return ys


def step(x_vel, y_vel):
    total_x = 0
    total_y = 0
    for i in count():
        total_x += max(x_vel - i, 0)
        total_y += y_vel - i
        yield (total_x, total_y)


possible_x = []
most_steps = -1
for x_ in range(target_x_max + 1):
    steps = step_x(x_)
    if any(target_x_min <= step <= target_x_max for step in steps):
        possible_x.append(x_)
        m_s = max(
            i + 1 for i in range(len(steps)) if target_x_min <= steps[i] <= target_x_max
        )
        most_steps = max(m_s, most_steps)

possible_minus_y = []
for y_ in range(target_y_min, 1):
    steps = step_y(y_, target_y_min)
    # print(y_, steps)
    if any(target_y_min <= step <= target_y_min for step in steps):
        possible_minus_y.append(y_)

hi_y = -min(possible_minus_y) - 1
ans = (hi_y * (hi_y + 1)) // 2

print(ans)


@cache
def x_on_step(x_vel, min_x, max_x):
    total = 0
    steps = set()
    for i in range(1000):
        total += max(x_vel - i, 0)
        if min_x <= total <= max_x:
            steps.add(i)
    return steps


@cache
def y_on_step(y_vel, min_y, max_y):
    total = 0
    steps = set()
    for i in range(1000):
        total += y_vel - i
        if min_y <= total <= max_y:
            steps.add(i)
    return steps


possible_y = set(range(min(possible_minus_y) - 20, -min(possible_minus_y) + 21))
possible_count = 0
possible_coords = set()
for x, y in product(possible_x, possible_y):
    xs = x_on_step(x, target_x_min, target_x_max)
    ys = y_on_step(y, target_y_min, target_y_max)
    if xs & ys:
        possible_count += 1
        possible_coords.add((x, y))

# print(test_coords() - possible_coords)
# print(possible_coords - test_coords())
print(possible_count)
