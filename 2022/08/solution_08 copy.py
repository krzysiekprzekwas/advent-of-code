
array = []
with open("input_test_08.txt") as file:
    lines = file.read().splitlines()
    for line in lines:
        array.append([int(x) for x in list(line)])

def import_file():
    with open("Aoc_Inputs\Advent_08_22.txt") as f: 
        return [list(line) for line in f.read().splitlines()]

grid  = import_file()
vis = 0
for r in range(len(grid)):
    for c in range(len(grid[r])):
        tree = grid[r][c]
        if (
            # Check left
            all(grid[r][x] < tree for x in range(c)) or 
            # Check right
            all(grid[r][x] < tree for x in range(c+1, len(grid[r]))) or 
            # Check top
            all(grid[x][c] < tree for x in range(r)) or 
            # Check bottom
            all(grid[x][c] < tree for x in range(r+1, len(grid)))
            ): 
            vis += 1
print(vis)
