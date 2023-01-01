import re  


def get_new_dir(dir, r):
    if r == "R":
        if dir == (0, 1):
            return (1, 0)
        elif dir == (1, 0):
            return (0, -1)
        elif dir == (0, -1):
            return (-1, 0)
        elif dir == (-1, 0):
            return (0, 1)
    else:
        if dir == (0, 1):
            return (-1, 0)
        elif dir == (-1, 0):
            return (0, -1)
        elif dir == (0, -1):
            return (1, 0)
        elif dir == (1, 0):
            return (0, 1)

def get_sign(dir):
    if dir == (0, 1):
        return 0
    elif dir == (1, 0):
        return 1
    elif dir == (0, -1):
        return 2
    elif dir == (-1, 0):
        return 3

with open("input_22.txt") as file:
    lines = file.read().splitlines()
    instructions = lines[-1]
    grove = []
    for line in lines[:-2]:
        grove.append(line)

    adj_grove = []
    width = max(map(len, grove))
    for line in grove:
        adj_grove.append(line.ljust(width))

start_column = adj_grove[0].find(".")

loc = (0, start_column)
d = (0, 1)

moves = re.findall(r"(\d+)([RL]?)", instructions)

for x, dir in moves:
    length = int(x)
    for _ in range(length):
        new_loc = loc
        while True:
            prop_new_loc = tuple(map(sum, zip(new_loc, d)))
            new_loc = (
                prop_new_loc[0] % len(adj_grove),
                prop_new_loc[1] % width
                )
            if adj_grove[new_loc[0]][new_loc[1]] != " ":
                break
        if adj_grove[new_loc[0]][new_loc[1]] == "#":
            break
        loc = new_loc
    
    if dir:
        d = get_new_dir(d, dir)

sign = get_sign(d)

print(1000 * (loc[0] + 1) + 4 * (loc[1] + 1) + sign)