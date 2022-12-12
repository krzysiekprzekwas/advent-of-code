from math import inf


def get_valid_paths(working_array, row, column):
    value = ord(working_array[row][column])
    edges = []
    # Right
    if column < len(working_array[row])-1 and ord(working_array[row][column+1]) - value <= 1:
        edges.append(f'{row}x{column+1}')
    # Left
    if column > 0 and ord(working_array[row][column-1]) - value <= 1:
        edges.append(f'{row}x{column-1}')
    # Down
    if row < len(working_array)-1 and ord(working_array[row+1][column]) - value <= 1:
        edges.append(f'{row+1}x{column}')
    # Up
    if row > 0 and ord(working_array[row-1][column]) - value <= 1:
        edges.append(f'{row-1}x{column}')

    return edges

# Stolen from https://onestepcode.com/graph-shortest-path-python/
def shortest_path(graph, node1, node2):
    path_list = [[node1]]
    path_index = 0
    # To keep track of previously visited nodes
    previous_nodes = {node1}
    if node1 == node2:
        return path_list[0]
        
    while path_index < len(path_list):
        current_path = path_list[path_index]
        last_node = current_path[-1]
        next_nodes = graph[last_node]
        # Search goal node
        if node2 in next_nodes:
            current_path.append(node2)
            return current_path
        # Add new paths
        for next_node in next_nodes:
            if not next_node in previous_nodes:
                new_path = current_path[:]
                new_path.append(next_node)
                path_list.append(new_path)
                # To avoid backtracking
                previous_nodes.add(next_node)
        # Continue to next path in list
        path_index += 1
    # No path is found
    return []

array = []
with open("input_12.txt") as file:
    lines = file.read().splitlines()
    for line in lines:
        array.append(list(line))

graph = {}

start = ''
end = ''

potential_starts = []

for i in range(len(array)):
    for j in range(len(array[i])):
        if array[i][j] == 'S':
            start = f'{i}x{j}'
            array[i][j] = 'a'
        elif array[i][j] == 'E':
            end = f'{i}x{j}'
            array[i][j] = 'z'

for i in range(len(array)):
    for j in range(len(array[i])):
        graph[f'{i}x{j}'] = get_valid_paths(array, i, j)
        if array[i][j] == 'a':
            potential_starts.append(f'{i}x{j}')

potential_min_path = inf
for potential_start in potential_starts:
    val = len(shortest_path(graph, potential_start, end))
    if val:
        potential_min_path = min(potential_min_path, val)

print(len(shortest_path(graph, start, end))-1)
print(potential_min_path-1)