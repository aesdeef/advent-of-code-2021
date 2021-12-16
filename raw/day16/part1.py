import re
from collections import Counter, defaultdict, deque
from itertools import chain, count

# READ THE ENTIRE DESCRIPTION FIRST

INPUT_FILE = "../../input/16.txt"
# INPUT_FILE = "test.txt"


def to_bin(x):
    b = bin(int(x, 16)).removeprefix("0b")
    padding = "0" * (4 - len(b))
    return padding + b


with open(INPUT_FILE) as f:
    data = "".join(to_bin(x) for x in f.readline().strip()).rstrip("0")

print(data)


def parse(data):
    version_sum = 0
    while data:
        version, data = int(data[:3], 2), data[3:]
        version_sum += version
        typeid, data = int(data[:3], 2), data[3:]
        print(version, typeid)
        if typeid == 4:
            bitgroup_len = 0
            while True:
                bitgroup, data = data[:5], data[5:]
                if bitgroup[0] == "0":
                    break
        else:
            i, data = data[0], data[1:]
            if i == "0":
                total_len, data = int(data[:15], 2), data[15:]
                sub, data = data[:total_len], data[total_len:]
                version_sum += parse(sub)
            else:
                no_of_subpackets, data = int(data[:11], 2), data[11:]
                sub, data = data, []
                version_sum += parse(sub)

    return version_sum


print(parse(data))
