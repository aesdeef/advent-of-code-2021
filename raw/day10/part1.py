import re
from collections import Counter
from itertools import chain

INPUT_FILE = "../../input/10.txt"
# INPUT_FILE = "test.txt"

with open(INPUT_FILE) as f:
    data = [line.strip() for line in f]

score = 0
score_extra = []
for line in data:
    open = []
    incomplete = True
    for ch in line:
        if ch in "<([{":
            open.append(ch)
        elif ch in ">)]}":
            last_open = open.pop()
            if (last_open, ch) in (
                ("{", "}"),
                ("[", "]"),
                ("(", ")"),
                ("<", ">"),
            ):
                continue
            else:
                incomplete = False
                match ch:
                    case ")":
                        score += 3
                    case "]":
                        score += 57
                    case "}":
                        score += 1197
                    case ">":
                        score += 25137
                break

        else:
            print(line)
            print(open)
            raise Exception

    if incomplete:
        score_part = 0
        for ch in open[::-1]:
            score_part *= 5
            match ch:
                case "(":
                    score_part += 1
                case "[":
                    score_part += 2
                case "{":
                    score_part += 3
                case "<":
                    score_part += 4
        score_extra.append(score_part)

score_extra = sorted(score_extra)
print(score_extra, len(score_extra), len(score_extra) // 2)
score_extra = score_extra[len(score_extra) // 2]
print(score_extra)


print(score)
print(score_extra)
