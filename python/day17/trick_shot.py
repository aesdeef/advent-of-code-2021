import re
from functools import cache
from itertools import count

INPUT_FILE = "../../input/17.txt"

Target = tuple[int, int, int, int]
Velocity = tuple[int, int]
Position = tuple[int, int]
Path = list[Position]


def parse_input() -> Target:
    """
    Parses the input and returns the target boundaries
    """
    with open(INPUT_FILE) as f:
        min_x, max_x, min_y, max_y = re.findall(r"-?\d+", f.readline())
    return (int(min_x), int(max_x), int(min_y), int(max_y))


@cache
def get_path(target: Target, velocity: Velocity) -> Path:
    """
    Computes the path up to the moment the probe goes beyond the target in
    either dimension
    """
    _, max_x, min_y, _ = target
    velocity_x, velocity_y = velocity
    path: Path = [(0, 0)]
    x = 0
    y = 0
    for step in count():
        x += max(velocity_x - step, 0)
        y += velocity_y - step
        path.append((x, y))
        if x >= max_x or y <= min_y:
            break
    return path


def in_target(target: Target, position: Position) -> bool:
    """
    Checks if the position is within the target
    """
    x, y = position
    min_x, max_x, min_y, max_y = target
    return min_x <= x <= max_x and min_y <= y <= max_y


def solve(target: Target) -> tuple[int, int]:
    """
    Evaluates all reasonable starting velocities and counts the number of
    possible starting velocities (for part 2) and the highest y coordinate
    reached from these velocities (for part 1)
    """
    possible_velocities_count = 0
    highest_y_overall = -1
    _, max_x, min_y, _ = target

    for velocity_x in range(max_x + 1):
        for velocity_y in range(min_y, -min_y):
            velocity = (velocity_x, velocity_y)
            path = get_path(target, velocity)
            if any(in_target(target, position) for position in path):
                possible_velocities_count += 1
                highest_y = max(position[1] for position in path)
                highest_y_overall = max(highest_y_overall, highest_y)

    return highest_y_overall, possible_velocities_count


if __name__ == "__main__":
    target = parse_input()
    part1, part2 = solve(target)

    print(part1)
    print(part2)
