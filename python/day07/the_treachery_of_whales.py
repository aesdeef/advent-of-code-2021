from typing import Callable

INPUT_FILE = "../../input/07.txt"


def parse_input() -> list[int]:
    """
    Parses the input and returns a list of positions of crab submarines
    """
    with open(INPUT_FILE) as f:
        return [int(x) for x in f.read().split(",")]


def required_fuel(crabs: list[int], cost: Callable[[list[int], int], int]) -> int:
    """
    Calculates the minimum required fuel for crabs to move given a cost function
    """
    position_range = range(min(crabs), max(crabs) + 1)
    assert len(position_range) > 0
    return min(cost(crabs, target) for target in position_range)


def cost_part1(crabs: list[int], target: int) -> int:
    """
    Calculates the total fuel that would be required for all crabs to move to
    the given position if the assumption from part 1 was true
    """
    return sum(abs(target - crab) for crab in crabs)


def cost_part2(crabs: list[int], target: int) -> int:
    """
    Calculates the total fuel that is actually required for all crabs to move
    to the given position
    """
    distances = [abs(target - crab) for crab in crabs]
    return sum((distance * (distance + 1)) // 2 for distance in distances)


if __name__ == "__main__":
    crabs = parse_input()
    part1 = required_fuel(crabs, cost_part1)
    part2 = required_fuel(crabs, cost_part2)

    print(part1)
    print(part2)
