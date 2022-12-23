def get_node(node, tree):
    value = tree[node]
    if isinstance(value, int):
        return value
    if value is None:
        return None

    l, op, r = value.split()

    value_1 = get_node(l, tree)
    value_2 = get_node(r, tree)

    if None in (value_1, value_2):
        return None

    return int(eval(f"{value_1}{op}{value_2}"))

input = {}

with open("input_21.txt") as file:
    lines = file.read().splitlines()
    for line in lines:
        a, b = line.split(': ')
        input[a] = int(b) if b.isnumeric() else b

answer_1 = get_node('root', input)
print(answer_1)

def find_humn(node, tree, expected):
    value = tree[node]
    if node == 'humn':
        return expected
    if isinstance(value, int):
        return value
    if value is None:
        return None

    left, op, right = value.split()

    value_1 = get_node(left, tree)
    value_2 = get_node(right, tree)

    if value_1 is None:
        if op == '*':
            exp = expected//value_2
        if op == '+':
            exp = expected-value_2
        if op == '-':
            exp = expected+value_2
        if op == '/':
            exp = expected*value_2
        return find_humn(left, input, exp)
    else:
        if op == '*':
            exp = expected//value_1
        if op == '+':
            exp = expected-value_1
        if op == '-':
            exp = value_1-expected
        if op == '/':
            exp = value_1/expected
        return find_humn(right, input, exp)

input['humn'] = None
left, _, right = input['root'].split()

value_1 = get_node(left, input)
value_2 = get_node(right, input)

if value_1 is None:
    answer_2 = find_humn(left, input, value_2)
else:
    answer_2 = find_humn(right, input, value_1)

print(answer_2)
