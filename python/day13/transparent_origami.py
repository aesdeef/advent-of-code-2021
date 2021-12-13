INPUT_FILE = "../../input/13.txt"

Point = tuple[int, int]
Fold = tuple[str, int]


def parse_input() -> tuple[set[Point], list[Fold]]:
    """
    Parses the input and returns a set of points and a list of folding instructions
    """
    with open(INPUT_FILE) as f:
        blocks = f.read().split("\n\n")
        point_lines, fold_lines = (block.splitlines() for block in blocks)

    points: set[Point] = set()
    for line in point_lines:
        x, y = line.split(",")
        points.add((int(x), int(y)))

    folds: list[Fold] = []
    for line in fold_lines:
        axis, value = line.removeprefix("fold along ").split("=")
        folds.append((axis, int(value)))

    return (points, folds)


def apply_fold(points: set[Point], fold: Fold) -> set[Point]:
    """
    Folds the paper and returns a set of points that are visible
    """
    axis, value = fold
    new_points: set[Point] = set()
    for point in points:
        x, y = point
        if axis == "x":
            distance_from_line = abs(x - value)
            new_x = value - distance_from_line
            new_points.add((new_x, y))
        elif axis == "y":
            distance_from_line = abs(y - value)
            new_y = value - distance_from_line
            new_points.add((x, new_y))
    return new_points


def solve_part1(points: set[Point], fold: Fold) -> int:
    """
    Counts the number of points that remain visible after the fold
    """
    return len(apply_fold(points, fold))


def solve_part2(points: set[Point], folds: list[Fold]) -> str:
    """
    Applies all folds to the given points and returns a multi-line string
    that reveals the eight-letter code when printed
    """
    for fold in folds:
        points = apply_fold(points, fold)

    height = max(y for _, y in points) + 1
    width = max(x for x, _ in points) + 1

    output: list[str] = []
    for y in range(height):
        row = "".join("#" if (x, y) in points else "." for x in range(width))
        output.append(row)

    return "\n".join(output)


if __name__ == "__main__":
    points, folds = parse_input()
    part1 = solve_part1(points, folds[0])
    part2 = solve_part2(points, folds)

    print(part1)
    print(part2)
