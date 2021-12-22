from io import StringIO


class Packet:

    def __init__(self, version, type_id, literal_value=None, children=None):
        self.version = version
        self.type_id = type_id
        self.literal_value = literal_value
        self.children = children or []

    def __eq__(self, other):
        return isinstance(other,
                          Packet) and self.version == other.version and self.type_id == other.type_id and self.children == other.children


def hex_to_bin(hex_string):
    hex_to_bin = {"0": "0000",
                  "1": "0001",
                  "2": "0010",
                  "3": "0011",
                  "4": "0100",
                  "5": "0101",
                  "6": "0110",
                  "7": "0111",
                  "8": "1000",
                  "9": "1001",
                  "A": "1010",
                  "B": "1011",
                  "C": "1100",
                  "D": "1101",
                  "E": "1110",
                  "F": "1111"}
    bits = []
    for hex_val in hex_string:
        bits.append(hex_to_bin[hex_val])

    return ''.join(bits)


def parse_literal(binary_str: StringIO) -> int:
    literal = 0
    while True:
        first_bit = int(binary_str.read(1), 2)
        # shifting left and then ORing with the next 4 bits is like appending
        # the string values to the end of a string
        literal = (literal << 4) | int(binary_str.read(4), 2)

        if first_bit == 0:
            break

    return literal


def parse_packet(binary_str: StringIO) -> Packet:
    version = int(binary_str.read(3), 2)
    type_id = int(binary_str.read(3), 2)

    if type_id == 4:
        literal_value = parse_literal(binary_str)
        return Packet(version, type_id, literal_value)
