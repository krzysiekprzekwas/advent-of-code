DIRECTION = {'R': [1, 0], 'U': [0, 1], 'L': [-1, 0], 'D': [0, -1]}

def add_lists(list_1, list_2):
    return [a + b for (a, b) in zip(list_1, list_2)]

def update_knot(previous_knot, current_knot):
    head_x, head_y = previous_knot
    tail_x, tail_y = current_knot
    
    if (tail_y == head_y):
        d = tail_x - head_x
        if (d <= -2):
            tail_x += 1
        elif (d >= 2):
            tail_x -= 1
    elif (tail_x == head_x):
        d = tail_y - head_y
        if (d <= -2):
            tail_y += 1
        elif (d >= 2):
            tail_y -= 1
    else:
        if ((abs(tail_x - head_x) + abs(tail_y - head_y)) > 2):
            if (head_x > tail_x):
                x_move = 1
            else:
                x_move = -1
            if (head_y > tail_y):
                y_move = 1
            else:
                y_move = -1
            tail_x += x_move
            tail_y += y_move
            
    return [tail_x, tail_y]

with open("input_09.txt") as file:

    knots_positions_1 = [[0, 0] for _ in range(0, 2)]
    knots_positions_2 = [[0, 0] for _ in range(0, 10)]

    visited_1 = set()
    visited_2 = set()

    visited_1.add((0, 0))
    visited_2.add((0, 0))
    
    for line in file:
        direction, steps = line.split()
        steps = int(steps)

        for _ in range(int(steps)):
            knots_positions_1[0] = add_lists(knots_positions_1[0], DIRECTION[direction])
            knots_positions_2[0] = add_lists(knots_positions_2[0], DIRECTION[direction])

            for i in range(1, len(knots_positions_1)):
                knots_positions_1[i] = update_knot(knots_positions_1[i - 1], knots_positions_1[i])
            for i in range(1, len(knots_positions_2)):
                knots_positions_2[i] = update_knot(knots_positions_2[i - 1], knots_positions_2[i])

            visited_1.add((tuple(knots_positions_1[1])))
            visited_2.add((tuple(knots_positions_2[9])))

print(len(visited_1))
print(len(visited_2))
