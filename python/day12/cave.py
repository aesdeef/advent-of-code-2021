from dataclasses import dataclass


@dataclass
class Cave:
    """
    A single cave aware of its neighbours
    """

    name: str
    neighbours: list["Cave"]

    def __init__(self, name: str):
        self.name = name
        self.neighbours = []

    def add_neighbour(self, cave: "Cave"):
        """
        Adds the given cave to the list of neighbours
        """
        self.neighbours.append(cave)

    @property
    def is_start(self) -> bool:
        return self.name == "start"

    @property
    def is_end(self) -> bool:
        return self.name == "end"

    @property
    def is_small(self) -> bool:
        return self.name.islower()
