INPUT_FILE = "../../input/09.txt"

Point = tuple[int, int]
Heightmap = dict[Point, int]
Basin = set[Point]


def parse_input() -> Heightmap:
    """
    Parses the input and returns a Heightmap
    """
    with open(INPUT_FILE) as f:
        heights = [[int(x) for x in line.strip()] for line in f]

    heightmap: Heightmap = dict()
    for (y, row) in enumerate(heights):
        for (x, height) in enumerate(row):
            heightmap[(x, y)] = height

    return heightmap


def get_surrounding_points(heightmap: Heightmap, point: Point) -> set[Point]:
    """
    Returns a set of surrounding points within the heightmap
    """
    x, y = point
    return {
        (x - 1, y),
        (x, y - 1),
        (x, y + 1),
        (x + 1, y),
    } & heightmap.keys()


def get_surrounding_heights(heightmap: Heightmap, point: Point) -> set[int]:
    """
    Returns the heights of points surrounding the given point
    """
    surrounding_points = get_surrounding_points(heightmap, point)
    return {heightmap[point] for point in surrounding_points}


def get_low_points(heightmap: Heightmap) -> set[Point]:
    """
    Finds the low points on the heightmap
    """
    low_points: set[Point] = set()
    for point in heightmap:
        surrounding_heights = get_surrounding_heights(heightmap, point)
        if all(heightmap[point] < height for height in surrounding_heights):
            low_points.add(point)
    return low_points


def solve_part1(heightmap: Heightmap, low_points: set[Point]) -> int:
    """
    Calculates the sum of the risk levels of all low points
    """
    return sum(1 + heightmap[point] for point in low_points)


def get_basins(heightmap: Heightmap, low_points: set[Point]) -> list[Basin]:
    """
    Finds all basins on the heightmap
    """
    basins: list[Basin] = []
    for low_point in low_points:
        basin: Basin = set()
        points_to_consider = {low_point}
        while points_to_consider:
            point = points_to_consider.pop()

            if heightmap[point] == 9:
                continue

            surrounding_points = get_surrounding_points(heightmap, point)
            points_to_consider.update(surrounding_points - basin)
            basin.add(point)

        basins.append(basin)
    return basins


def solve_part2(heightmap: Heightmap, low_points: set[Point]) -> int:
    """
    Calculates the product of the sizes of the three largest basins
    """
    basins = get_basins(heightmap, low_points)
    basin_sizes = sorted((len(basin) for basin in basins), reverse=True)
    return basin_sizes[0] * basin_sizes[1] * basin_sizes[2]


if __name__ == "__main__":
    heightmap = parse_input()
    low_points = get_low_points(heightmap)
    part1 = solve_part1(heightmap, low_points)
    part2 = solve_part2(heightmap, low_points)

    print(part1)
    print(part2)
