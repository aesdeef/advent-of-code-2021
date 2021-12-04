INPUT_FILE = "../../input/01.txt"


def parse_input() -> list[int]:
    """
    Parses the input and returns a list of depth measurements.
    """
    with open(INPUT_FILE, "r") as f:
        return [int(line) for line in f]


def count_increases(measurements: list[int]) -> int:
    """
    Counts the number of times a measurement increases from the previous measurement.
    """
    return sum(1 for a, b in zip(measurements[:-1], measurements[1:]) if a < b)


def get_sliding_windows(depths: list[int]) -> list[int]:
    """
    Calculates the three-measurement sliding windows.
    """
    return [a + b + c for a, b, c in zip(depths[:-2], depths[1:-1], depths[2:])]


if __name__ == "__main__":
    depths = parse_input()
    part1 = count_increases(depths)
    sliding_windows = get_sliding_windows(depths)
    part2 = count_increases(sliding_windows)

    print(part1)
    print(part2)
