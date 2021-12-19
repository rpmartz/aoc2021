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


def parse_string(hex_string, packets, pc):
    binary_str = hex_to_bin(hex_string)

    while pc < len(binary_str):

        # parse version
        version_bits = binary_str[pc:pc + 3]
        packet_version = int(version_bits, 2)
        pc += 3

        # parse type
        type_bits = binary_str[pc:pc + 3]
        packet_type = int(type_bits, 2)
        pc += 3

        if packet_type == 4:
            literal_value, pc = parse_literal(binary_str, pc)
            packets.append({
                'version': packet_version,
                'type': packet_type,
                'literal_value': literal_value
            })

        elif packet_type in (0, 1, 2, 3, 5, 6, 7):
            length_type_bit = int(binary_str[pc])
            pc += 1

            if length_type_bit == 0:
                # next 15 bits are total length in bits of the subpackets in this packet
                pass
            elif length_type_bit == 1:
                # the next 11 bits are a number that represents the number of sub-packets immediately contained by this packet.
                ## todo read 11 bits into a number
                num_subpackets = int(binary_str[pc:pc + 11])
                pc += 11



        else:
            raise Exception('Parsed unexpected packet type')

    return packets
