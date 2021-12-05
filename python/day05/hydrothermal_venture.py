import re
from collections import Counter
from dataclasses import dataclass
from itertools import chain
from typing import Generator

INPUT_FILE = "../../input/05.txt"


@dataclass(frozen=True)
class Point:
    x: int
    y: int

    def step(self, step_x: int, step_y: int) -> "Point":
        """
        Returns a new Point a given number of steps away from self
        """
        return Point(self.x + step_x, self.y + step_y)


@dataclass
class Line:
    start: Point
    end: Point
    parser = re.compile(r"([0-9]+),([0-9]+) -> ([0-9]+),([0-9]+)")

    def __init__(self, line: str):
        match = Line.parser.match(line.strip())
        assert match is not None
        coordinates = [int(x) for x in match.groups()]
        self.start = Point(coordinates[0], coordinates[1])
        self.end = Point(coordinates[2], coordinates[3])

    def is_horizontal_or_vertical(self) -> bool:
        """
        Checks whether the line is horizontal or vertical
        """
        return self.start.x == self.end.x or self.start.y == self.end.y

    @property
    def delta_x(self) -> int:
        """
        Returns the difference of the x coordinates of the points defining the line
        """
        return self.end.x - self.start.x

    @property
    def delta_y(self) -> int:
        """
        Returns the difference of the y coordinates of the points defining the line
        """
        return self.end.y - self.start.y

    def points(self) -> Generator[Point, None, None]:
        """
        Returns a generator of all points lying on the line
        """
        step_x = 0 if self.delta_x == 0 else self.delta_x // abs(self.delta_x)
        step_y = 0 if self.delta_y == 0 else self.delta_y // abs(self.delta_y)
        current_point = self.start
        while True:
            yield current_point
            if current_point == self.end:
                break
            current_point = current_point.step(step_x, step_y)


def parse_input() -> list[Line]:
    """
    Parses the input and returns a list of Lines
    """
    with open(INPUT_FILE) as f:
        return [Line(line) for line in f]


def count_overlaps(lines: list[Line]) -> int:
    """
    Counts the number of points where at least two lines overlap
    """
    points = (line.points() for line in lines)
    counter = Counter(chain(*points))
    return sum(count > 1 for count in counter.values())


if __name__ == "__main__":
    lines = parse_input()
    horizontal_and_vertical_lines = [
        line for line in lines if line.is_horizontal_or_vertical()
    ]
    part1 = count_overlaps(horizontal_and_vertical_lines)
    part2 = count_overlaps(lines)

    print(part1)
    print(part2)
