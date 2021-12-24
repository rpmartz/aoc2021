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
    x = z
    x = x % 26
    z = z // 1
    x = x + 10
    x = eql(x, w)
    x = eql(x, 0)
    y = 25 * x
    y = y + 1
    z = z * y
    y = w + 13
    y = y * x
    z = z + y
    w = int(model_number[index])
    index += 1
    x = z
    x = x % 26
    z = z // 1
    x = x + 13
    x = eql(x, w)
    x = eql(x, 0)
    y = 25
    y = y + 1
    z = z * y
    y = w + 10
    y = y * x
    z = z + y
    w = int(model_number[index])
    index += 1
    x = z
    x = x % 26
    z = z // 1
    x = x + 13
    x = eql(x, w)
    x = eql(x, 0)
    y = 25 * x
    y = y + 1
    z = z * y
    y = w + 3
    y = y * x
    z = z + y
    w = int(model_number[index])
    index += 1
    x = z
    x = x % 26
    z = z // 26
    x = x + -11
    x = eql(x, w)
    x = eql(x, 0)
    y = 25 * x
    y = y + 1
    z = z * y
    y = w + 1
    y = y * x
    z = z + y
    w = int(model_number[index])
    index += 1
    x = z
    x = x % 26
    z = z // 1
    x = x + 11
    x = eql(x, w)
    x = eql(x, 0)
    y = 25 * x
    y = y + 1
    z = z * y
    y = w + 9
    y = y * x
    z = z + y
    w = int(model_number[index])
    index += 1
    x = z
    x = x % 26
    z = z // 26
    x = x + -4
    x = eql(x, w)
    x = eql(x, 0)
    y = 25 * x
    y = y + 1
    z = z * y
    y = w + 3
    y = y * x
    z = z + y
    w = int(model_number[index])
    index += 1
    x = z
    x = x % 26
    z = z // 1
    x = x + 12
    x = eql(x, w)
    x = eql(x, 0)
    y = 25 * x
    y = y + 1
    z = z * y
    y = w + 5
    y = y * x
    z = z + y
    w = int(model_number[index])
    index += 1
    x = z
    x = x % 26
    z = z // 1
    x = x + 12
    x = eql(x, w)
    x = eql(x, 0)
    y = 25 * x
    y = y + 1
    z = z * y
    y = w + 1
    y = y * x
    z = z + y
    w = int(model_number[index])
    index += 1
    x = z
    x = x % 26
    z = z // 1
    x = x + 15
    x = eql(x, w)
    x = eql(x, 0)
    y = 25 * x
    y = y + 1
    z = z * y
    y = w + 0
    y = y * x
    z = z + y
    w = int(model_number[index])
    index += 1
    x = z
    x = x % 26
    z = z // 26
    x = x + -2
    x = eql(x, w)
    x = eql(x, 0)
    y = 25 * x
    y = y + 1
    z = z * y
    y = w + 13
    y = y * x
    z = z + y
    w = int(model_number[index])
    index += 1
    x = z
    x = x % 26
    z = z // 26
    x = x + -5
    x = eql(x, w)
    x = eql(x, 0)
    y = 25 * x
    y = y + 1
    z = z * y
    y = w + 7
    y = y * x
    z = z + y
    w = int(model_number[index])
    index += 1
    x = z
    x = x % 26
    z = z // 26
    x = x + -11
    x = eql(x, w)
    x = eql(x, 0)
    y = 25 * x
    y = y + 1
    z = z * y
    y = w + 15
    y = y * x
    z = z + y
    w = int(model_number[index])
    index += 1
    x = z
    x = x % 26
    z = z // 26
    x = x + -13
    x = eql(x, w)
    x = eql(x, 0)
    y = 25 * x
    y = y + 1
    z = z * y
    y = w + 12
    y = y * x
    z = z + y
    w = int(model_number[index])
    index += 1
    x = z
    x = x % 26
    z = z // 26
    x = x + -10
    x = eql(x, w)
    x = eql(x, 0)
    y = 25 * x
    y = y + 1
    z = z * y
    y = w + 8
    y = y * x
    z = z + y

    return z == 0

if __name__ == '__main__':
    start = int(14 * '9')

    for i in range(start, 1, -1):
        if i % 1000000 == 0:
            print(f'Tried from {start} down through {i}')
        model_number = str(i)
        if '0' in model_number:
            continue
        elif is_valid(model_number):
            print(f'min: {model_number}')
            break
