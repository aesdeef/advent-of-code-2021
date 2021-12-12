from itertools import chain, count

INPUT_FILE = "../../input/11.txt"
STEPS = 100
HEIGHT = 10
WIDTH = 10

EnergyLevelGrid = list[list[int]]


def parse_input() -> EnergyLevelGrid:
    """
    Parses the input and returns an EnergyLevelGrid
    """
    with open(INPUT_FILE) as f:
        return [[int(x) for x in line.strip()] for line in f]


def neighbours(row_number: int, column_number: int) -> set[tuple[int, int]]:
    """
    Returns all the neighboring cells within the grid
    """
    output: set[tuple[int, int]] = set()
    for i in (-1, 0, 1):
        for j in (-1, 0, 1):
            if i == 0 and j == 0:
                continue
            new_row_number = row_number + i
            new_column_number = column_number + j
            if 0 <= new_row_number < HEIGHT and 0 <= new_column_number < WIDTH:
                output.add((new_row_number, new_column_number))
    return output


def step(energy_levels: EnergyLevelGrid) -> tuple[int, EnergyLevelGrid]:
    """
    Applies one step to the energy level grid and returns the number of flashes
    and the updated energy level grid
    """
    energy_levels = [[x + 1 for x in line] for line in energy_levels]
    flashed = [[False for _ in row] for row in energy_levels]
    still_flashing = True

    while still_flashing:
        still_flashing = False
        for (r, row) in enumerate(energy_levels):
            for (c, cell) in enumerate(row):
                if cell > 9 and not flashed[r][c]:
                    still_flashing = True
                    flashed[r][c] = True
                    for y, x in neighbours(r, c):
                        energy_levels[y][x] += 1

    flash_count = sum(chain(*flashed))
    energy_levels = [
        [level if level < 10 else 0 for level in row] for row in energy_levels
    ]

    return (flash_count, energy_levels)


def solve(energy_levels: EnergyLevelGrid) -> tuple[int, int]:
    """
    Applies the steps until conditions for both parts are fulfilled and returns
    the answers for both parts
    """
    part1 = 0
    part2 = 0
    synchronised = False

    for steps in count(1):
        flash_count, energy_levels = step(energy_levels)

        if steps <= 100:
            part1 += flash_count

        if flash_count == HEIGHT * WIDTH:
            synchronised = True
            part2 = steps

        if steps >= 100 and synchronised:
            break

    return (part1, part2)


if __name__ == "__main__":
    energy_levels = parse_input()
    part1, part2 = solve(energy_levels)

    print(part1)
    print(part2)
