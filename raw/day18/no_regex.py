import re
from collections import Counter, defaultdict, deque
from dataclasses import dataclass
from functools import cache
from itertools import chain, count, product

# READ THE ENTIRE DESCRIPTION FIRST

INPUT_FILE = "../../input/18.txt"
# INPUT_FILE = "test.txt"


class Number:
    def __init__(self, first, second):
        self.first = first
        self.second = second
        self.parent = None


class Leaf:
    def __init__(self, val):
        self.val = val
        self.parent = None


with open(INPUT_FILE) as f:
    numbers = [eval(line.strip()) for line in f]


def parse_number(number):
    if type(number) == int:
        return Leaf(number)
    first = parse_number(number[0])
    second = parse_number(number[1])
    this = Number(first, second)
    first.parent = this
    second.parent = this
    return this


numbers = [parse_number(number) for number in numbers]


def can_explode(number, depth=0):
    if type(number) == Leaf:
        return False
    if depth >= 4:
        return number
    return can_explode(number.first, depth + 1) or can_explode(number.second, depth + 1)


def leftmost(number):
    if type(number) == Leaf:
        return number
    return leftmost(number.first)


def rightmost(number):
    if type(number) == Leaf:
        return number
    return rightmost(number.second)


def find_left_number(number):
    if number.parent is None:
        return None
    if number == number.parent.second:
        return rightmost(number.parent.first)
    return find_left_number(number.parent)


def find_right_number(number):
    if number.parent is None:
        return None
    if number == number.parent.first:
        return leftmost(number.parent.second)
    return find_right_number(number.parent)


def explode(number):
    left_number = find_left_number(number)
    right_number = find_right_number(number)

    print(number)
    print(left_number)
    print(right_number)
    raise NotImplementedError


def can_split(number):
    if type(number) == Leaf:
        if number.val >= 10:
            return number
        return False
    return can_split(number.first) or can_split(number.second)


def split(number):
    first = number // 2
    second = number - first
    return Number(first, second)


def add(a, b):
    number = Number(a, b)
    a.parent = number
    b.parent = number

    while True:
        explodable = can_explode(number)
        splittable = can_split(number)
        if explodable:
            number = explode(number)
        elif splittable:
            number = split(number)
        else:
            break

    return number


acc = numbers[0]
for num in numbers[1:]:
    acc = add(acc, num)

print(acc)
