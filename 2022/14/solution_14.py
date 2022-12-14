from copy import deepcopy


with open("input_14.txt") as file:
     lines = file.read().strip().splitlines()
     wall_descriptions = [[list(map(int, j.split(','))) for j in l.split(' -> ') ] for l in lines]

rocks_1 = set()
floor_y = 0

for wall in wall_descriptions:
    for i in range(len(wall) - 1):
        (x1, y1),(x2, y2) = wall[i], wall[i + 1]
        if x1==x2:
            for wall_y in range(min(y1, y2), max(y1, y2) + 1):
                rocks_1.add((x1,wall_y))
                floor_y = max(floor_y, wall_y)
        else:
            for wall_x in range(min(x1, x2), max(x1, x2) + 1):
                rocks_1.add((wall_x, y1))
            floor_y = max(floor_y, y1)

rocks_2 = deepcopy(rocks_1)

answer_1 = answer_2 = 0
start_coord = 500, 0
while True: 
    s_x, s_y = start_coord
    while s_y != floor_y:
        if (
            (p:=(s_x, s_y+1)) not in rocks_1 or 
            (p:=(s_x-1, s_y+1)) not in rocks_1 or 
            (p:=(s_x+1, s_y+1)) not in rocks_1
            ):
            s_x, s_y = p
        else:
            break
    
    if s_y == floor_y:
        break

    rocks_1.add((s_x, s_y))
    answer_1 += 1
print(answer_1)

while (s_x, s_y) != start_coord:
    s_x, s_y = start_coord
    while s_y != floor_y+1: 
        if (
            (p:=(s_x, s_y+1)) not in rocks_2 or 
            (p:=(s_x-1, s_y+1)) not in rocks_2 or 
            (p:=(s_x+1, s_y+1)) not in rocks_2
            ):
            s_x, s_y= p
        else:
            break
        
    rocks_2.add((s_x, s_y))
    answer_2 +=1
print(answer_2)