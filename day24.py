def eql(a, b):
    if a == b:
        return 1

    return 0
#
#
#
#
# start = int(14 * '9')
#
# for i in range(start, 0, -1):
#     model_number = str(i)
#     if '0' in model_number:
#         continue
#
#     # todo run ALU
#     pass

def parse(symbol: str):
    if symbol.isalpha():
        return symbol
    else:
        return int(symbol)

def parse_instructions():
    with open('data/day24.txt', 'r') as f:
        unparsed_lines = [line.strip() for line in f.readlines()]

    parsed_instructions = []

    for line in unparsed_lines:

        if line.startswith('inp'):
            op, first = line.split()

            stmt = f'{first} = model_number[index]'
            parsed_instructions.append(stmt)

            parsed_instructions.append('index += 1')
        else:
            op, first, second = line.split()
            if op == 'inp':
                stmt = f'{first} = model_number[index]'
                parsed_instructions.append(stmt)
                parsed_instructions.append('index += 1')
            elif op == 'mul':
                stmt = f'{first} = {first} * {parse(second)}'
                parsed_instructions.append(stmt)
            elif op == 'add':
                stmt = f'{first} = {first} + {parse(second)}'
                parsed_instructions.append(stmt)
            elif op == 'div':
                stmt = f'{first} = {first} // {parse(second)}'
                parsed_instructions.append(stmt)
            elif op == 'mod':
                stmt = f'{first} = {first} % {parse(second)}'
                parsed_instructions.append(stmt)
            elif op == 'eql':
                stmt = f'{first} = eql({first}, {parse(second)})'
                parsed_instructions.append(stmt)

    return parsed_instructions

if __name__ == '__main__':
    inst = parse_instructions()
    with open('24.txt', 'w') as f:
        f.writelines('\n'.join(inst))