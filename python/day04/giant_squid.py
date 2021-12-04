from itertools import chain

INPUT_FILE = "../../input/04.txt"

Board = list[list[int]]
Prediction = tuple[int, int]


def parse_block(block: str) -> Board:
    """
    Parses a block of 5 lines (passed as a single string with '\n's) and returns
    a list of 5 rows, where each row is a list of 5 numbers
    """
    return [[int(x) for x in line.split()] for line in block.split("\n")]


def parse_input() -> tuple[list[int], list[Board]]:
    """
    Parses the input and returns a list of numbers that were drawn and a list
    of Boards
    """
    with open(INPUT_FILE) as f:
        first, *rest = f.read().strip().split("\n\n")

    draws = [int(x) for x in first.split(",")]
    boards = [parse_block(block) for block in rest]

    return (draws, boards)


def board_lines(board: Board) -> list[set[int]]:
    """
    Returns a list of all lines (rows and columns) on a given board
    """
    return [set(row) for row in board] + [set(column) for column in zip(*board)]


def get_score(board: Board, draws_until_win: list[int]) -> int:
    """
    Calculates the score of the board at the moment one of the lines is completed
    """
    remaining_numbers = set(chain(*board)) - set(draws_until_win)
    return sum(remaining_numbers) * draws_until_win[-1]


def predicted_win(board: Board, draws: list[int]) -> Prediction:
    """
    Goes through the drawn numbers and returns a Prediction, which is a tuple of
    two numbers:
    - the turn on which the board wins
    - the score of the board at that moment
    """
    lines = board_lines(board)
    for i, draw in enumerate(draws):
        for line in lines:
            if draw in line:
                line.remove(draw)
        if not all(lines):
            score = get_score(board, draws[: i + 1])
            return (i, score)

    raise ValueError


def get_predictions(boards: list[Board], draws: list[int]) -> list[Prediction]:
    """
    Analyses the boards one by one and returns the Predictions sorted by the
    turn on which the board wins
    """
    predictions = [predicted_win(board, draws) for board in boards]
    return sorted(predictions)


if __name__ == "__main__":
    draws, boards = parse_input()
    predictions = get_predictions(boards, draws)
    part1 = predictions[0][1]
    part2 = predictions[-1][1]
    print(part1)
    print(part2)
