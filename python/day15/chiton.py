from collections import defaultdict

INPUT_FILE = "../../input/15.txt"

Position = tuple[int, int]
Risk = int
RiskGrid = list[list[Risk]]


def parse_input() -> RiskGrid:
    """
    Parses the input and return a grid of risk levels
    """
    with open(INPUT_FILE) as f:
        return [[int(x) for x in line.strip()] for line in f]


def enlarge(grid: RiskGrid, factor: int) -> RiskGrid:
    """
    Enlarges the grid as described in part 2 by the given factor
    """
    HEIGHT = len(grid)
    WIDTH = len(grid[0])

    def risk(x: int, y: int):
        base_risk = grid[x % WIDTH][y % HEIGHT]
        increase = x // WIDTH + y // HEIGHT
        return (base_risk + increase) % 9 or 9

    return [[risk(x, y) for x in range(WIDTH * factor)] for y in range(HEIGHT * factor)]


def neighbours(position: Position, height: int, width: int) -> set[Position]:
    """
    Returns the neighbouring positions within the grid
    """
    x, y = position
    return {
        (new_x, new_y)
        for new_x, new_y in {
            (x - 1, y),
            (x + 1, y),
            (x, y - 1),
            (x, y + 1),
        }
        if 0 <= new_x < width and 0 <= new_y < height
    }


def lowest_total_risk(grid: RiskGrid) -> int:
    """
    Returns the lowest total risk for the given grid
    """
    HEIGHT = len(grid)
    WIDTH = len(grid[0])

    options: defaultdict[Risk, set[Position]] = defaultdict(set, {0: {(0, 0)}})
    lowest_risks: dict[Position, Risk] = {(0, 0): 0}
    bottom_right = (HEIGHT - 1, WIDTH - 1)

    while options:
        current_risk = min(options)
        position = options[current_risk].pop()
        if not options[current_risk]:
            del options[current_risk]

        for neighbour in neighbours(position, HEIGHT, WIDTH):
            x, y = neighbour
            new_risk = current_risk + grid[y][x]
            if neighbour not in lowest_risks or new_risk < lowest_risks[neighbour]:
                lowest_risks[neighbour] = new_risk
                options[new_risk].add(neighbour)

    return lowest_risks[bottom_right]


if __name__ == "__main__":
    grid = parse_input()
    part1 = lowest_total_risk(grid)
    large_grid = enlarge(grid, 5)
    part2 = lowest_total_risk(large_grid)

    print(part1)
    print(part2)
