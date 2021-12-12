import re
from collections import Counter
from itertools import chain, count

INPUT_FILE = "../../input/12.txt"
# INPUT_FILE = "test.txt"

with open(INPUT_FILE) as f:
    data = [line.strip().split("-") for line in f]


class Node:
    all_nodes = {}

    def __init__(self, name):
        self.name = name
        self.neighbours = set()

    def __repr__(self):
        return self.name


for node, nei in data:
    if node in Node.all_nodes:
        n = Node.all_nodes[node]
    else:
        n = Node(node)
        Node.all_nodes[node] = n

    if nei in Node.all_nodes:
        nein = Node.all_nodes[nei]
    else:
        nein = Node(nei)
        Node.all_nodes[nei] = nein

    n.neighbours.add(nein)
    nein.neighbours.add(n)


stack = [(Node.all_nodes["start"], ())]
paths = set()

while stack:
    x, path = stack.pop()
    path = path + (x,)
    for nei in x.neighbours:
        if nei.name == "end":
            path = path + (nei,)
            paths.add(path)
        elif nei.name.islower() and nei in path:
            continue
        else:
            stack.append((nei, path))

# [print(path) for path in paths]
print(len(paths))
