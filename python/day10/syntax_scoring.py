from enum import Enum, auto

INPUT_FILE = "../../input/10.txt"


class ErrorType(Enum):
    CORRUPTED = auto()
    INCOMPLETE = auto()


class InvalidCharacterError(ValueError):
    """
    Inappropriate character
    """


def parse_input() -> list[str]:
    """
    Parses the input and returns a list of lines
    """
    with open(INPUT_FILE) as f:
        return [line.strip() for line in f]


def analyse(line: str) -> tuple[ErrorType, str]:
    """
    Analyses the line and returns the error type and the character(s) required
    to calculate the score
    """
    open_characters: list[str] = []
    for character in line:
        if character in "([{<":
            open_characters += character
        else:
            last_open_character = open_characters.pop()
            if (last_open_character, character) not in {
                ("(", ")"),
                ("[", "]"),
                ("{", "}"),
                ("<", ">"),
            }:
                return (ErrorType.CORRUPTED, character)
    return (ErrorType.INCOMPLETE, "".join(open_characters[::-1]))


def score_corrupted(illegal_character: str) -> int:
    """
    Returns the score for the given corrupted line
    """
    match illegal_character:
        case ")":
            return 3
        case "]":
            return 57
        case "}":
            return 1197
        case ">":
            return 25137
        case _:
            raise InvalidCharacterError


def score_incomplete(remaining_open_characters: str) -> int:
    """
    Returns the score for the given incomplete line
    """
    score = 0
    for character in remaining_open_characters:
        score *= 5
        match character:
            case "(":
                score += 1
            case "[":
                score += 2
            case "{":
                score += 3
            case "<":
                score += 4
            case _:
                raise InvalidCharacterError
    return score


def solve(lines: list[str]) -> tuple[int, int]:
    """
    Calculates the scores for each line and returns the results for both parts
    """
    part1 = 0
    part2_line_scores: list[int] = []

    for line in lines:
        type, important_part = analyse(line)
        match type:
            case ErrorType.CORRUPTED:
                part1 += score_corrupted(important_part)
            case ErrorType.INCOMPLETE:
                part2_line_scores.append(score_incomplete(important_part))

    part2 = sorted(part2_line_scores)[len(part2_line_scores) // 2]

    return (part1, part2)


if __name__ == "__main__":
    lines = parse_input()
    part1, part2 = solve(lines)

    print(part1)
    print(part2)
