def test_coords():
    coords = set()

    with open("./help.txt") as f:
        for line in f:
            for c in line.split():
                x, y = c.split(",")
                coords.add((int(x), int(y)))

    return coords
