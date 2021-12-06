import re
from collections import Counter

INPUT_FILE = "../../input/06.txt"

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


data = [int(x) for x in lines[0].split(",")]
days = 80
for day in range(days):
    new_data = []
    extras = []
    for thing in data:
        new_point = thing - 1
        if new_point == -1:
            new_data.append(6)
            extras.append(8)
        else:
            new_data.append(new_point)

    data = new_data + extras

print(len(data))

data = {key: val for key, val in Counter([int(x) for x in lines[0].split(",")]).items()}
print(data)
days = 256
for day in range(days):
    data = {(key - 1): val for key, val in data.items()}
    extras = data.get(-1, 0)
    data[6] = data.get(6, 0) + extras
    data[8] = extras
    data[-1] = 0


print(sum(data.values()))
