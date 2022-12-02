def score_round(p1, p2):
    if p1 == p2:
        return p2 + 4
    elif (p1 - 1) % 3 == p2:
        return p2 + 1
    else:
        return p2 + 7
 
opponent_offset = ord("A")
player_offset = ord("X")
 
with open("input_02.txt", "r") as f:
    file_data = f.read().splitlines()
    moves_data = [line.split() for line in file_data]
    normalized_moves_data = [(ord(p1) - opponent_offset, ord(p2) - player_offset) for p1, p2 in moves_data]
 
final_moves = [(p1, (p1 + p2 - 1) % 3) for p1, p2 in normalized_moves_data]
 
print(sum(score_round(p1, p2) for p1, p2 in normalized_moves_data))
print(sum(score_round(p1, p2) for p1, p2 in final_moves))