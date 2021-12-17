from dataclasses import dataclass
from enum import Enum
from math import prod

INPUT_FILE = "../../input/16.txt"


class Operation(Enum):
    SUM = 0
    PRODUCT = 1
    MINIMUM = 2
    MAXIMUM = 3
    GREATER_THAN = 5
    LESS_THAN = 6
    EQUAL = 7


Bits = str


@dataclass(frozen=True)
class Packet:
    version: int


@dataclass(frozen=True)
class LiteralValue(Packet):
    value: int


@dataclass(frozen=True)
class Operator(Packet):
    operation: Operation
    subpackets: list[Packet]


def hex_to_bin(char: str) -> Bits:
    """
    Takes a hex digit and returns a 4-digit binary representation
    """
    b = bin(int(char, 16)).removeprefix("0b")
    padding = "0" * (4 - len(b))
    return padding + b


def parse_input() -> Bits:
    """
    Parses the input and returns a string of bits with trailing 0s removed
    """
    with open(INPUT_FILE) as f:
        return "".join(hex_to_bin(char) for char in f.readline().strip()).rstrip("0")


def read_packets(data: Bits) -> tuple[Packet, Bits]:
    """
    Parses the bits and returns the first packet it finds and the remaining bits
    (so that it can be used recursively)
    """
    version, type_id, data = int(data[:3], 2), int(data[3:6], 2), data[6:]

    if type_id == 4:
        number_bits = ""
        while True:
            group, data = data[:5], data[5:]
            number_bits += group[1:]
            if group[0] == "0":
                break
        return LiteralValue(version, int(number_bits, 2)), data

    length_type, data = data[0], data[1:]
    args: list[Packet] = []

    match length_type:
        case "0":
            data_length, data = int(data[:15], 2), data[15:]
            subpacket_data, data = data[:data_length], data[data_length:]
            while subpacket_data:
                packet, subpacket_data = read_packets(subpacket_data)
                args.append(packet)

        case "1":
            subpacket_count, data = int(data[:11], 2), data[11:]
            for _ in range(subpacket_count):
                packet, data = read_packets(data)
                args.append(packet)

    operator = Operation(type_id)
    return Operator(version, operator, args), data


def evaluate(packet: Packet) -> LiteralValue:
    """
    Applies all operators in the packet and returns a LiteralValue, where the
    version is the sum of all versions of (sub)packets composing the given
    packet, and the value is the result of the operations
    """
    match packet:
        case LiteralValue():
            return packet
        case Operator():
            literal_values = [evaluate(subpacket) for subpacket in packet.subpackets]
            versions = [lv.version for lv in literal_values]
            values = [lv.value for lv in literal_values]
            version_sum = packet.version + sum(versions)
            return LiteralValue(version_sum, apply_operator(packet.operation, values))
        case _:
            raise ValueError


def apply_operator(operation: Operation, args: list[int]) -> int:
    """
    Applies the correct operation to the arguments
    """
    match operation:
        case Operation.SUM:
            return sum(args)
        case Operation.PRODUCT:
            return prod(args)
        case Operation.MINIMUM:
            return min(args)
        case Operation.MAXIMUM:
            return max(args)
        case Operation.GREATER_THAN:
            return args[0] > args[1]
        case Operation.LESS_THAN:
            return args[0] < args[1]
        case Operation.EQUAL:
            return args[0] == args[1]
        case _:
            raise ValueError


if __name__ == "__main__":
    data = parse_input()
    packet, _ = read_packets(data)
    literal_value = evaluate(packet)
    part1 = literal_value.version
    part2 = literal_value.value

    print(part1)
    print(part2)
