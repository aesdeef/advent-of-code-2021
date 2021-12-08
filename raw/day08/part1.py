import re
from collections import Counter
from itertools import chain

INPUT_FILE = "../../input/08.txt"

with open(INPUT_FILE) as f:
    input_ = f.read()
lines = [line.strip() for line in input_.split("\n")]

def magic(inp, out):
    numbers = inp + out
    ones = [x for x in numbers if len(x) == 2]
    sevens = [x for x in numbers if len(x) == 3]
    fours = [x for x in numbers if len(x) == 4]
    top = set()
    leftup_and_middle = set()
    right = set()
    if ones:
        right = set(ones[0])
    else:
        if sevens and fours:
            right = set(sevens[0]) & set(fours[0])
    if sevens and fours:
        top = set(sevens[0]) - set(fours[0])
        leftup_and_middle = set(fours[0]) - set(sevens[0])
    else:
        if sevens and ones:
            top = set(sevens[0]) - set(ones[0])
        if fours and ones:
            leftup_and_middle = set(fours[0]) - set(ones[0])

    assert leftup_and_middle
    assert right
    return sum(
        mult * digit
        for mult, digit
        in zip([1000, 100, 10, 1], [let_to_num(x, top, leftup_and_middle, right) for x in out])
    )




def let_to_num(x, top, leftup_and_middle, right):
    match len(x):
        case 2: return 1
        case 3: return 7
        case 4: return 4
        case 7: return 8
        case 5:
            if leftup_and_middle:
                if len(set(x) & leftup_and_middle) == 2: return 5
            if right:
                if len(set(x) & right) == 2: return 3
            return 2
        case 6:
            if len(set(x) & leftup_and_middle) == 1: return 0
            if len(set(x) & right) == 2: return 9
            return 6

part1 = 0
part2 = 0
for line in lines:
    if not line:
        continue
    inp, out = line.split(" | ")
    inp = ["".join(sorted(word)) for word in inp.split(" ")]
    out = ["".join(sorted(word)) for word in out.split(" ")]
    for x in out:
        if len(x) in (2, 3, 4, 7):
            part1 += 1
    print(out)
    part2 += magic(inp, out)


print(part1)
print(part2)
