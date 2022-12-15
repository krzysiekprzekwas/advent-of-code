def manhattan_distance(x_1, y_1, x_2, y_2):
    return abs(x_1 - x_2) + abs(y_1 - y_2)

with open("input_15.txt") as file:
    lines = file.read().strip().splitlines()
    height = 2_000_000
    coords = []

    beacons_on_row = 0
    occupied_positions = set()
    beacons_on_height = set()
    
    for i in lines:
        split = i.split(" ")
        sensor_x = int(split[2][2:-1])
        sensor_y = int(split[3][2:-1])
        beacon_x = int(split[8][2:-1])
        beacon_y = int(split[9][2:])
        distance = manhattan_distance(sensor_x, sensor_y, beacon_x, beacon_y)
        coords.append((sensor_x, sensor_y, beacon_x, beacon_y, distance))

        if beacon_y == height:  
            beacons_on_height.add(beacon_x)

        distance_at_row = distance - abs(sensor_y - height)
        occupied_positions.update(range(sensor_x - distance_at_row, sensor_x + distance_at_row + 1))

    print(len(occupied_positions) - len(beacons_on_height))

    for y in range(0, 4_000_000):
        occupied_positions = set()
        for sensor_x, sensor_y, beacon_x, beacon_y, distance in coords:
            y_range = abs(sensor_y - y)
            if y_range > distance:
                continue
            
            x_range = distance - y_range
            occupied_positions.update(range(sensor_x - x_range, sensor_x + x_range+1))
    
        start = min(occupied_positions)
        end = max(occupied_positions)
    
        free_spot = set(range(start, end+1)).difference(occupied_positions)
        if free_spot:
            print(4_000_000 * list(free_spot)[0] + y)
