import re
from collections import Counter, defaultdict, deque
from functools import cache
from itertools import (
    chain,
    combinations,
    combinations_with_replacement,
    count,
    cycle,
    permutations,
    product,
)

# READ THE ENTIRE DESCRIPTION FIRST

INPUT_FILE = "../../input/21.txt"
# INPUT_FILE = "test.txt"

with open(INPUT_FILE) as f:
    positions = []
    for line in f.read().splitlines():
        positions.append(int(line.split(": ")[-1]))


scores = (0, 0)

universe_counts = [Counter(), Counter()]
universes = Counter({((0, 0), tuple(positions), 0, 1): 1})


@cache
def next_turn(scores, positions, player_on_turn, turn):
    outcomes = Counter()
    for rolls, count in [(6, 7), (5, 6), (7, 6), (4, 3), (8, 3), (3, 1), (9, 1)]:
        new_pos = (positions[player_on_turn] + rolls) % 10 or 10
        if scores[player_on_turn] + new_pos >= 21:
            outcomes[(True, player_on_turn, turn)] += count
        else:
            scorelist = list(scores)
            scorelist[player_on_turn] += new_pos
            new_scores = tuple(scorelist)
            positionslist = list(positions)
            positionslist[player_on_turn] = new_pos
            new_positions = tuple(positionslist)
            outcomes[
                (False, (new_scores, new_positions, 1 - player_on_turn, turn + 1))
            ] += count
    return outcomes


while universes:
    u, cts = universes.popitem()
    del universes[u]
    outcomes = next_turn(*u)
    for k, v in outcomes.items():
        if k[0]:
            player = k[1]
            turn = k[2]
            universe_counts[player][turn] += v * cts
        else:
            universes[k[1]] += v * cts

print(list(sum(u.values()) for u in universe_counts))
