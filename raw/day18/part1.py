import re
from collections import Counter, defaultdict, deque
from functools import cache
from itertools import chain, count, product

# READ THE ENTIRE DESCRIPTION FIRST

INPUT_FILE = "../../input/18.txt"
# INPUT_FILE = "test.txt"

with open(INPUT_FILE) as f:
    numbers = [eval(line.strip()) for line in f]


def can_explode(number):
    line = str(number)
    open_ = 0
    for x in line:
        match x:
            case "[":
                open_ += 1
            case "]":
                open_ -= 1
            case _:
                continue
        if open_ > 4:
            return True
    return False


def can_split(number):
    return re.match(r".*\d\d.*", str(number))


def explode(number):
    line = str(number)
    open_ = 0
    index = -1
    for i, x in enumerate(line):
        match x:
            case "[":
                open_ += 1
            case "]":
                open_ -= 1
            case _:
                continue
        if open_ > 4:
            index = i
            break
    # print(number, index)

    if re.search(r"\d", line[:index]):
        before_left, left_number, after_left = re.match(
            r"(.*)((?<!\d)\d+)([^\d]*)", line[:index]
        ).groups()
    else:
        before_left = line[:index]
        left_number = ""
        after_left = ""
    # print("|".join((before_left, left_number, after_left)))

    expl1, expl2, rest = re.match(r"\[(\d+), (\d+)\](.*)", line[index:]).groups()

    if re.search(r"\d", rest):
        before_right, right_number, after_right = re.match(
            r"([^\d]*)(\d+)(.*)", rest
        ).groups()
    else:
        before_right = ""
        right_number = ""
        after_right = rest
    # print("|".join((before_right, right_number, after_right)))

    if left_number and right_number:
        middle = "0"
    else:
        middle = ""

    if left_number:
        left_number = str(int(left_number) + int(expl1))
    else:
        left_number = "0"

    if right_number:
        right_number = str(int(right_number) + int(expl2))
    else:
        right_number = "0"

    new_number = "".join(
        (
            before_left,
            left_number,
            after_left,
            middle,
            before_right,
            right_number,
            after_right,
        )
    )
    # print(new_number)
    return eval(new_number)


def split(number):
    line = str(number)
    m = re.search(r"\d{2,}", line)
    num = int(m.group(0))
    first = num // 2
    second = num - first
    new_pair = f"[{first}, {second}]"

    return eval(line[: m.start()] + new_pair + line[m.end() :])


def reduce(number):
    # print(number)
    if can_explode(number):
        return reduce(explode(number))
    elif can_split(number):
        return reduce(split(number))
    else:
        return number


def red(numbers):
    acc = numbers[0]
    for number in numbers[1:]:
        acc = reduce([acc, number])
    return reduce(acc)


final_number = red(numbers)
print(final_number)


def magnitude(number):
    if type(number) == int:
        return number
    return magnitude(number[0]) * 3 + magnitude(number[1]) * 2


print(magnitude(final_number))
