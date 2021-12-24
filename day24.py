def eql(a, b):
    if a == b:
        return 1

    return 0

def run(model_num):
    w, x, y, z = 0, 0, 0, 0
    pc = 0

    w = int(model_num[pc])
    pc += 1

    # mul x 0
    # add x z
    # mod x 26
    x = z % 26
    # div z 1
    # add x 10
    x = x + 10
    # eql x w
    x = eql(x, w)
    # eql x 0
    x = eql(x, 0)
    # mul y 0
    # add y 25
    # mul y x
    # add y 1
    y = (25 * x) + 1
    # mul z y
    z = z * y
    # mul y 0
    # add y w
    # add y 13
    # mul y x
    y = (w + 13) * x
    # add z y
    z = z + y
    # inp w
    w = int(model_num[pc])
    pc += 1

    # mul x 0
    x = 0
    # add x z
    x = x + z
    # mod x 26
    x = x % 26
    # div z 1
    z = z / 1
    # add x 13
    x = x + 13
    # eql x w
    x = eql(x, w)
    # eql x 0
    x = eql(x, 0)
    # mul y 0
    # add y 25
    # mul y x
    # add y 1
    y = (25 * x) + 1
    # mul z y
    z = z * y
    # mul y 0
    # add y w
    # add y 10
    # mul y x
    y = (w + 10) * x
    # add z y
    z = z + y
    # inp w
    w = int(model_num[pc])
    pc += 1

    # mul x 0
    # add x z
    # mod x 26
    # div z 1
    # add x 13
    # eql x w
    # eql x 0
    # mul y 0
    # add y 25
    # mul y x
    # add y 1
    # mul z y
    # mul y 0
    # add y w
    # add y 3
    # mul y x
    # add z y
    # inp w
    # mul x 0
    # add x z
    # mod x 26
    # div z 26
    # add x -11
    # eql x w
    # eql x 0
    # mul y 0
    # add y 25
    # mul y x
    # add y 1
    # mul z y
    # mul y 0
    # add y w
    # add y 1
    # mul y x
    # add z y
    # inp w
    # mul x 0
    # add x z
    # mod x 26
    # div z 1
    # add x 11
    # eql x w
    # eql x 0
    # mul y 0
    # add y 25
    # mul y x
    # add y 1
    # mul z y
    # mul y 0
    # add y w
    # add y 9
    # mul y x
    # add z y
    # inp w
    # mul x 0
    # add x z
    # mod x 26
    # div z 26
    # add x -4
    # eql x w
    # eql x 0
    # mul y 0
    # add y 25
    # mul y x
    # add y 1
    # mul z y
    # mul y 0
    # add y w
    # add y 3
    # mul y x
    # add z y
    # inp w
    # mul x 0
    # add x z
    # mod x 26
    # div z 1
    # add x 12
    # eql x w
    # eql x 0
    # mul y 0
    # add y 25
    # mul y x
    # add y 1
    # mul z y
    # mul y 0
    # add y w
    # add y 5
    # mul y x
    # add z y
    # inp w
    # mul x 0
    # add x z
    # mod x 26
    # div z 1
    # add x 12
    # eql x w
    # eql x 0
    # mul y 0
    # add y 25
    # mul y x
    # add y 1
    # mul z y
    # mul y 0
    # add y w
    # add y 1
    # mul y x
    # add z y
    # inp w
    # mul x 0
    # add x z
    # mod x 26
    # div z 1
    # add x 15
    # eql x w
    # eql x 0
    # mul y 0
    # add y 25
    # mul y x
    # add y 1
    # mul z y
    # mul y 0
    # add y w
    # add y 0
    # mul y x
    # add z y
    # inp w
    # mul x 0
    # add x z
    # mod x 26
    # div z 26
    # add x -2
    # eql x w
    # eql x 0
    # mul y 0
    # add y 25
    # mul y x
    # add y 1
    # mul z y
    # mul y 0
    # add y w
    # add y 13
    # mul y x
    # add z y
    # inp w
    # mul x 0
    # add x z
    # mod x 26
    # div z 26
    # add x -5
    # eql x w
    # eql x 0
    # mul y 0
    # add y 25
    # mul y x
    # add y 1
    # mul z y
    # mul y 0
    # add y w
    # add y 7
    # mul y x
    # add z y
    # inp w
    # mul x 0
    # add x z
    # mod x 26
    # div z 26
    # add x -11
    # eql x w
    # eql x 0
    # mul y 0
    # add y 25
    # mul y x
    # add y 1
    # mul z y
    # mul y 0
    # add y w
    # add y 15
    # mul y x
    # add z y
    # inp w
    # mul x 0
    # add x z
    # mod x 26
    # div z 26
    # add x -13
    # eql x w
    # eql x 0
    # mul y 0
    # add y 25
    # mul y x
    # add y 1
    # mul z y
    # mul y 0
    # add y w
    # add y 12
    # mul y x
    # add z y
    # inp w
    # mul x 0
    # add x z
    # mod x 26
    # div z 26
    # add x -10
    # eql x w
    # eql x 0
    # mul y 0
    # add y 25
    # mul y x
    # add y 1
    # mul z y
    # mul y 0
    # add y w
    # add y 8
    # mul y x
    # add z y



def run_alu():
    # push digits on stack
    pass


start = int(14 * '9')

for i in range(start, 0, -1):
    model_number = str(i)
    if '0' in model_number:
        continue

    # todo run ALU
    pass