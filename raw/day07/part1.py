import re
from collections import Counter
from itertools import chain

INPUT_FILE = "../../input/07.txt"

# pre-written code starts here
def intify(line: list[str]):
    return [int(x) if re.match(r"^[+-]?\d+$", x) else x for x in line]


with open(INPUT_FILE) as f:
    input_ = f.read()

blocks = [block.split("\n") for block in input_.split("\n\n")]
lines = [line.strip() for line in input_.split("\n")]
wordlines = [line.split() for line in lines]
nums = intify(lines)
alphanums = [re.findall(r"[\w+-]+", line) for line in lines]
renums = [intify(line) for line in alphanums]
# pre-written code ends here
crabs = [int(x) for x in lines[0].split(",")]

best_pos = -1
best_fuel = 10000000000000
for pos in range(min(crabs), max(crabs) + 1):
    fuel = sum([abs(x - pos) for x in crabs])
    if fuel < best_fuel:
        best_fuel = fuel
        best_pos = pos

print(best_pos, best_fuel)


best_pos = -1
best_fuel = 10000000000000
for pos in range(min(crabs), max(crabs) + 1):
    fuel = sum([abs(x - pos) * (abs(x - pos) + 1) / 2 for x in crabs])
    if fuel < best_fuel:
        best_fuel = fuel
        best_pos = pos

print(best_pos, best_fuel)
