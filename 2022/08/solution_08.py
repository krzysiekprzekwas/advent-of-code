array = []
with open("input_08.txt") as file:
    lines = file.read().splitlines()
    for line in lines:
        array.append([int(x) for x in list(line)])

visible_trees = 0
max_scenic_score = 0

for i in range(len(array)):
    for j in range(len(array[i])):
        tree_height = array[i][j]

        if (
            # Check left
            all(array[i][x] < tree_height for x in range(j)) or 
            # Check right
            all(array[i][x] < tree_height for x in range(j+1, len(array[i]))) or 
            # Check top
            all(array[x][j] < tree_height for x in range(i)) or 
            # Check bottom
            all(array[x][j] < tree_height for x in range(i+1, len(array)))
            ): 
            visible_trees += 1
        
        left_view = right_view = top_view = bottom_view = 0

        # Calculate left
        for x in range(j - 1, -1, -1):
            left_view += 1
            if array[i][x] >= tree_height: break
        # Calculate right
        for x in range(j+1, len(array[i])):
            right_view += 1
            if array[i][x] >= tree_height: break
        # Calculate top
        for x in range(i - 1, -1, -1):
            top_view += 1
            if array[x][j] >= tree_height: break
        # Calculate bottom
        for x in range(i+1, len(array[i])):
            bottom_view += 1
            if array[x][j] >= tree_height: break

        if (left_view * right_view * top_view * bottom_view > max_scenic_score):
            max_scenic_score = max(max_scenic_score, left_view * right_view * top_view * bottom_view)
            print(i, j)

print(visible_trees)
print(max_scenic_score)