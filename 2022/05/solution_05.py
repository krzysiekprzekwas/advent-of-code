import copy

def get_top_crates(stacks):
    return "".join(stack[-1] for stack in stacks)

with open("input_05.txt", encoding="utf-8") as f:
    file_data = f.read().splitlines()

    start = next(i for i, line in enumerate(file_data) if "1" in line)

    number_of_stacks = int(file_data[start][-2])

    stacks_1 = []
    for stack in range(number_of_stacks):
        stacks_1.append([])

    for line in reversed(file_data[:start]):
        for i, crate in enumerate(line[1::4]):
            if crate != " ":
                stacks_1[i].append(crate)

    stacks_2 = copy.deepcopy(stacks_1)

    moves = []

    for line in file_data[start + 2:]:
        line = line.split()
        moves.append((int(line[1]), int(line[3]), int(line[5])))

    for (amount, source, dest) in moves:
        # stacks_1
        for i in range(amount):
            stacks_1[dest-1].extend(stacks_1[source-1][-1:])
            stacks_1[source-1] = stacks_1[source-1][:-1]

        # stacks_2
        stacks_2[dest-1].extend(stacks_2[source-1][-amount:])
        stacks_2[source-1] = stacks_2[source-1][:-amount]


    print(get_top_crates(stacks_1))
    print(get_top_crates(stacks_2))