from itertools import chain

INPUT_FILE = "../../input/08.txt"

Entry = tuple[set[str], list[str]]


def standardise_signal_pattern(signal_pattern: str) -> str:
    """
    Sorts the letters in the given signal pattern alphabetically
    """
    return "".join(sorted(signal_pattern))


def parse_puzzle_input() -> list[Entry]:
    """
    Parses the puzzle input and returns a list of entries
    """
    entries: list[Entry] = []
    with open(INPUT_FILE) as f:
        for line in f:
            parts = [part.split() for part in line.split(" | ")]
            input_ = {standardise_signal_pattern(pattern) for pattern in parts[0]}
            output = [standardise_signal_pattern(pattern) for pattern in parts[1]]
            entries.append((input_, output))
    return entries


def understand_input(input_: set[str]) -> dict[str, int]:
    """
    Figures out which signal pattern corresponds to which digit
    """
    digits: dict[str, int] = {}
    five_segments: set[str] = set()
    six_segments: set[str] = set()
    one = ""
    four = ""

    for digit in input_:
        match len(digit):
            case 2:
                one = digit
                digits[digit] = 1
            case 3:
                digits[digit] = 7
            case 4:
                four = digit
                digits[digit] = 4
            case 5:
                five_segments.add(digit)
            case 6:
                six_segments.add(digit)
            case 7:
                digits[digit] = 8

    for digit in five_segments:
        if len(set(digit) & set(one)) == 2:
            digits[digit] = 3
        elif len(set(digit) & (set(four) - set(one))) == 2:
            digits[digit] = 5
        else:
            digits[digit] = 2

    for digit in six_segments:
        if len(set(digit) & (set(four) - set(one))) == 1:
            digits[digit] = 0
        elif len(set(digit) & set(one)) == 2:
            digits[digit] = 9
        else:
            digits[digit] = 6

    return digits


def parse_output(entry: Entry) -> list[int]:
    """
    Returns a list of digits corresponding to the output signal patterns
    """
    input_, output = entry
    digit_parser = understand_input(input_)
    return [digit_parser[digit] for digit in output]


def solve_part1(outputs: list[list[int]]) -> int:
    """
    Counts the number of digits 1, 4, 7, and 8 in the outputs
    """
    return sum(digit in (1, 4, 7, 8) for digit in chain(*outputs))


def solve_part2(outputs: list[list[int]]) -> int:
    """
    Sums the numbers represented in the outputs
    """
    numbers = [int("".join(str(digit) for digit in number)) for number in outputs]
    return sum(numbers)


if __name__ == "__main__":
    entries = parse_puzzle_input()
    outputs = [parse_output(entry) for entry in entries]
    part1 = solve_part1(outputs)
    part2 = solve_part2(outputs)

    print(part1)
    print(part2)
