from enum import Enum
from typing import Generator


class Command(Enum):
    FORWARD = "forward"
    DOWN = "down"
    UP = "up"

Instruction = tuple[Command, int]
InstructionGenerator = Generator[Instruction, None, None]

def parse_input() -> InstructionGenerator:
    """
    Parses the input and returns a generator of Instructions
    """
    with open("../input.txt", "r") as f:
        for line in f:
            command, value = line.strip().split()
            command = Command(command)
            value = int(value)
            yield (command, value)

def solve_part1(instructions: InstructionGenerator) -> int:
    """
    Processes the instructions according to rules stated in part 1 and returns
    the answer, i.e. the product of the horizontal position and the depth
    """
    horizontal = 0
    depth = 0

    for command, value in instructions:
        match command:
            case Command.FORWARD:
                horizontal += value
            case Command.DOWN:
                depth += value
            case Command.UP:
                depth -= value

    return horizontal * depth

def solve_part2(instructions: InstructionGenerator) -> int:
    """
    Processes the instructions according to rules stated in part 2 and returns
    the answer, i.e. the product of the horizontal position and the depth
    """
    aim = 0
    horizontal = 0
    depth = 0

    for command, value in instructions:
        match command:
            case Command.FORWARD:
                horizontal += value
                depth += aim * value
            case Command.DOWN:
                aim += value
            case Command.UP:
                aim -= value

    return horizontal * depth

if __name__ == "__main__":
   part1 = solve_part1(parse_input())
   part2 = solve_part2(parse_input())
   print(part1)
   print(part2)
