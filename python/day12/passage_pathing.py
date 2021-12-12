from collections import Counter, deque

from cave import Cave
from graph import Graph

INPUT_FILE = "../../input/12.txt"

Path = list[Cave]
PathCandidate = tuple[Cave, Path]


def parse_input() -> Graph:
    """
    Parses the input and returns a Graph
    """
    with open(INPUT_FILE) as f:
        links = [line.strip().split("-") for line in f]

    return Graph(links)


def visited_a_small_cave_twice(path: Path) -> bool:
    """
    Checks if you've already visited a small cave twice
    """
    c = Counter(cave.name for cave in path if cave.is_small)
    return any(value > 1 for value in c.values())


def can_visit(cave: Cave, path: Path, part: int) -> bool:
    """
    Checks if you can visit the cave
    """
    if not cave.is_small:
        return True

    if cave.is_start:
        return False

    if cave in path:
        return not visited_a_small_cave_twice(path) if part == 2 else False

    return True


def count_paths(graph: Graph, part: int) -> int:
    """
    Counts all possible paths from start to end
    """
    candidates: deque[PathCandidate] = deque([(graph.get("start"), [])])
    path_count = 0

    while candidates:
        current_node, path = candidates.popleft()
        path = path[:] + [current_node]

        for neighbour in current_node.neighbours:
            if neighbour.is_end:
                path_count += 1

            elif can_visit(neighbour, path, part):
                candidates.append((neighbour, path))

    return path_count


if __name__ == "__main__":
    graph = parse_input()
    part1 = count_paths(graph, part=1)
    part2 = count_paths(graph, part=2)

    print(part1)
    print(part2)
