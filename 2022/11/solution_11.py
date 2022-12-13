from copy import deepcopy

with open("input_11.txt") as file:
    monkey_descriptions = file.read().split('\n\n')

    state = {}
    state['monkey_bussines_scores'] = [0] * len(monkey_descriptions)
    state['items'], state['operations'], state['divisors'], state['throw_options'] = {}, {}, {}, {}

    for description in monkey_descriptions:
        lines = description.splitlines()

        monkey_id = int(lines[0][7])
        state['items'][monkey_id] = [int(x) for x in lines[1][18:].split(', ')]
        state['operations'][monkey_id] = lines[2][19:]
        state['divisors'][monkey_id] = int(lines[3][21:])
        state['throw_options'][monkey_id] = int(lines[4][29:]), int(lines[5][30:])

state_2 = deepcopy(state)

for rounds in range(20):
    for i in range(len(monkey_descriptions)):
        state['monkey_bussines_scores'][i] += len(state['items'][i])

        for j in range(len(state['items'][i])):
            state['items'][i][j] = eval(state['operations'][i].replace("old", str(state['items'][i][j]))) // 3
            
            if state['items'][i][j] % state['divisors'][i] == 0:
                state['items'][state['throw_options'][i][0]].append(state['items'][i][j])
            else:
                state['items'][state['throw_options'][i][1]].append(state['items'][i][j])
        state['items'][i] = []

state['monkey_bussines_scores'].sort()

print(state['monkey_bussines_scores'][-1] * state['monkey_bussines_scores'][-2])

master_divider = 1
for div in state_2['divisors'].values():
    master_divider *= div

for rounds in range(10000):
    for i in range(len(monkey_descriptions)):
        state_2['monkey_bussines_scores'][i] += len(state_2['items'][i])

        for j in range(len(state_2['items'][i])):
            state_2['items'][i][j] = eval(state_2['operations'][i].replace("old", str(state_2['items'][i][j]))) % master_divider
            
            if state_2['items'][i][j] % state_2['divisors'][i] == 0:
                state_2['items'][state_2['throw_options'][i][0]].append(state_2['items'][i][j])
            else:
                state_2['items'][state_2['throw_options'][i][1]].append(state_2['items'][i][j])
        state_2['items'][i] = []

state_2['monkey_bussines_scores'].sort()

print(state_2['monkey_bussines_scores'][-1] * state_2['monkey_bussines_scores'][-2])