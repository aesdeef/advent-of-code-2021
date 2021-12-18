import re
from functools import reduce
from itertools import permutations

INPUT_FILE = "../../input/18.txt"


def parse_input() -> list[str]:
    """
    Parses the input and returns a list of snailfish numbers
    """
    with open(INPUT_FILE) as f:
        return [line.strip() for line in f]


def pair(first: int | str, second: int | str) -> str:
    """
    Takes two numbers (regular or snailfish) and returns a snailfish number
    """
    return f"[{first},{second}]"


def find_explodable(number: str) -> re.Match[str] | None:
    """
    Finds the first pair nested inside four pairs and returns a Match object
    or None, if there are no such pairs
    """
    for match in re.finditer(r"(\[(?P<first>\d+),(?P<second>\d+)\])", number):
        before_match = number[: match.start()]
        if before_match.count("[") - before_match.count("]") >= 4:
            return match
    return None


def find_splittable(number: str) -> re.Match[str] | None:
    """
    Finds the first regular number that is 10 or greater and returns a Match
    object or None, if there are no such numbers
    """
    return re.search(r"\d{2,}", number)


def explode(number: str, explodable: re.Match[str]) -> str:
    """
    Explodes the explodable pair
    """
    exploded_first = int(explodable["first"])
    exploded_second = int(explodable["second"])

    before, after = number[: explodable.start()], number[explodable.end() :]

    if m_left := re.fullmatch(
        r"(?P<before_left>.*)(?P<left>(?<!\d)\d+)(?P<after_left>[^\d]*)", before
    ):
        new_left = int(m_left["left"]) + exploded_first
        before = f"{m_left['before_left']}{new_left}{m_left['after_left']}"

    if m_right := re.fullmatch(
        r"(?P<before_right>[^\d]*)(?P<right>\d+)(?P<after_right>.*)", after
    ):
        new_right = int(m_right["right"]) + exploded_second
        after = f"{m_right['before_right']}{new_right}{m_right['after_right']}"

    return before + "0" + after


def split(number: str, splittable: re.Match[str]) -> str:
    """
    Splits the splittable number
    """
    splittable_number = int(splittable.group(0))
    first = splittable_number // 2
    second = splittable_number - first
    return (
        number[: splittable.start()] + pair(first, second) + number[splittable.end() :]
    )


def add(first: str, second: str) -> str:
    """
    Adds two snailfish numbers
    """
    number = pair(first, second)
    while True:
        if explodable := find_explodable(number):
            number = explode(number, explodable)
        elif splittable := find_splittable(number):
            number = split(number, splittable)
        else:
            return number


def magnitude(number: str) -> int:
    """
    Returns the magnitude of the snailfish number
    """
    while m := re.search(r"(\[(?P<first>\d+),(?P<second>\d+)\])", number):
        number = (
            number[: m.start()]
            + str(3 * int(m["first"]) + 2 * int(m["second"]))
            + number[m.end() :]
        )
    return int(number)


def solve_part1(numbers: list[str]) -> int:
    """
    Finds the solution for part 1
    """
    return magnitude(reduce(add, numbers))


def solve_part2(numbers: list[str]) -> int:
    """
    Finds the solution for part 2
    """
    return max(magnitude(add(a, b)) for a, b in permutations(numbers, 2))


if __name__ == "__main__":
    numbers = parse_input()
    part1 = solve_part1(numbers)
    part2 = solve_part2(numbers)

    print(part1)
    print(part2)
