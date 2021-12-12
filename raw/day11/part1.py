import re
from collections import Counter
from itertools import chain, count

INPUT_FILE = "../../input/11.txt"
# INPUT_FILE = "test.txt"
STEPS = 100

with open(INPUT_FILE) as f:
    energy_levels = [[int(x) for x in line.strip()] for line in f]


flashes = 0


# step
for _ in range(STEPS):
    energy_levels = [[x + 1 for x in line] for line in energy_levels]

    flashed = [
        [False for l in range(len(energy_levels[0]))] for j in range(len(energy_levels))
    ]
    while True:
        new_flashed = [row[:] for row in flashed]
        for (y, row) in enumerate(energy_levels):
            for (x, cell) in enumerate(row):
                if energy_levels[y][x] >= 10 and not flashed[y][x]:
                    flashed[y][x] = True
                    flashes += 1
                    for a, b in {
                        (y - 1, x - 1),
                        (y - 1, x),
                        (y - 1, x + 1),
                        (y, x - 1),
                        (y, x + 1),
                        (y + 1, x - 1),
                        (y + 1, x),
                        (y + 1, x + 1),
                    }:
                        if 0 <= a < len(energy_levels) and 0 <= b < len(
                            energy_levels[0]
                        ):
                            energy_levels[a][b] += 1

        if new_flashed == flashed:
            break

    # flashes += sum(x > 10 for x in chain(*energy_levels))
    energy_levels = [[x if x < 10 else 0 for x in line] for line in energy_levels]

print(flashes)


with open(INPUT_FILE) as f:
    energy_levels = [[int(x) for x in line.strip()] for line in f]


# step
for steps in count(1):
    energy_levels = [[x + 1 for x in line] for line in energy_levels]

    flashed = [
        [False for l in range(len(energy_levels[0]))] for j in range(len(energy_levels))
    ]
    while True:
        old_flashed = [row[:] for row in flashed]
        for (y, row) in enumerate(energy_levels):
            for (x, cell) in enumerate(row):
                if energy_levels[y][x] >= 10 and not flashed[y][x]:
                    flashed[y][x] = True
                    flashes += 1
                    for a, b in {
                        (y - 1, x - 1),
                        (y - 1, x),
                        (y - 1, x + 1),
                        (y, x - 1),
                        (y, x + 1),
                        (y + 1, x - 1),
                        (y + 1, x),
                        (y + 1, x + 1),
                    }:
                        if 0 <= a < len(energy_levels) and 0 <= b < len(
                            energy_levels[0]
                        ):
                            energy_levels[a][b] += 1

        if old_flashed == flashed:
            break

    energy_levels = [[x if x < 10 else 0 for x in line] for line in energy_levels]
    if sum(sum(line) for line in energy_levels) == 0:
        print(steps)
        break
