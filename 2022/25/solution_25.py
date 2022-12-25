def SNAFU_to_decimal(val):
    sum = 0
    BASE = 5
    for i, c in enumerate(val[::-1]):
        if c == '=':
            sum -= 2*BASE**i
        elif c == '-':
            sum -= BASE**i
        else:
            sum += int(c)*BASE**i
    return sum

def decimal_to_SNAFU(val):
    sum = ''
    BASE = 5
    i = 0
    while(val):
        c = val % BASE
        val //= BASE

        if c == 4:
            sum += '-'
            val += 1
        elif c == 3:
            sum += '='
            val += 1
        else:
            sum += str(c)
    return sum[::-1]

with open("input_25.txt") as file:
    lines = file.read().splitlines()
    sum = 0
    for line in lines:
        sum += SNAFU_to_decimal(line)
    print(sum)
    print(decimal_to_SNAFU(sum))