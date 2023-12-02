import re

with open("input_01.txt", "r") as f:
    data = f.read().splitlines()

    max_cubes = {
        'red':12,
        'green':13,
        'blue':14
    }

    score_1 = 0
    score_2 = 0
    id = 0

    for game in data:

        min_game_cubes = {
            'red':0,
            'green':0,
            'blue':0
        }

        game = game.split(':')
        id += 1
        draws = game[1].split(';')
        valid = True

        for draw in draws:
            cubes = draw.split(',')
            
            for cube in cubes:
                value = int(re.findall(r'\d+',cube)[0])
                color = re.findall(r'red|green|blue',cube)[0]

                min_game_cubes[color] = max(value, min_game_cubes[color])

                if value > max_cubes[color]:
                    valid = False
              
        if valid:
            score_1 += id
        
        score_2 += (min_game_cubes['red'] * min_game_cubes['green'] * min_game_cubes['blue'])

print(score_1)
print(score_2)