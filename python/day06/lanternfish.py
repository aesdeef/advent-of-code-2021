from collections import Counter

INPUT_FILE = "../../input/06.txt"

LanternfishCounter = dict[int, int]
"""
A counter of lanternfish due to create a new lanternfish in the number of days
specified by the key
"""


def parse_input() -> LanternfishCounter:
    """
    Parses the input and returns a LanternfishCounter
    """
    with open(INPUT_FILE) as f:
        numbers = [int(x) for x in f.readline().split(",")]
        return dict(Counter(numbers))


def counter_after_n_days(counter: LanternfishCounter, n: int) -> LanternfishCounter:
    """
    Returns a LanternfishCounter after the specified number of days from the
    given starting position
    """
    for _ in range(n):
        counter = {days - 1: count_ for days, count_ in counter.items() if days >= 0}
        new_counter = counter.get(-1, 0)
        counter[6] = counter.get(6, 0) + new_counter
        counter[8] = new_counter
        counter[-1] = 0
    return counter


def count_lanternfish(counter: LanternfishCounter) -> int:
    """
    Counts the number of all lanternfish
    """
    return sum(counter.values())


if __name__ == "__main__":
    counter = parse_input()
    after_80_days = counter_after_n_days(counter, 80)
    after_256_days = counter_after_n_days(after_80_days, 256 - 80)
    print(count_lanternfish(after_80_days))
    print(count_lanternfish(after_256_days))
