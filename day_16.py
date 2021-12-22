class Packet:

    def __init__(self, version, type_id, literal_value=None, children=None):
        self.version = version
        self.type_id = type_id
        self.literal_value = literal_value
        self.children = children or []


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


def get_packet_version(binary_str) -> int:
    first_three = binary_str[0:3]

    return int(first_three, 2)


def get_packet_type(binary_str) -> int:
    version_bits = binary_str[3:6]

    return int(version_bits, 2)


def parse_literal(binary_str, pc) -> (int, int):
    literal_str = ''

    while True:
        next_bit = binary_str[pc]
        pc += 1

        literal_bits = binary_str[pc:pc + 4]
        literal_str += literal_bits
        pc += 4

        if int(next_bit) == 0:

            # read rest of padding
            while pc % 4 != 0:
                pc += 1

            break

    return int(literal_str, 2), pc


