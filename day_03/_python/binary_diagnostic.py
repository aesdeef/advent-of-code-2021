from collections import Counter
from typing import Callable, Iterable


def parse_input() -> list[str]:
    """
    Parses the data and returns a list of binary entries
    """
    with open("../input.txt", "r") as f:
        return [line.strip() for line in f]


def more_common_bit(bits: Iterable[str]) -> str:
    """
    Returns the more common bit or "1" if both are equally common
    """
    c = Counter(bits)
    return "1" if c["1"] >= c["0"] else "0"


def less_common_bit(bits: Iterable[str]) -> str:
    """
    Returns the less common bit or "0" if both are equally common
    """
    c = Counter(bits)
    return "0" if c["1"] >= c["0"] else "1"


def multiply_binary(first: str, second: str) -> int:
    """
    Parses two strings representing binary numbers and multiplies them
    """
    return int(first, 2) * int(second, 2)


def solve_part1(data: list[str]) -> int:
    """
    Finds the solution to part 1 (the power consumption of the submarine)
    """
    gamma = ""
    epsilon = ""

    for bits in zip(*data):
        gamma += more_common_bit(bits)
        epsilon += less_common_bit(bits)

    return multiply_binary(gamma, epsilon)


def find_rating(data: list[str], keep_condition: Callable[[list[str]], str]) -> str:
    """
    Finds the rating by going through each bit position and keeping only those
    entries where the ith bit matches the one returned by the keep_condition
    function
    """
    for i in range(len(data[0])):
        bits = [entry[i] for entry in data]
        data = [entry for entry in data if entry[i] == keep_condition(bits)]

        if len(data) == 1:
            return data[0]

    raise ValueError("could not find the rating")


def solve_part2(data: list[str]) -> int:
    """
    Finds the solution to part 2 (the life support rating of the submarine)
    """
    oxygen_generator_rating = find_rating(data, more_common_bit)
    co2_scrubber_rating = find_rating(data, less_common_bit)

    return multiply_binary(oxygen_generator_rating, co2_scrubber_rating)


if __name__ == "__main__":
    data = parse_input()
    part1 = solve_part1(data)
    part2 = solve_part2(data)
    print(part1)
    print(part2)
