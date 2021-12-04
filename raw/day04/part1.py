with open("../../input/04.txt", "r") as f:
    draws = None
    current = []
    cards = []
    for line in f:
        line = line.strip()
        if draws is None:
            draws = [int(x) for x in line.split(",")]
            continue
        if line.strip() == "" and current:
            cards.append(current)
            current = []
            continue
        nums = [int(x) for x in line.split(" ") if x != ""]
        if nums:
            current.append(nums)
    cards.append(current)


def score(board, drawn, last):
    print(board)
    s = 0
    for line in board:
        print(set(line) - drawn)
        s += sum(set(line) - drawn)
    print(last)
    return s * last


def check(board, drawn, last):
    lines = (
        [set(line) for line in board]
        + [set(line[i] for line in board) for i in range(5)]
        # + [set(board[i][i] for i in range(len(board)))]
        # + [{board[0][4], board[1][3], board[2][2], board[3][1], board[4][0]}]
    )
    for line in lines:
        if len(line & drawn) == 5:
            print(board, drawn)
            return score(board, drawn, last)
    return False


won = False
for i, n in enumerate(draws, start=1):
    ds = set(draws[:i])
    if n == 24:
        print(check(cards[2], ds, 24))
    for board in cards:
        s = check(board, ds, n)
        if s is not False:
            won = True
            print(s)
            break
    if won:
        break


last = None
last_board = None
for i, n in enumerate(draws, start=1):
    ds = set(draws[:i])
    for board in cards:
        s = check(board, ds, n)
        if s is not False:
            cards.remove(board)
            print(len(cards))
            last = s
            last_board = board
print(last)
print(last_board, ds)
