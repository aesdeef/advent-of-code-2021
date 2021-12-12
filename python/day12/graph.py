from dataclasses import dataclass

from cave import Cave

Link = list[str]


@dataclass
class Graph:
    """
    A graph of all caves and the connections between them
    """

    caves: dict[str, Cave]

    def __init__(self, links: list[Link]):
        self.caves = {}
        for link in links:
            self.add_link(link)

    def get(self, cave_name: str) -> Cave:
        """
        Finds a cave with the given name or creates one if it doesn't exist
        """
        if cave_name in self.caves:
            return self.caves[cave_name]

        new_cave = Cave(cave_name)
        self.caves[cave_name] = new_cave
        return new_cave

    def add_link(self, link: list[str]):
        """
        Adds the given link to the graph
        """
        cave1 = self.get(link[0])
        cave2 = self.get(link[1])
        cave1.add_neighbour(cave2)
        cave2.add_neighbour(cave1)
