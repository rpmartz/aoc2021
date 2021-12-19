# BITS has a single packet that contains many other packets, and potentially some padding

# every packet has standard header:
## first 3 bits are packet version version 100 = 4

## next 3 bits encode packet type id

### packets with type ID 4 represent a literal value that encode a single binary number

#### to encode this, the number is padded with leading zeros until the length is a multiple
#### of four bits, and then broken into groups prefixed by one except for the last, which is
### prefixed by zero

### every other type of packet is an operator packet that contains one or more packets
### operator packet has a **length type ID** by the bit immediately after the header, where 0
### means the next 15 bits are a number that represents the total length in bits of the sub-packets
### contained in the packet
### if the length type id is 1, then next 11 bits are the number of **sub-packets** that immediately follow the packet

def bin_string_for_char(c):
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

    return hex_to_bin[c]


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


def parse_string(hex_string):
    binary_str = hex_to_bin(hex_string)

    pc = 0
    while pc < len(binary_str):

        # parse version
        version_bits = binary_str[pc] + binary_str[pc + 3]
        packet_version = int(version_bits, 2)
        pc += 3

        # parse type
        type_bits = binary_str[pc] + binary_str[pc + 3]
        packet_type = int(type_bits, 2)
        pc += 3

        if packet_type == 4:
            # todo parse literal
            pass
        elif packet_type in (0, 1, 2, 3, 5, 6, 7):
            # todo parse operator
            pass
        else:
            raise Exception('Parsed unexpected packet type')
