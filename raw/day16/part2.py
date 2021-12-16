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


def parse(data):
    stack = []
    version_sum = 0
    # while data:
    version, data = int(data[:3], 2), data[3:]
    version_sum += version
    typeid, data = int(data[:3], 2), data[3:]
    stack.append(fun(typeid))
    if typeid == 4:
        bits = ""
        while True:
            bitgroup, data = data[:5], data[5:]
            bits += bitgroup[1:]
            if bitgroup[0] == "0":
                break
        stack.append(int(bits, 2))
    else:
        i, data = data[0], data[1:]
        if i == "0":
            total_len, data = int(data[:15], 2), data[15:]
            stop_when_data_len = len(data) - total_len
            while len(data) > stop_when_data_len:
                pack, data = parse(data)
                stack.append(pack)
        else:
            no_of_subpackets, data = int(data[:11], 2), data[11:]
            for _ in range(no_of_subpackets):
                pack, data = parse(data)
                stack.append(pack)

    return stack, data


def mult(args, prod=1):
    if not args:
        return prod
    return mult(args[:-1], prod * args[-1])


def gt(args):
    return args[0] > args[1]


def lt(args):
    return args[0] < args[1]


def eq(args):
    return args[0] == args[1]


def identity(args):
    return args[0]


def fun(typeid):
    match typeid:
        case 0:
            return sum
        case 1:
            return mult
        case 2:
            return min
        case 3:
            return max
        case 4:
            return identity
        case 5:
            return gt
        case 6:
            return lt
        case 7:
            return eq


stack, _ = parse(data)


def calc(stack):
    f, *rest = stack
    args = []
    for r in rest:
        if type(r) is list:
            args.append(calc(r))
        else:
            args.append(r)
    return f(args)


print(calc(stack))
