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
    x = (z % 26) + 10
    x = eql(x, w)
    x = eql(x, 0)
    z = ((z // 1) * ((25 * x) + 1)) + ((w + 13) * x)
    w = int(model_number[index])
    index += 1
    x = z % 26
    z = z // 1
    x = eql(x + 13, w)
    x = eql(x, 0)
    z = (26 * z) + ((w + 10) * x)
    w = int(model_number[index])
    index += 1
    x = z % 26
    z = z // 1
    x = eql(x + 13, w)
    x = eql(x, 0)
    z = (z * ((25 * x) + 1)) + ((w + 3) * x)
    w = int(model_number[index])
    index += 1
    x = x % 26
    x = eql(x + -11, w)
    x = eql(x, 0)
    z = ((z // 26) * ((25 * x) + 1)) + ((w + 1) * x)
    w = int(model_number[index])
    index += 1
    x = z % 26
    x = eql(x + 11, w)
    x = eql(x, 0)
    z = ((z // 1) * ((25 * x) + 1)) + ((w + 9) * x)
    w = int(model_number[index])
    index += 1
    x = z % 26
    x = eql(x - 4, w)
    x = eql(x, 0)
    z = ((z // 26) * ((25 * x) + 1)) + ((25 * x) + 1)
    w = int(model_number[index])
    index += 1
    x = z % 26
    x = eql(x + 12, w)
    x = eql(x, 0)
    z = ((z // 1) * ((25 * x) + 1)) + ((w + 5) * x)
    w = int(model_number[index])
    index += 1
    x = z % 26
    x = x + 12
    x = eql(x, w)
    x = eql(x, 0)
    z = ((z // 1) * ((25 * x) + 1)) + ((w + 1) * x)
    w = int(model_number[index])
    index += 1
    x = (z % 26) + 15
    x = eql(x, w)
    x = eql(x, 0)
    z = ((z // 1) * ((25 * x) + 1)) + (w * x)
    w = int(model_number[index])
    index += 1
    x = (z % 26) + -2
    x = eql(x, w)
    x = eql(x, 0)
    z = ((z // 26) * ((25 * x) + 1)) + ((w + 13) * x)
    w = int(model_number[index])
    index += 1
    x = (z % 26) + -5
    x = eql(x, w)
    x = eql(x, 0)
    z = ((z // 26) * ((25 * x) + 1)) + ((w + 7) * x)
    w = int(model_number[index])
    index += 1
    x = (z % 26) + -11
    x = eql(x, w)
    x = eql(x, 0)
    z = ((z // 26) * ((25 * x) + 1)) + ((w + 15) * x)
    w = int(model_number[index])
    index += 1
    x = (z % 26) + -13
    x = eql(x, w)
    x = eql(x, 0)
    z = ((z // 26) * ((25 * x) + 1)) + ((w + 12) * x)
    w = int(model_number[index])
    index += 1
    x = (z % 26) + -10
    x = eql(x, w)
    x = eql(x, 0)
    z = ((z // 26) * ((25 * x) + 1)) + ((w + 8) * x)

    return z == 0

if __name__ == '__main__':
    start = int(14 * '9')

    valid_codes = set()

    for i in range(start, 1, -1):
        if i % 1000000 == 0:
            print(f'Tried from {start} down through {i}')
        model_number = str(i)
        if '0' in model_number:
            continue
        elif is_valid(model_number):
            valid_codes.add(int(model_number))

    print(f'max: {max(valid_codes)}')
    print(f'min: {min(valid_codes)}')
