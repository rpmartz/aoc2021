def eql(a, b):
    if a == b:
        return 1

    return 0






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

            stmt = f'{first} = int(model_number[index])'
            parsed_instructions.append(stmt)

            parsed_instructions.append('index += 1')
        else:
            op, first, second = line.split()

            if op == 'mul':
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

def is_valid(model_number):
    x, y, z = 0, 0, 0
    index = 0

    w = int(model_number[index])
    index += 1
    x = 1
    y = 26
    z = z * y
    z = z + (w + 13)
    w = int(model_number[index])
    index += 1
    z = z * y
    z = z + (w + 10)
    w = int(model_number[index])
    index += 1
    y = 26
    z = z * y
    z = z + (w + 3)
    w = int(model_number[index])
    index += 1
    z = z // 26
    z = z * 26
    z = z + (w + 1)
    w = int(model_number[index])
    index += 1
    z = z * 26
    z = z + w + 9
    w = int(model_number[index])
    index += 1
    z = z // 26
    y = 26
    z = z * y
    y = (w + 3)
    z = z + y
    w = int(model_number[index])
    index += 1
    y = 26
    z = z * y
    y = (w + 5)
    z = z + y
    w = int(model_number[index])
    index += 1
    y = 26
    z = z * y
    y = (w + 1)
    z = z + y
    w = int(model_number[index])
    index += 1
    y = 26
    z = z * y
    y = w
    z = z + y
    w = int(model_number[index])
    index += 1
    z = z // 26
    y = 26
    z = z * y
    y = (w + 13)
    z = z + y
    w = int(model_number[index])
    index += 1
    z = z // 26
    y = 26
    z = z * y
    y = (w + 7)
    z = z + y
    w = int(model_number[index])
    index += 1
    z = z // 26
    y = 26
    z = z * y
    y = (w + 15)
    z = z + y
    w = int(model_number[index])
    index += 1
    z = z // 26
    y = 26
    z = z * y
    y = (w + 12) * x
    z = z + y
    w = int(model_number[index])
    index += 1
    z = z // 26
    z = z * 26
    z = z + (w + 8)

    return z == 0

if __name__ == '__main__':
    inst = parse_instructions()
    with open('24.txt', 'w') as f:
        f.writelines('\n'.join(inst))

    start = int(14 * '9')

    for i in range(start, 1, -1):
        model_number = str(i)
        if '0' in model_number:
            continue
        elif is_valid(model_number):
            print(model_number)
            break

        if i % 1000 == 0:
            print(i)