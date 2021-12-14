import re
from collections import Counter
from itertools import chain, count

# READ THE ENTIRE DESCRIPTION FIRST

INPUT_FILE = "../../input/14.txt"
# INPUT_FILE = "test.txt"

with open(INPUT_FILE) as f:
    template = f.readline().strip()
    template = [x for x in template]
    f.readline()
    rules = dict()
    for line in f:
        fro, to = line.strip().split(" -> ")
        a, b = fro
        rules[(a, b)] = to

print(template)


def step(temp):
    ins = []
    for a, b in zip(temp[:-1], temp[1:]):
        ins += rules[(a, b)]
    return list(chain(*zip(temp, ins))) + [temp[-1]]


temp = template[:]
for _ in range(10):
    temp = step(temp)

c = Counter(temp)
print(c.most_common()[0][1] - c.most_common()[-1][1])

temp = template[:]
paired = list(zip(temp[:-1], temp[1:]))
pairs = Counter(paired)
last_pair = tuple(temp[-2:])
for _ in range(40):
    new_last_pair = []
    new_pairs = Counter()
    for pair, value in pairs.items():
        a, b = pair
        x = rules[(a, b)]
        if pair == last_pair:
            new_last_pair = (x, b)
        new_pairs[(a, x)] = new_pairs.get((a, x), 0) + value
        new_pairs[(x, b)] = new_pairs.get((x, b), 0) + value

    pairs = new_pairs
    last_pair = new_last_pair

c = Counter()
for pair, value in pairs.items():
    a, b = pair
    c[a] = c.get(a, 0) + value

c[last_pair[1]] = c.get(last_pair[1], 0) + 1

c = c.most_common()
print(c)
print((c[0][1] - c[-1][1]))
